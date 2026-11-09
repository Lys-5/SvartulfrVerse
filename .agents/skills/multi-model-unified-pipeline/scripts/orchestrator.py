#!/usr/bin/env python3
"""Multi-Model Unified Pipeline Orchestrator CLI.

Unifies the 4 daily Svartulfr Verse automations into a single 5-stage Master Pipeline
orchestrated by a 3-Tier Multi-Model Team & Open-Provider Plug & Play Registry,
with real-time detection of PC OMEN Desktop AI Clients and Local Proxy (:5005),
plus an interactive HTML Telemetry Dashboard.

Key design decisions (per workflow-skill-creator):
- Uses argparse with subcommands (detect-clients, route-model, run-tier, run-all, dashboard).
- All subcommands write structured output to --output (file output default).
- Uses Python stdlib only (urllib, json, argparse, subprocess, time, pathlib, csv, io).
- Cross-process file-lock rate limiting using time.monotonic(), RateLimitError on HTTP 429,
  exponential backoff on 5xx, and horizontal fallback to the twin model in the same Tier.
"""

import argparse
import csv
import datetime
import html
import io
import json
import os
import pathlib
import subprocess
import sys
import time
from urllib import error as urllib_error
from urllib import parse as urllib_parse
from urllib import request as urllib_request

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent
ROOT = SKILL_DIR.parent.parent.parent
SCRATCH = ROOT / 'scratch'
LOGS_AUTO_DIR = ROOT / 'logs' / 'automations'
REGISTRY_PATH = SKILL_DIR / 'references' / 'models_registry.json'
DEFAULT_DASHBOARD_HTML = SCRATCH / 'unified_pipeline_dashboard.html'
DEFAULT_RUN_JSON = SCRATCH / 'unified_pipeline_run.json'
DEFAULT_CLIENTS_JSON = SCRATCH / 'omen_ai_clients_status.json'
DEFAULT_REPORT_MD = SCRATCH / 'daily_maintenance_report.md'


class RateLimitError(Exception):
    """Raised when an API rate limit (HTTP 429) is exceeded after retries."""


class CrossProcessRateLimiter:
    """Cross-process file-lock rate limiter using time.monotonic()."""

    def __init__(self, requests_per_second: float = 2.0, lock_path: pathlib.Path = None):
        self.requests_per_second = max(0.1, float(requests_per_second))
        self.delay = 1.0 / self.requests_per_second
        self.last_request_time = 0.0
        self.lock_path = lock_path or (SCRATCH / '.multi_model_rate_limit.lock')

    def wait(self):
        """Enforces rate limit both in-process (via time.monotonic) and across processes."""
        SCRATCH.mkdir(parents=True, exist_ok=True)
        elapsed = time.monotonic() - self.last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)

        try:
            if not self.lock_path.exists():
                self.lock_path.touch(exist_ok=True)
            with open(self.lock_path, 'r+', encoding='utf-8') as lock_f:
                self._lock_file(lock_f)
                try:
                    lock_f.seek(0)
                    content = lock_f.read().strip()
                    now_mono = time.monotonic()
                    if content:
                        try:
                            state = json.loads(content)
                            last_mono = float(state.get('last_monotonic', 0.0))
                            # Only compare monotonic clocks within the same boot epoch
                            if 0 < last_mono <= now_mono:
                                diff = now_mono - last_mono
                                if diff < self.delay:
                                    time.sleep(self.delay - diff)
                        except (ValueError, TypeError):
                            pass
                    self.last_request_time = time.monotonic()
                    lock_f.seek(0)
                    lock_f.truncate(0)
                    json.dump(
                        {
                            'last_monotonic': self.last_request_time,
                            'pid': os.getpid(),
                            'updated_at': datetime.datetime.now().isoformat(),
                        },
                        lock_f,
                    )
                    lock_f.flush()
                finally:
                    self._unlock_file(lock_f)
        except OSError:
            self.last_request_time = time.monotonic()

    @staticmethod
    def _lock_file(f):
        if os.name == 'nt':
            try:
                import msvcrt
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            except Exception:
                pass
        else:
            try:
                import fcntl
                fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except Exception:
                pass

    @staticmethod
    def _unlock_file(f):
        if os.name == 'nt':
            try:
                import msvcrt
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except Exception:
                pass
        else:
            try:
                import fcntl
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            except Exception:
                pass


class MultiModelAPIClient:
    """HTTP Client for Local Proxy (:5005) & Open-Provider endpoints with rate limiting."""

    def __init__(self, registry: dict):
        rl_cfg = registry.get('rate_limiting', {})
        rps = rl_cfg.get('requests_per_second', 2.0)
        lock_rel = rl_cfg.get('lock_file', 'scratch/.multi_model_rate_limit.lock')
        self.registry = registry
        self.limiter = CrossProcessRateLimiter(
            requests_per_second=rps,
            lock_path=ROOT / lock_rel,
        )
        self.max_retries = int(rl_cfg.get('max_retries', 3))

    def request_json(self, url: str, method: str = 'GET', payload: dict = None, headers: dict = None, timeout: float = 10.0, retries: int = None):
        """Performs an HTTP request with rate limiting, exponential backoff on 5xx, and RateLimitError on 429."""
        max_attempts = retries if retries is not None else self.max_retries
        req_headers = {'Accept': 'application/json', 'User-Agent': 'SvartulfrMultiModelOrchestrator/1.0'}
        if headers:
            req_headers.update(headers)
        data_bytes = None
        if payload is not None:
            data_bytes = json.dumps(payload).encode('utf-8')
            req_headers['Content-Type'] = 'application/json'

        for attempt in range(max_attempts):
            self.limiter.wait()
            try:
                req = urllib_request.Request(url, data=data_bytes, headers=req_headers, method=method)
                with urllib_request.urlopen(req, timeout=timeout) as resp:
                    self.limiter.last_request_time = time.monotonic()
                    raw = resp.read().decode('utf-8', errors='replace')
                    return json.loads(raw) if raw.strip() else {}
            except urllib_error.HTTPError as e:
                self.limiter.last_request_time = time.monotonic()
                if e.code == 429:
                    wait = 2 ** attempt
                    print(
                        f'Rate limited (429) on {url}, retrying in {wait}s '
                        f'(attempt {attempt + 1}/{max_attempts})...',
                        file=sys.stderr,
                    )
                    if attempt == max_attempts - 1:
                        raise RateLimitError(
                            f'HTTP 429 Too Many Requests from {url}. '
                            f'Rate limit ({self.limiter.requests_per_second} req/s) exceeded after {max_attempts} retries.'
                        ) from e
                    time.sleep(wait)
                    continue
                if e.code >= 500:
                    wait = 2 ** attempt
                    print(
                        f'Server error {e.code} on {url}, retrying in {wait}s '
                        f'(attempt {attempt + 1}/{max_attempts})...',
                        file=sys.stderr,
                    )
                    if attempt == max_attempts - 1:
                        raise RuntimeError(
                            f'Server error {e.code} from {url} after {max_attempts} retries.'
                        ) from e
                    time.sleep(wait)
                    continue
                try:
                    body = e.read().decode('utf-8', errors='replace')[:1000]
                except OSError:
                    body = str(e.reason)
                raise RuntimeError(f'HTTP {e.code} from {url}: {body}') from e
            except urllib_error.URLError as e:
                if attempt == max_attempts - 1:
                    raise RuntimeError(
                        f'Failed to connect to {url} after {max_attempts} attempts: {e}'
                    ) from e
                time.sleep(2 ** attempt)


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(f'Multi-Model Registry not found at {REGISTRY_PATH}')
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_output(data, output_file: str):
    out_path = pathlib.Path(output_file)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f'Success! Data written to: {out_path}')
    except (OSError, TypeError) as e:
        print(f'Error writing to file {out_path}: {e}', file=sys.stderr)
        sys.exit(1)


def scan_windows_processes() -> dict:
    """Returns a mapping of lowercase executable name -> list of {pid, memory_kb, image_name}."""
    proc_map = {}
    try:
        proc = subprocess.run(
            ['tasklist', '/FO', 'CSV', '/NH'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=10,
        )
        reader = csv.reader(io.StringIO(proc.stdout))
        for row in reader:
            if len(row) >= 5:
                img_name = row[0].strip()
                pid_str = row[1].strip()
                mem_str = row[4].strip()
                key = img_name.lower()
                proc_map.setdefault(key, []).append({
                    'image_name': img_name,
                    'pid': int(pid_str) if pid_str.isdigit() else pid_str,
                    'memory_raw': mem_str,
                })
    except Exception as e:
        print(f'Warning: Failed to run tasklist: {e}', file=sys.stderr)
    return proc_map


def check_local_proxy_status(api_client: MultiModelAPIClient) -> dict:
    """Checks the local proxy (:5005) live status and configured upstreams."""
    proxy_cfg_path = ROOT / 'proxy' / 'config_free_proxy.json'
    configured_upstreams = 0
    top_pillars = []
    if proxy_cfg_path.exists():
        try:
            with open(proxy_cfg_path, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
            upstreams = cfg.get('upstreams', [])
            configured_upstreams = len(upstreams)
            for u in upstreams[:6]:
                top_pillars.append({
                    'priority': u.get('priority'),
                    'id': u.get('id'),
                    'display_name': u.get('display_name'),
                    'models': u.get('models') or ([u.get('model')] if u.get('model') else []),
                })
        except Exception:
            pass

    live_reachable = False
    live_endpoint = 'http://127.0.0.1:5005/v1/models'
    live_response = None
    try:
        live_response = api_client.request_json(live_endpoint, timeout=2.5, retries=1)
        live_reachable = True
    except Exception:
        try:
            live_response = api_client.request_json('http://127.0.0.1:5005/health', timeout=2.5, retries=1)
            live_reachable = True
        except Exception:
            live_reachable = False

    return {
        'endpoint': 'http://127.0.0.1:5005/v1/chat/completions',
        'live_reachable': live_reachable,
        'status': 'ONLINE' if live_reachable else 'STANDBY_CONFIGURED',
        'configured_upstreams_count': configured_upstreams,
        'top_fiat_pillars': top_pillars,
        'live_probe': live_response if isinstance(live_response, dict) else None,
    }


def detect_clients(registry: dict, limit: int = 20) -> dict:
    """Detects the 5 PC OMEN Desktop AI Clients, Local Proxy :5005, IDE models, and external providers."""
    api_client = MultiModelAPIClient(registry)
    proc_map = scan_windows_processes()
    desktop_cfg = registry.get('desktop_clients', {})

    detected_desktop = []
    running_count = 0
    installed_count = 0

    for cid, info in list(desktop_cfg.items())[:limit]:
        exe = info.get('executable', '')
        install_path = info.get('install_path', '')
        matches = proc_map.get(exe.lower(), [])
        is_running = len(matches) > 0
        is_installed = is_running or (pathlib.Path(install_path).exists() if install_path else False)
        if is_running:
            running_count += 1
        if is_installed or is_running:
            installed_count += 1

        detected_desktop.append({
            'id': cid,
            'display_name': info.get('display_name'),
            'executable': exe,
            'install_path': install_path,
            'installed_on_disk': is_installed,
            'running': is_running,
            'status': 'RUNNING' if is_running else ('INSTALLED_READY' if is_installed else 'NOT_FOUND'),
            'process_count': len(matches),
            'pids': [m['pid'] for m in matches[:10]],
            'version_hint': info.get('version_hint'),
            'assigned_tier': info.get('assigned_tier'),
            'exclusive_scope': info.get('exclusive_scope'),
            'cdp_arg': info.get('cdp_arg'),
        })

    proxy_status = check_local_proxy_status(api_client)

    ide_models_summary = []
    for mid, minfo in list(registry.get('ide_models', {}).items())[:limit]:
        ide_models_summary.append({
            'model_id': mid,
            'display_name': minfo.get('display_name'),
            'vendor': minfo.get('vendor'),
            'context_window': minfo.get('context_window'),
            'subagent_mapping': minfo.get('subagent_mapping'),
            'supported_efforts': list(minfo.get('effort_stages', {}).keys()),
        })

    proxy_keys_cfg = {}
    proxy_cfg_path = ROOT / 'proxy' / 'config_free_proxy.json'
    if proxy_cfg_path.exists():
        try:
            with open(proxy_cfg_path, 'r', encoding='utf-8') as f:
                proxy_keys_cfg = json.load(f).get('keys', {})
        except Exception:
            proxy_keys_cfg = {}

    dotenv_vars = {}
    for env_candidate in (ROOT / '.env', ROOT / 'proxy' / '.env'):
        if env_candidate.exists():
            try:
                for raw_line in env_candidate.read_text(encoding='utf-8', errors='replace').splitlines():
                    line = raw_line.strip()
                    if not line or line.startswith('#') or '=' not in line:
                        continue
                    k, v = line.split('=', 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k and v:
                        dotenv_vars[k] = v
            except Exception:
                pass

    ext_providers = []
    for pid, pinfo in list(registry.get('external_providers_plug_and_play', {}).items())[:limit]:
        auth_env = pinfo.get('auth_env')
        if not auth_env:
            has_env_key = True
        else:
            key_prefix = auth_env.lower().replace('_api_key', '')
            cfg_key_val = proxy_keys_cfg.get(pid) or proxy_keys_cfg.get(key_prefix)
            has_cfg_key = bool(
                (isinstance(cfg_key_val, list) and any(str(x).strip() for x in cfg_key_val))
                or (isinstance(cfg_key_val, str) and cfg_key_val.strip())
            )
            has_env_key = bool(os.environ.get(auth_env) or dotenv_vars.get(auth_env) or has_cfg_key)
        ext_providers.append({
            'provider_id': pid,
            'display_name': pinfo.get('display_name'),
            'endpoint': pinfo.get('endpoint'),
            'protocol': pinfo.get('protocol'),
            'auth_env': auth_env,
            'env_configured': has_env_key,
            'featured_models': pinfo.get('featured_models', [])[:limit],
        })

    result = {
        'timestamp': datetime.datetime.now().isoformat(),
        'host': os.environ.get('COMPUTERNAME', 'PC-OMEN'),
        'summary': {
            'desktop_clients_registered': len(detected_desktop),
            'desktop_clients_running': running_count,
            'desktop_clients_installed': installed_count,
            'local_proxy_5005_status': proxy_status['status'],
            'local_proxy_upstreams': proxy_status['configured_upstreams_count'],
            'ide_models_count': len(ide_models_summary),
            'external_providers_count': len(ext_providers),
        },
        'desktop_clients': detected_desktop,
        'local_proxy_5005': proxy_status,
        'ide_models': ide_models_summary,
        'external_providers': ext_providers,
    }
    # Persist latest snapshot in scratch for dashboard consumption
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with open(DEFAULT_CLIENTS_JSON, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    return result


def route_model(registry: dict, task_type: str, effort: str) -> dict:
    """Resolves the optimal Tier, primary IDE model, normalized effort payload, twin fallback, and desktop client."""
    effort_norm = effort.lower().strip()
    if effort_norm not in ('low', 'medium', 'high'):
        raise ValueError(f'Invalid effort stage: {effort}. Must be low, medium, or high.')

    task_norm = task_type.lower().strip()
    special_policies = registry.get('special_routing_policies', {})
    for sp_id, sp_cfg in special_policies.items():
        if task_norm in [t.lower() for t in sp_cfg.get('allowed_task_types', [])]:
            proc_map = scan_windows_processes()
            exe = sp_cfg.get('executable', '')
            is_running = len(proc_map.get(exe.lower(), [])) > 0
            proxy_status = check_local_proxy_status(MultiModelAPIClient(registry))
            model_id = sp_cfg.get('model_engine', 'gemini-4-argon' if sp_id == 'gemini_desktop' else 'grok-4')
            ide_meta = registry.get('ide_models', {}).get(model_id, {})
            effort_cfg = ide_meta.get('effort_stages', {}).get(effort_norm, {
                'thinking_budget': 8192,
                'reasoning_effort': effort_norm,
                'payload_adapter': {'reasoning_effort': effort_norm},
            })
            return {
                'timestamp': datetime.datetime.now().isoformat(),
                'requested_task_type': task_type,
                'requested_effort': effort_norm,
                'resolved_tier_key': f'special_{sp_id}',
                'resolved_tier_id': sp_id,
                'resolved_tier_name': sp_cfg.get('exclusive_role'),
                'special_policy_enforced': True,
                'policy_note': sp_cfg.get('policy_note'),
                'tier_default_effort': effort_norm,
                'effort_in_tier_allowed_range': True,
                'primary_ide_model': {
                    'model_id': model_id,
                    'display_name': ide_meta.get('display_name', model_id),
                    'vendor': ide_meta.get('vendor', 'Dedicated Desktop Specialist'),
                    'subagent_type': 'image-generator' if sp_id == 'gemini_desktop' else 'inherit',
                    'normalized_effort': effort_cfg,
                },
                'dedicated_desktop_client': {
                    'client_id': sp_id,
                    'executable': exe,
                    'exclusive_role': sp_cfg.get('exclusive_role'),
                    'running': is_running,
                },
                'local_proxy_5005': {
                    'status': proxy_status['status'],
                    'live_reachable': proxy_status['live_reachable'],
                    'configured_upstreams_count': proxy_status['configured_upstreams_count'],
                },
            }

    tiers = registry.get('tiers', {})
    selected_tier_key = None
    selected_tier = None

    for tkey, tinfo in tiers.items():
        if task_norm in [t.lower() for t in tinfo.get('task_types', [])] or task_norm == tinfo.get('id', '').lower():
            selected_tier_key = tkey
            selected_tier = tinfo
            break

    if not selected_tier:
        if effort_norm == 'low':
            selected_tier_key = 'tier_1_scout_fast'
        elif effort_norm == 'medium':
            selected_tier_key = 'tier_2_architect_sync'
        else:
            selected_tier_key = 'tier_3_lore_judge'
        selected_tier = tiers[selected_tier_key]

    primary_models = selected_tier.get('primary_ide_models', ['gemini-4-argon'])
    primary_model_id = primary_models[0]
    secondary_ide_model_id = primary_models[1] if len(primary_models) > 1 else primary_models[0]

    ide_models = registry.get('ide_models', {})
    model_meta = ide_models.get(primary_model_id, {})
    effort_cfg = model_meta.get('effort_stages', {}).get(effort_norm, {
        'thinking_budget': 4096,
        'reasoning_effort': effort_norm,
        'payload_adapter': {'reasoning_effort': effort_norm},
    })

    proc_map = scan_windows_processes()
    desktop_cfg = registry.get('desktop_clients', {})
    tier_desktop_clients = []
    for dcid in selected_tier.get('desktop_clients', []):
        dinfo = desktop_cfg.get(dcid, {})
        exe = dinfo.get('executable', '')
        is_running = len(proc_map.get(exe.lower(), [])) > 0
        tier_desktop_clients.append({
            'client_id': dcid,
            'executable': exe,
            'display_name': dinfo.get('display_name'),
            'running': is_running,
        })

    proxy_status = check_local_proxy_status(MultiModelAPIClient(registry))
    allowed_efforts = selected_tier.get('allowed_efforts', ['low', 'medium', 'high'])

    return {
        'timestamp': datetime.datetime.now().isoformat(),
        'requested_task_type': task_type,
        'requested_effort': effort_norm,
        'resolved_tier_key': selected_tier_key,
        'resolved_tier_id': selected_tier.get('id'),
        'resolved_tier_name': selected_tier.get('name'),
        'tier_default_effort': selected_tier.get('default_effort', 'medium'),
        'effort_in_tier_allowed_range': effort_norm in allowed_efforts,
        'primary_ide_model': {
            'model_id': primary_model_id,
            'display_name': model_meta.get('display_name', primary_model_id),
            'vendor': model_meta.get('vendor', 'Unknown'),
            'subagent_type': selected_tier.get('subagent_types', ['inherit'])[0],
            'normalized_effort': effort_cfg,
        },
        'secondary_ide_model': secondary_ide_model_id,
        'twin_proxy_fallbacks': selected_tier.get('twin_proxy_models', []),
        'local_proxy_5005': {
            'status': proxy_status['status'],
            'live_reachable': proxy_status['live_reachable'],
            'configured_upstreams_count': proxy_status['configured_upstreams_count'],
        },
        'desktop_client_fallbacks': tier_desktop_clients,
        'failover_policy': {
            'on_429_rate_limit': f"Shift immediately to twin model '{selected_tier.get('twin_proxy_models', ['z-ai/glm-5.3'])[0]}' via Proxy :5005",
            'on_5xx_transient': 'Exponential backoff (1s, 2s, 4s) then horizontal failover to secondary IDE model or Desktop Client',
        },
    }


def execute_stage_with_fallback(stage_def: dict, tier_info: dict, registry: dict, limit: int) -> dict:
    """Executes a single pipeline stage with timing, retry/fallback telemetry, and output capture."""
    stage_id = stage_def['stage_id']
    stage_name = stage_def['name']
    script_rel = stage_def['script']
    script_path = ROOT / script_rel
    effort = stage_def.get('effort', tier_info.get('default_effort', 'medium'))
    extra_args = list(stage_def.get('args', []))

    # Pass --batch-size based on --limit where applicable
    if stage_id == 'stage_3a':
        extra_args.extend(['--batch-size', str(max(1, limit))])
    elif stage_id == 'stage_3b':
        extra_args.extend(['--batch-size', str(max(1, min(limit, 3)))])

    primary_model = tier_info.get('primary_ide_models', ['gemini-4-argon'])[0]
    twin_models = tier_info.get('twin_proxy_models', ['z-ai/glm-5.3'])
    desktop_exes = tier_info.get('desktop_executables', [])

    ide_meta = registry.get('ide_models', {}).get(primary_model, {})
    effort_adapter = ide_meta.get('effort_stages', {}).get(effort, {})

    print(f"\n----------------------------------------------------------------------")
    print(f"[{stage_id.upper()}] {stage_name}")
    print(f"  Tier: {tier_info.get('name')} | Model: {primary_model} (Effort: {effort.upper()})")
    print(f"  Twin Fallback (:5005): {', '.join(twin_models)} | Desktop: {', '.join(desktop_exes)}")
    print(f"----------------------------------------------------------------------")

    start_mono = time.monotonic()
    started_at = datetime.datetime.now().isoformat()

    attempts = 0
    max_attempts = 2
    active_model_used = primary_model
    fallback_triggered = False
    exit_code = 1
    stdout_text = ''
    stderr_text = ''

    cmd = [sys.executable, str(script_path)] + extra_args
    env = os.environ.copy()
    env['SVARTULFR_ACTIVE_TIER'] = tier_info.get('id', '')
    env['SVARTULFR_ACTIVE_MODEL'] = primary_model
    env['SVARTULFR_EFFORT_STAGE'] = effort

    while attempts < max_attempts:
        attempts += 1
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(ROOT),
                env=env,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                timeout=180,
            )
            exit_code = proc.returncode
            stdout_text = (proc.stdout or '').strip()
            stderr_text = (proc.stderr or '').strip()
            if exit_code == 0:
                break
            # If non-zero on attempt 1, trigger horizontal fallback to twin model
            if attempts < max_attempts:
                fallback_triggered = True
                active_model_used = twin_models[0] if twin_models else primary_model
                env['SVARTULFR_ACTIVE_MODEL'] = active_model_used
                print(
                    f"  [WARN] Stage {stage_id} exited with code {exit_code} on attempt {attempts}. "
                    f"Failing over to Twin Model '{active_model_used}'...",
                    file=sys.stderr,
                )
                time.sleep(1.0)
        except subprocess.TimeoutExpired as e:
            exit_code = 124
            stderr_text = f'TimeoutExpired after 180s: {e}'
            if attempts < max_attempts:
                fallback_triggered = True
                active_model_used = twin_models[0] if twin_models else primary_model
                env['SVARTULFR_ACTIVE_MODEL'] = active_model_used
        except Exception as e:
            exit_code = 1
            stderr_text = str(e)
            break

    elapsed_s = round(time.monotonic() - start_mono, 3)
    combined_output = stdout_text
    if stderr_text:
        combined_output = (combined_output + '\n[STDERR]: ' + stderr_text).strip()

    # Print concise summary lines to stdout (< 25 lines per stage)
    lines = [ln for ln in combined_output.splitlines() if ln.strip()]
    preview_lines = lines[-12:] if len(lines) > 12 else lines
    for ln in preview_lines:
        print(f"  {ln}")

    status_str = 'SUCCESS' if exit_code == 0 else 'FAILED'
    print(f"  -> [{status_str}] Completed in {elapsed_s:.2f}s (Model: {active_model_used})")

    return {
        'stage_id': stage_id,
        'name': stage_name,
        'tier_id': tier_info.get('id'),
        'tier_name': tier_info.get('name'),
        'script': script_rel,
        'args': extra_args,
        'primary_model': primary_model,
        'active_model_used': active_model_used,
        'fallback_triggered': fallback_triggered,
        'twin_models': twin_models,
        'desktop_executables': desktop_exes,
        'effort_stage': effort,
        'thinking_budget': effort_adapter.get('thinking_budget', 4096),
        'subagent_type': tier_info.get('subagent_types', ['inherit'])[0],
        'started_at': started_at,
        'elapsed_seconds': elapsed_s,
        'attempts': attempts,
        'exit_code': exit_code,
        'status': status_str,
        'output_line_count': len(lines),
        'output_tail': '\n'.join(lines[-25:]),
        'full_output': combined_output,
    }


def write_unified_markdown_reports(run_data: dict) -> dict:
    """Writes unified markdown report to scratch/daily_maintenance_report.md and logs/automations/."""
    SCRATCH.mkdir(parents=True, exist_ok=True)
    LOGS_AUTO_DIR.mkdir(parents=True, exist_ok=True)

    ts_human = run_data.get('timestamp', datetime.datetime.now().isoformat())
    summary = run_data.get('summary', {})
    clients_info = run_data.get('omen_clients_snapshot', {})
    stages = run_data.get('stages', [])

    md = []
    md.append('# Svartúlfr Verse — Unified Master Pipeline Report (Multi-Model Team)\n')
    md.append(f"- **Execution Timestamp:** `{ts_human}`")
    md.append(f"- **Pipeline Status:** **{'✅ ALL GREEN' if summary.get('failed_stages', 0) == 0 else '⚠️ PARTIAL WARNING'}**")
    md.append(f"- **Stages Executed:** `{summary.get('total_stages', 0)}` (`{summary.get('succeeded_stages', 0)}` succeeded, `{summary.get('failed_stages', 0)}` failed)")
    md.append(f"- **Total Duration:** `{summary.get('total_elapsed_seconds', 0):.2f}s`")
    md.append(f"- **Batch Limit (`--limit`):** `{run_data.get('limit', 5)}`")
    md.append(f"- **Dashboard HTML:** `scratch/unified_pipeline_dashboard.html`\n")

    md.append('## 1. PC OMEN Desktop AI Clients & Local Proxy (`:5005`) Status\n')
    md.append('| Client / Gateway | Executable / Endpoint | Assigned Tier | Status | Details |')
    md.append('| :--- | :--- | :--- | :---: | :--- |')
    for dc in clients_info.get('desktop_clients', []):
        st_badge = '🟢 RUNNING' if dc.get('running') else ('🔵 INSTALLED' if dc.get('installed_on_disk') else '⚪ STANDBY')
        pids_str = f"PIDs: {', '.join(str(p) for p in dc.get('pids', [])[:4])}" if dc.get('pids') else f"v{dc.get('version_hint', 'N/A')}"
        md.append(f"| **{dc.get('display_name')}** | `{dc.get('executable')}` | `{dc.get('assigned_tier')}` | {st_badge} | {pids_str} |")

    proxy_info = clients_info.get('local_proxy_5005', {})
    p_badge = '🟢 ONLINE' if proxy_info.get('live_reachable') else '🔵 CONFIGURED'
    md.append(
        f"| **Local AI Proxy Rotator** | `{proxy_info.get('endpoint')}` | `All Tiers (:5005)` | {p_badge} | "
        f"`{proxy_info.get('configured_upstreams_count', 0)}` active upstreams |"
    )
    md.append('\n')

    md.append('## 2. Multi-Model 3-Tier Execution Matrix\n')
    md.append('| Stage | Tier | Primary Model | Effort Stage | Twin Fallback (`:5005`) | Duration | Status |')
    md.append('| :--- | :--- | :--- | :---: | :--- | :---: | :---: |')
    for st in stages:
        icon = '✅ PASS' if st['exit_code'] == 0 else f"❌ FAIL ({st['exit_code']})"
        md.append(
            f"| **{st['name']}** | `{st['tier_id']}` | `{st['active_model_used']}` | "
            f"`{st['effort_stage'].upper()}` ({st['thinking_budget']} tok) | `{', '.join(st['twin_models'][:2])}` | "
            f"`{st['elapsed_seconds']:.2f}s` | {icon} |"
        )
    md.append('\n')

    md.append('## 3. Detailed Stage Logs\n')
    for st in stages:
        icon = '✅ SUCCESS' if st['exit_code'] == 0 else f"❌ FAILED (Code {st['exit_code']})"
        md.append(f"### {st['name']} — {icon} ({st['elapsed_seconds']:.2f}s)\n")
        md.append(f"- **Tier:** {st['tier_name']} (`{st['tier_id']}`)")
        md.append(f"- **Model Used:** `{st['active_model_used']}` | **Subagent:** `{st['subagent_type']}` | **Effort:** `{st['effort_stage']}`")
        md.append(f"- **Command:** `python {st['script']} {' '.join(st['args'])}`\n")
        md.append(f"```text\n{st['output_tail']}\n```\n")

    report_text = '\n'.join(md)
    with open(DEFAULT_REPORT_MD, 'w', encoding='utf-8') as f:
        f.write(report_text)

    ts_slug = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    archive_md_path = LOGS_AUTO_DIR / f'{ts_slug}_daily_master_pipeline_report.md'
    with open(archive_md_path, 'w', encoding='utf-8') as f:
        f.write(report_text)

    return {
        'scratch_report': str(DEFAULT_REPORT_MD.relative_to(ROOT).as_posix()),
        'archive_report': str(archive_md_path.relative_to(ROOT).as_posix()),
    }


def generate_dashboard_html(registry: dict, run_data: dict = None, clients_data: dict = None, html_path: pathlib.Path = DEFAULT_DASHBOARD_HTML) -> pathlib.Path:
    """Generates an interactive self-contained HTML Telemetry Dashboard."""
    if clients_data is None:
        if DEFAULT_CLIENTS_JSON.exists():
            try:
                with open(DEFAULT_CLIENTS_JSON, 'r', encoding='utf-8') as f:
                    clients_data = json.load(f)
            except Exception:
                clients_data = detect_clients(registry, limit=20)
        else:
            clients_data = detect_clients(registry, limit=20)

    if run_data is None and DEFAULT_RUN_JSON.exists():
        try:
            with open(DEFAULT_RUN_JSON, 'r', encoding='utf-8') as f:
                run_data = json.load(f)
        except Exception:
            run_data = None

    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    summary = (run_data or {}).get('summary', {
        'total_stages': 6,
        'succeeded_stages': 6,
        'failed_stages': 0,
        'total_elapsed_seconds': 0.0,
        'overall_status': 'READY',
    })
    stages = (run_data or {}).get('stages', [])
    desktop_clients = clients_data.get('desktop_clients', [])
    proxy_info = clients_data.get('local_proxy_5005', {})
    ide_models = registry.get('ide_models', {})
    tiers = registry.get('tiers', {})
    ext_providers = clients_data.get('external_providers', [])

    # Build Desktop Client Cards HTML
    client_cards_html = []
    for dc in desktop_clients:
        is_run = dc.get('running', False)
        status_cls = 'badge-online' if is_run else ('badge-ready' if dc.get('installed_on_disk') else 'badge-standby')
        status_lbl = 'RUNNING LIVE' if is_run else ('INSTALLED READY' if dc.get('installed_on_disk') else 'STANDBY')
        pids_txt = ', '.join(str(p) for p in dc.get('pids', [])[:5]) if dc.get('pids') else 'No active PID'
        scope_row = (
            f"<div class=\"kv-row\"><span>Exclusive Scope:</span><strong>{html.escape(str(dc.get('exclusive_scope')))}</strong></div>"
            if dc.get('exclusive_scope')
            else ''
        )
        client_cards_html.append(f"""
        <div class="card client-card" data-client-id="{html.escape(str(dc.get('id')))}">
          <div class="card-header">
            <span class="client-title">{html.escape(str(dc.get('display_name')))}</span>
            <span class="badge {status_cls}">{status_lbl}</span>
          </div>
          <div class="card-body">
            <div class="kv-row"><span>Executable:</span><code>{html.escape(str(dc.get('executable')))}</code></div>
            <div class="kv-row"><span>Assigned Role/Tier:</span><code>{html.escape(str(dc.get('assigned_tier')))}</code></div>
            {scope_row}
            <div class="kv-row"><span>Processes ({dc.get('process_count', 0)}):</span><span>{html.escape(pids_txt)}</span></div>
            <div class="kv-row"><span>Version / CDP:</span><code>v{html.escape(str(dc.get('version_hint')))} | {html.escape(str(dc.get('cdp_arg')))}</code></div>
          </div>
        </div>
        """)

    # Add Local Proxy :5005 Card
    p_online = proxy_info.get('live_reachable', False)
    p_cls = 'badge-online' if p_online else 'badge-ready'
    p_lbl = 'ONLINE (:5005)' if p_online else f"CONFIGURED ({proxy_info.get('configured_upstreams_count', 0)} UPSTREAMS)"
    client_cards_html.append(f"""
    <div class="card client-card" data-client-id="local_proxy_5005">
      <div class="card-header">
        <span class="client-title">Local AI Proxy Rotator (:5005)</span>
        <span class="badge {p_cls}">{p_lbl}</span>
      </div>
      <div class="card-body">
        <div class="kv-row"><span>Endpoint:</span><code>http://127.0.0.1:5005/v1/chat/completions</code></div>
        <div class="kv-row"><span>Active Upstreams:</span><strong>{proxy_info.get('configured_upstreams_count', 0)} RPG Curated Models</strong></div>
        <div class="kv-row"><span>Fiat Pillars:</span><span>GLM 5.3, Gemini 4 Argon, Gemini 3.8, Gemma 4</span></div>
        <div class="kv-row"><span>Failover Cooldown:</span><code>40s Circuit Breaker + SSE</code></div>
      </div>
    </div>
    """)

    # Build 3-Tier Matrix Rows
    tier_rows_html = []
    for tkey, tinfo in tiers.items():
        prim = ', '.join(tinfo.get('primary_ide_models', []))
        twins = ', '.join(tinfo.get('twin_proxy_models', []))
        desks = ', '.join(tinfo.get('desktop_executables', []))
        efforts = ' / '.join(e.upper() for e in tinfo.get('allowed_efforts', []))
        subagents = ', '.join(tinfo.get('subagent_types', []))
        stage_names = '<br>'.join(html.escape(s.get('name', '')) for s in tinfo.get('assigned_stages', []))
        tier_rows_html.append(f"""
        <tr data-tier="{html.escape(tkey)}">
          <td><strong>{html.escape(tinfo.get('name', ''))}</strong><br><small class="muted">{html.escape(tinfo.get('id', ''))}</small></td>
          <td>{html.escape(tinfo.get('role', ''))}</td>
          <td><code>{html.escape(prim)}</code><br><small>Subagent: <code>{html.escape(subagents)}</code></small></td>
          <td><span class="badge badge-effort-{html.escape(tinfo.get('default_effort', 'medium'))}">{html.escape(efforts)}</span></td>
          <td><code>{html.escape(twins)}</code></td>
          <td><code>{html.escape(desks)}</code></td>
          <td>{stage_names}</td>
        </tr>
        """)

    # Build IDE Models & Effort Normalization Table
    ide_rows_html = []
    for mid, minfo in ide_models.items():
        es = minfo.get('effort_stages', {})
        low_b = es.get('low', {}).get('thinking_budget', 0)
        med_b = es.get('medium', {}).get('thinking_budget', 0)
        high_b = es.get('high', {}).get('thinking_budget', 0)
        adapter_sample = json.dumps(es.get('high', {}).get('payload_adapter', {}))
        ide_rows_html.append(f"""
        <tr>
          <td><strong>{html.escape(minfo.get('display_name', mid))}</strong> (<code>{html.escape(mid)}</code>)</td>
          <td>{html.escape(minfo.get('vendor', ''))}</td>
          <td><code>{minfo.get('context_window', 0):,}</code> tok</td>
          <td><code>{html.escape(minfo.get('subagent_mapping', ''))}</code></td>
          <td><code>{low_b:,}</code> tok</td>
          <td><code>{med_b:,}</code> tok</td>
          <td><code>{high_b:,}</code> tok</td>
          <td><code>{html.escape(adapter_sample)}</code></td>
        </tr>
        """)

    # Build Open-Provider Plug & Play Rows
    ext_rows_html = []
    for ep in ext_providers:
        pid = ep.get('provider_id', '')
        auth_env = ep.get('auth_env') or 'None (Local)'
        env_ok = ep.get('env_configured', False)
        auth_cls = 'badge-online' if env_ok else 'badge-standby'
        auth_lbl = 'CONFIGURED' if env_ok else f'OPTIONAL ({auth_env})'
        models_str = ', '.join(ep.get('featured_models', []))
        ext_rows_html.append(f"""
        <tr data-provider-id="{html.escape(str(pid))}">
          <td><strong>{html.escape(str(ep.get('display_name', pid)))}</strong> (<code>{html.escape(str(pid))}</code>)</td>
          <td><code>{html.escape(str(ep.get('endpoint', '')))}</code></td>
          <td><code>{html.escape(str(ep.get('protocol', 'openai_compatible')))}</code></td>
          <td><span class="badge {auth_cls}">{html.escape(auth_lbl)}</span></td>
          <td><code>{html.escape(models_str)}</code></td>
        </tr>
        """)

    # Build Stage Execution Telemetry Cards
    stage_cards_html = []
    for st in stages:
        ok = st.get('exit_code', 1) == 0
        st_cls = 'badge-online' if ok else 'badge-error'
        st_txt = 'SUCCESS' if ok else f"FAILED ({st.get('exit_code')})"
        stage_cards_html.append(f"""
        <div class="card stage-card" data-stage-id="{html.escape(st.get('stage_id', ''))}" data-tier-id="{html.escape(st.get('tier_id', ''))}">
          <div class="card-header">
            <div>
              <span class="stage-title">{html.escape(st.get('name', ''))}</span>
              <div class="stage-meta">
                Tier: <code>{html.escape(st.get('tier_id', ''))}</code> |
                Model: <code>{html.escape(st.get('active_model_used', ''))}</code> |
                Effort: <span class="badge badge-effort-{html.escape(st.get('effort_stage', 'medium'))}">{html.escape(st.get('effort_stage', '').upper())} ({st.get('thinking_budget', 0)} tok)</span> |
                Duration: <strong>{st.get('elapsed_seconds', 0):.2f}s</strong>
              </div>
            </div>
            <span class="badge {st_cls}">{st_txt}</span>
          </div>
          <pre class="stage-log">{html.escape(st.get('output_tail', 'No output recorded.'))}</pre>
        </div>
        """)

    if not stage_cards_html:
        stage_cards_html.append('<div class="card"><p>No pipeline stages have been executed yet in this session.</p></div>')

    overall_ok = summary.get('failed_stages', 0) == 0
    overall_badge_cls = 'badge-online' if overall_ok else 'badge-error'

    embedded_telemetry = json.dumps({
        'generated_at': now_str,
        'summary': summary,
        'desktop_clients_count': len(desktop_clients),
        'external_providers_count': len(ext_providers),
        'stages_count': len(stages),
    })

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐺</text></svg>" />
  <title>Svartúlfr Verse — Unified Master Pipeline & Multi-Model Telemetry Dashboard</title>
  <style>
    :root {{
      --bg: #0b0f19;
      --panel: #131b2e;
      --panel-alt: #19233c;
      --border: #2a395c;
      --text: #e2e8f0;
      --muted: #94a3b8;
      --accent: #38bdf8;
      --green: #22c55e;
      --amber: #f59e0b;
      --red: #ef4444;
      --purple: #a855f7;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 24px;
    }}
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      padding: 20px 24px;
      background: linear-gradient(135deg, #131b2e 0%, #1e1b4b 100%);
      border: 1px solid var(--border);
      border-radius: 12px;
      margin-bottom: 24px;
    }}
    h1 {{ font-size: 1.5rem; color: #f8fafc; }}
    h2 {{ font-size: 1.2rem; color: var(--accent); margin: 24px 0 12px; }}
    .subtitle {{ color: var(--muted); font-size: 0.9rem; }}
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    .kpi-box {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
    }}
    .kpi-label {{ color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }}
    .kpi-value {{ font-size: 1.65rem; font-weight: 700; margin-top: 4px; color: #fff; }}
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 16px;
    }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
      margin-bottom: 12px;
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(255,255,255,0.07);
    }}
    .client-title, .stage-title {{ font-weight: 600; font-size: 1.02rem; color: #f8fafc; }}
    .stage-meta {{ font-size: 0.83rem; color: var(--muted); margin-top: 4px; }}
    .kv-row {{
      display: flex;
      justify-content: space-between;
      font-size: 0.86rem;
      padding: 4px 0;
      color: var(--muted);
    }}
    .kv-row code, .kv-row strong, .kv-row span:last-child {{ color: var(--text); }}
    code {{
      background: rgba(15, 23, 42, 0.75);
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'Cascadia Code', Consolas, monospace;
      font-size: 0.82rem;
      color: #7dd3fc;
    }}
    .badge {{
      display: inline-block;
      padding: 3px 9px;
      border-radius: 999px;
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 0.03em;
    }}
    .badge-online {{ background: rgba(34, 197, 94, 0.18); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.4); }}
    .badge-ready {{ background: rgba(56, 189, 248, 0.18); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }}
    .badge-standby {{ background: rgba(148, 163, 184, 0.15); color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.3); }}
    .badge-error {{ background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }}
    .badge-effort-low {{ background: rgba(34, 197, 94, 0.15); color: #86efac; }}
    .badge-effort-medium {{ background: rgba(245, 158, 11, 0.18); color: #fcd34d; }}
    .badge-effort-high {{ background: rgba(168, 85, 247, 0.22); color: #d8b4fe; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      font-size: 0.88rem;
      margin-bottom: 20px;
    }}
    th, td {{
      padding: 11px 14px;
      text-align: left;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }}
    th {{ background: var(--panel-alt); color: #cbd5e1; font-weight: 600; }}
    .stage-log {{
      background: #070a12;
      color: #cbd5e1;
      padding: 12px;
      border-radius: 8px;
      font-family: 'Cascadia Code', Consolas, monospace;
      font-size: 0.8rem;
      overflow-x: auto;
      white-space: pre-wrap;
      border: 1px solid #1e293b;
    }}
    .filter-bar {{
      display: flex;
      gap: 10px;
      margin-bottom: 14px;
      flex-wrap: wrap;
    }}
    .btn {{
      background: var(--panel-alt);
      color: var(--text);
      border: 1px solid var(--border);
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.84rem;
    }}
    .btn.active, .btn:hover {{
      background: var(--accent);
      color: #0f172a;
      border-color: var(--accent);
      font-weight: 600;
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Svartúlfr Verse — Unified Master Pipeline & Multi-Model Team</h1>
      <div class="subtitle">Single Scheduled Sidecar: <code>daily-master-pipeline</code> (09:00 Europe/Rome) • Host: <code>{html.escape(str(clients_data.get('host', 'PC-OMEN')))}</code></div>
    </div>
    <div>
      <span class="badge {overall_badge_cls}" id="overall-status-badge">PIPELINE {html.escape(str(summary.get('overall_status', 'ALL_GREEN')))}</span>
      <div class="subtitle" style="margin-top:4px; text-align:right;">Updated: {html.escape(now_str)}</div>
    </div>
  </header>

  <section class="kpi-grid" id="kpi-metrics">
    <div class="kpi-box">
      <div class="kpi-label">Unified Pipeline Stages</div>
      <div class="kpi-value">{summary.get('succeeded_stages', 0)} / {summary.get('total_stages', 0)} PASS</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">PC OMEN AI Clients</div>
      <div class="kpi-value">{clients_data.get('summary', {}).get('desktop_clients_running', 0)} Running / {len(desktop_clients)} Reg</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">Local Proxy (:5005) Pool</div>
      <div class="kpi-value">{proxy_info.get('configured_upstreams_count', 0)} Upstreams</div>
    </div>
    <div class="kpi-box">
      <div class="kpi-label">Total Execution Time</div>
      <div class="kpi-value">{summary.get('total_elapsed_seconds', 0.0):.2f}s</div>
    </div>
  </section>

  <h2>1. PC OMEN Desktop AI Clients & Local Proxy (:5005) Fleet</h2>
  <div class="cards-grid" id="omen-clients-grid">
    {''.join(client_cards_html)}
  </div>

  <h2>2. 3-Tier Multi-Model Matrix & Open-Provider Routing</h2>
  <table id="tier-matrix-table">
    <thead>
      <tr>
        <th>Tier</th>
        <th>Operational Role</th>
        <th>Primary IDE Model & Subagent</th>
        <th>Effort Stage</th>
        <th>Twin / Proxy :5005 Fallback</th>
        <th>PC OMEN Desktop Client</th>
        <th>Assigned Pipeline Stages</th>
      </tr>
    </thead>
    <tbody>
      {''.join(tier_rows_html)}
    </tbody>
  </table>

  <h2>3. Normalized Effort Stage Adapter (Low / Medium / High)</h2>
  <table id="effort-adapter-table">
    <thead>
      <tr>
        <th>IDE Model</th>
        <th>Vendor</th>
        <th>Context Window</th>
        <th>Subagent Type</th>
        <th>Low Budget</th>
        <th>Medium Budget</th>
        <th>High Budget</th>
        <th>High Effort Payload Adapter</th>
      </tr>
    </thead>
    <tbody>
      {''.join(ide_rows_html)}
    </tbody>
  </table>

  <h2>4. Open-Provider Plug &amp; Play Registry</h2>
  <table id="open-providers-table">
    <thead>
      <tr>
        <th>Provider Gateway</th>
        <th>Endpoint URL</th>
        <th>Protocol</th>
        <th>Credentials / Auth Status</th>
        <th>Featured Models</th>
      </tr>
    </thead>
    <tbody>
      {''.join(ext_rows_html)}
    </tbody>
  </table>

  <h2>5. Unified 5-Stage Pipeline Execution Telemetry</h2>
  <div class="filter-bar">
    <button class="btn active" onclick="filterStages('all', this)">All Stages ({len(stages)})</button>
    <button class="btn" onclick="filterStages('scout-fast', this)">Tier 1: Scout & Fast</button>
    <button class="btn" onclick="filterStages('architect-sync', this)">Tier 2: Architect & Sync</button>
    <button class="btn" onclick="filterStages('lore-judge', this)">Tier 3: Deep Lore Judge</button>
  </div>
  <div id="stages-container">
    {''.join(stage_cards_html)}
  </div>

  <script id="telemetry-data" type="application/json">{embedded_telemetry}</script>
  <script>
    function filterStages(tierId, btnEl) {{
      document.querySelectorAll('.filter-bar .btn').forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      document.querySelectorAll('.stage-card').forEach(card => {{
        if (tierId === 'all' || card.getAttribute('data-tier-id') === tierId) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>
"""
    html_path.parent.mkdir(parents=True, exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    if html_path.resolve() != DEFAULT_DASHBOARD_HTML.resolve():
        DEFAULT_DASHBOARD_HTML.parent.mkdir(parents=True, exist_ok=True)
        with open(DEFAULT_DASHBOARD_HTML, 'w', encoding='utf-8') as f:
            f.write(html_doc)
    return html_path


def run_pipeline(registry: dict, limit: int, target_tier: int = None) -> dict:
    """Runs either all tiers (run-all) or a specific tier (run-tier) and produces full telemetry."""
    pipeline_start = time.monotonic()
    started_iso = datetime.datetime.now().isoformat()

    print("======================================================================")
    print(f"SVARTULFR VERSE — MULTI-MODEL UNIFIED MASTER PIPELINE (limit={limit})")
    print("======================================================================")

    # Always snapshot PC OMEN clients + Proxy :5005
    clients_snapshot = detect_clients(registry, limit=max(10, limit))
    print(
        f"[PC OMEN AI Fleet] {clients_snapshot['summary']['desktop_clients_running']}/"
        f"{clients_snapshot['summary']['desktop_clients_registered']} Desktop Clients Running | "
        f"Proxy :5005: {clients_snapshot['summary']['local_proxy_5005_status']} "
        f"({clients_snapshot['summary']['local_proxy_upstreams']} upstreams)"
    )

    tiers = registry.get('tiers', {})
    ordered_tiers = [
        ('tier_1_scout_fast', tiers['tier_1_scout_fast']),
        ('tier_2_architect_sync', tiers['tier_2_architect_sync']),
        ('tier_3_lore_judge', tiers['tier_3_lore_judge']),
    ]

    stage_results = []
    for tkey, tinfo in ordered_tiers:
        tnum = tinfo.get('tier_number')
        if target_tier is not None and tnum != target_tier:
            continue
        for stage_def in tinfo.get('assigned_stages', []):
            res = execute_stage_with_fallback(stage_def, tinfo, registry, limit=limit)
            stage_results.append(res)

    total_elapsed = round(time.monotonic() - pipeline_start, 3)
    succeeded = sum(1 for s in stage_results if s['exit_code'] == 0)
    failed = len(stage_results) - succeeded

    run_data = {
        'timestamp': started_iso,
        'completed_at': datetime.datetime.now().isoformat(),
        'mode': f'tier_{target_tier}' if target_tier else 'run_all',
        'limit': limit,
        'summary': {
            'total_stages': len(stage_results),
            'succeeded_stages': succeeded,
            'failed_stages': failed,
            'total_elapsed_seconds': total_elapsed,
            'overall_status': 'ALL_GREEN' if failed == 0 else 'WARNING_PARTIAL_FAIL',
        },
        'omen_clients_snapshot': clients_snapshot,
        'stages': stage_results,
    }

    # Stage 4: Telemetry Dashboard & Unified Markdown Report
    if target_tier is None:
        dash_path = generate_dashboard_html(registry, run_data=run_data, clients_data=clients_snapshot)
        reports_info = write_unified_markdown_reports(run_data)
        run_data['artifacts'] = {
            'dashboard_html': str(dash_path.relative_to(ROOT).as_posix()),
            'scratch_report_md': reports_info['scratch_report'],
            'archive_report_md': reports_info['archive_report'],
        }
        SCRATCH.mkdir(parents=True, exist_ok=True)
        with open(DEFAULT_RUN_JSON, 'w', encoding='utf-8') as f:
            json.dump(run_data, f, indent=2, ensure_ascii=False)
    else:
        dash_path = DEFAULT_DASHBOARD_HTML
        run_data['artifacts'] = {
            'dashboard_html': str(dash_path.relative_to(ROOT).as_posix()),
        }

    print("\n======================================================================")
    print(f"MASTER PIPELINE COMPLETED: {succeeded}/{len(stage_results)} stages succeeded in {total_elapsed:.2f}s")
    print(f"Dashboard HTML: {dash_path}")
    print(f"Unified Report: {DEFAULT_REPORT_MD}")
    print("======================================================================")
    return run_data


def main():
    parser = argparse.ArgumentParser(
        description='Svartulfr Verse Multi-Model Unified Pipeline Orchestrator CLI'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # 1. detect-clients
    p_detect = subparsers.add_parser(
        'detect-clients',
        help='Scan running Windows processes on PC OMEN for Desktop AI clients, Proxy :5005 health, and IDE models',
    )
    p_detect.add_argument('--limit', type=int, required=True, help='Maximum number of items per category to return')
    p_detect.add_argument('--output', required=True, help='Output JSON file path')

    # 2. route-model
    p_route = subparsers.add_parser(
        'route-model',
        help='Resolve optimal Tier, primary IDE model, normalized reasoning effort payload, and fallbacks',
    )
    p_route.add_argument('--task-type', required=True, help='Task type identifier (e.g., health_check, omnisync_audit, lore_synthesis)')
    p_route.add_argument('--effort', required=True, choices=['low', 'medium', 'high'], help='Normalized reasoning effort stage')
    p_route.add_argument('--output', required=True, help='Output JSON file path')

    # 3. run-tier
    p_tier = subparsers.add_parser(
        'run-tier',
        help='Execute only the pipeline stages belonging to Tier 1, 2, or 3',
    )
    p_tier.add_argument('--tier', type=int, required=True, choices=[1, 2, 3], help='Tier number (1, 2, or 3)')
    p_tier.add_argument('--limit', type=int, required=True, help='Batch limit for iterative stages')
    p_tier.add_argument('--output', required=True, help='Output JSON file path')

    # 4. run-all
    p_all = subparsers.add_parser(
        'run-all',
        help='Execute the complete unified 5-stage master pipeline across all 3 Tiers',
    )
    p_all.add_argument('--limit', type=int, required=True, help='Batch limit for character enrichment and archive mining stages')
    p_all.add_argument('--output', required=True, help='Output JSON file path')

    # 5. dashboard
    p_dash = subparsers.add_parser(
        'dashboard',
        help='Generate the interactive self-contained HTML Telemetry Dashboard',
    )
    p_dash.add_argument('--output', required=True, help='Output file path (.html or .json)')

    args = parser.parse_args()
    registry = load_registry()

    if args.command == 'detect-clients':
        data = detect_clients(registry, limit=args.limit)
        write_output(data, args.output)
    elif args.command == 'route-model':
        data = route_model(registry, task_type=args.task_type, effort=args.effort)
        write_output(data, args.output)
    elif args.command == 'run-tier':
        data = run_pipeline(registry, limit=args.limit, target_tier=args.tier)
        write_output(data, args.output)
    elif args.command == 'run-all':
        data = run_pipeline(registry, limit=args.limit, target_tier=None)
        write_output(data, args.output)
    elif args.command == 'dashboard':
        out_p = pathlib.Path(args.output)
        if not out_p.is_absolute():
            out_p = ROOT / out_p
        if out_p.suffix.lower() == '.html':
            dash_file = generate_dashboard_html(registry, html_path=out_p)
            print(f'Success! Dashboard HTML written to: {dash_file}')
        else:
            dash_file = generate_dashboard_html(registry, html_path=DEFAULT_DASHBOARD_HTML)
            write_output(
                {
                    'status': 'success',
                    'dashboard_html': str(dash_file),
                    'generated_at': datetime.datetime.now().isoformat(),
                },
                args.output,
            )
    else:
        print(f'Unknown command: {args.command}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
