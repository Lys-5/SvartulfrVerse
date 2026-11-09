import http.server
import json
import os
import pathlib
import socketserver
import sys
import tempfile
import threading
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_SCRIPTS = ROOT / '.agents' / 'skills' / 'multi-model-unified-pipeline' / 'scripts'
if str(SKILL_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SKILL_SCRIPTS))

import orchestrator


def test_registry_and_sidecar_consolidation():
    reg = orchestrator.load_registry()
    tiers = reg.get('tiers', {})
    assert set(tiers.keys()) == {'tier_1_scout_fast', 'tier_2_architect_sync', 'tier_3_lore_judge'}

    ide_models = reg.get('ide_models', {})
    assert set(ide_models.keys()) == {
        'gemini-4-argon',
        'gemini-3.8-flash',
        'claude-opus-5.5',
        'claude-sonnet-5.5',
        'gpt-oss-120b',
    }
    for mid, mdata in ide_models.items():
        assert set(mdata['effort_stages'].keys()) == {'low', 'medium', 'high'}

    desktop = reg.get('desktop_clients', {})
    assert set(desktop.keys()) == {
        'antigravity',
        'gemini_desktop',
        'grok_bot',
        'claude_desktop',
        'copilot_desktop',
    }

    ext = reg.get('external_providers_plug_and_play', {})
    assert set(ext.keys()) == {
        'local_proxy',
        'xai_grok',
        'openrouter',
        'ollama_local',
        'lm_studio_local',
    }

    sidecars_dir = pathlib.Path(os.path.expanduser('~/.gemini/config/sidecars'))
    master_sidecar = sidecars_dir / 'daily-master-pipeline' / 'sidecar.json'
    assert master_sidecar.exists(), 'daily-master-pipeline/sidecar.json must exist'
    sc_data = json.loads(master_sidecar.read_text(encoding='utf-8'))
    assert sc_data['builtin'] == 'schedule'
    assert sc_data['restart_policy'] == 'always'
    assert sc_data['args'][0] == 'CRON_TZ=Europe/Rome 0 9 * * *'
    assert sc_data['args'][3] == '--'

    legacy_names = [
        'daily-character-enrichment',
        'daily-wyvern-monitor',
        'daily-proxy-free-models',
        'daily-omnisync-archive-mining',
    ]
    for name in legacy_names:
        assert not (sidecars_dir / name).exists(), f'Legacy sidecar {name} should be removed from active sidecars'
        assert (ROOT / 'ARCHIVIO' / 'sidecars_legacy_backup' / name / 'sidecar.json').exists()


def test_detect_clients_and_route_model():
    reg = orchestrator.load_registry()
    clients = orchestrator.detect_clients(reg, limit=20)
    assert clients['summary']['desktop_clients_registered'] == 5
    assert clients['summary']['ide_models_count'] == 5
    assert clients['summary']['external_providers_count'] == 5

    or_prov = next(p for p in clients['external_providers'] if p['provider_id'] == 'openrouter')
    assert or_prov['env_configured'] is True, 'openrouter should detect keys from proxy/config_free_proxy.json'

    r_low = orchestrator.route_model(reg, 'health_check', 'low')
    assert r_low['resolved_tier_id'] == 'scout-fast'
    assert r_low['primary_ide_model']['model_id'] == 'gemini-3.8-flash'
    assert 'local_proxy_5005' in r_low

    r_med = orchestrator.route_model(reg, 'omnisync_audit', 'medium')
    assert r_med['resolved_tier_id'] == 'architect-sync'
    assert r_med['primary_ide_model']['model_id'] == 'gemini-4-argon'

    r_high = orchestrator.route_model(reg, 'lore_synthesis', 'high')
    assert r_high['resolved_tier_id'] == 'lore-judge'
    assert r_high['primary_ide_model']['model_id'] == 'claude-opus-5.5'

    # Test Special Routing Policies (Grok Bot = Agenda Work Slots ONLY; Gemini Desktop = Argon Image Gen ONLY)
    r_agenda = orchestrator.route_model(reg, 'agenda_work_slot', 'medium')
    assert r_agenda['special_policy_enforced'] is True
    assert r_agenda['dedicated_desktop_client']['client_id'] == 'grok_bot'
    assert r_agenda['dedicated_desktop_client']['executable'] == 'Grok Bot.exe'

    r_img = orchestrator.route_model(reg, 'image_generation', 'high')
    assert r_img['special_policy_enforced'] is True
    assert r_img['dedicated_desktop_client']['client_id'] == 'gemini_desktop'
    assert r_img['primary_ide_model']['model_id'] == 'gemini-4-argon'

    with pytest.raises(ValueError):
        orchestrator.route_model(reg, 'lore_synthesis', 'extreme')


def test_http_rate_limiter_429_503_400_and_stage_failover():
    reg = orchestrator.load_registry()
    state = {'503_count': 0, '429_count': 0}

    class MockHandler(http.server.BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

        def do_GET(self):
            if self.path == '/mock/429':
                state['429_count'] += 1
                self.send_response(429)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"error": "rate_limited"}')
            elif self.path == '/mock/503_then_200':
                state['503_count'] += 1
                if state['503_count'] < 2:
                    self.send_response(503)
                    self.end_headers()
                    self.wfile.write(b'{"error": "transient"}')
                else:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(b'{"ok": true}')
            elif self.path == '/mock/400':
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid parameter xyz"}')

    httpd = socketserver.TCPServer(('127.0.0.1', 0), MockHandler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()

    try:
        client = orchestrator.MultiModelAPIClient(reg)
        res = client.request_json(f'http://127.0.0.1:{port}/mock/503_then_200', retries=3)
        assert res == {'ok': True}
        assert state['503_count'] == 2

        with pytest.raises(orchestrator.RateLimitError) as exc_429:
            client.request_json(f'http://127.0.0.1:{port}/mock/429', retries=2)
        assert '429' in str(exc_429.value)
        assert state['429_count'] == 2

        with pytest.raises(RuntimeError) as exc_400:
            client.request_json(f'http://127.0.0.1:{port}/mock/400', retries=2)
        assert 'Invalid parameter xyz' in str(exc_400.value)
    finally:
        httpd.shutdown()

    # Test horizontal failover in execute_stage_with_fallback when primary model fails on attempt 1
    with tempfile.NamedTemporaryFile('w', suffix='.py', dir=str(ROOT / 'scratch'), delete=False, encoding='utf-8') as tf:
        tf.write(
            "import os, sys\n"
            "if os.environ.get('SVARTULFR_ACTIVE_MODEL') == 'gemini-3.8-flash':\n"
            "    print('Primary failed with simulated 429', file=sys.stderr)\n"
            "    sys.exit(1)\n"
            "print('Twin model succeeded!')\n"
            "sys.exit(0)\n"
        )
        temp_script_path = pathlib.Path(tf.name)

    try:
        stage_def = {
            'stage_id': 'stage_test_failover',
            'name': 'Test Horizontal Twin Failover',
            'script': str(temp_script_path.relative_to(ROOT)),
            'effort': 'low',
        }
        res_stage = orchestrator.execute_stage_with_fallback(
            stage_def, reg['tiers']['tier_1_scout_fast'], reg, limit=2
        )
        assert res_stage['status'] == 'SUCCESS'
        assert res_stage['fallback_triggered'] is True
        assert res_stage['active_model_used'] == 'gemma-4-31B-it'
        assert res_stage['attempts'] == 2
    finally:
        temp_script_path.unlink(missing_ok=True)


def test_dashboard_playwright_headless_dom_and_filters():
    from playwright.sync_api import sync_playwright

    reg = orchestrator.load_registry()
    dash_path = orchestrator.generate_dashboard_html(reg)
    assert dash_path.exists()

    class RootStaticHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(ROOT), **kwargs)

        def log_message(self, format, *args):
            pass

    httpd = socketserver.TCPServer(('127.0.0.1', 0), RootStaticHandler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()

    console_errors = []
    network_errors = []
    chrome_path = r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'
    if not os.path.exists(chrome_path):
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=chrome_path, headless=True)
            page = browser.new_page(viewport={'width': 1440, 'height': 1080})
            page.on('console', lambda m: console_errors.append(m.text) if m.type == 'error' else None)
            page.on(
                'response',
                lambda r: network_errors.append(f'{r.status} {r.url}')
                if r.status >= 400
                else None,
            )

            page.goto(f'http://127.0.0.1:{port}/scratch/unified_pipeline_dashboard.html', wait_until='networkidle')

            badge_text = page.locator('#overall-status-badge').inner_text()
            badge_cls = page.locator('#overall-status-badge').get_attribute('class')
            assert 'ALL_GREEN' in badge_text
            assert 'badge-online' in badge_cls

            assert page.locator('#omen-clients-grid .client-card').count() == 6
            assert page.locator('#tier-matrix-table tbody tr').count() == 3
            assert page.locator('#effort-adapter-table tbody tr').count() == 5
            assert page.locator('#open-providers-table tbody tr').count() == 5
            assert page.locator('#stages-container .stage-card').count() == 6

            buttons = page.locator('.filter-bar .btn')
            buttons.nth(1).click()
            vis_t1 = page.locator('#stages-container .stage-card:visible').count()
            buttons.nth(2).click()
            vis_t2 = page.locator('#stages-container .stage-card:visible').count()
            buttons.nth(3).click()
            vis_t3 = page.locator('#stages-container .stage-card:visible').count()
            buttons.nth(0).click()
            vis_all = page.locator('#stages-container .stage-card:visible').count()

            assert (vis_t1, vis_t2, vis_t3, vis_all) == (3, 1, 2, 6)
            assert console_errors == []
            assert network_errors == []

            page.screenshot(path=str(ROOT / 'scratch' / 'unified_pipeline_dashboard_verified.png'), full_page=True)
            browser.close()
    finally:
        httpd.shutdown()
