#!/usr/bin/env python3
"""
scripts/daily_maintenance_runner.py

Unified Daily Maintenance Runner for Svartulfr Verse.
Delegates execution to the 5-Stage Multi-Model Unified Pipeline Orchestrator
(.agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py),
which executes:
  - Stage 0 [Tier 1 - Low]: Vault Health Check & PC OMEN AI Clients Scan
  - Stage 1A [Tier 1 - Low]: Wyvern Platform Bundle Monitor
  - Stage 1B [Tier 1 - Medium]: Proxy Free Models Hierarchy Update (:5005)
  - Stage 2 [Tier 2 - Medium]: Omni-Sync Forensic Audit & Byte-for-Byte Parity
  - Stage 3A [Tier 3 - High]: Active Chat Monitor & Character Lore Enrichment
  - Stage 3B [Tier 3 - High]: Archive Lore Mining Engine
  - Stage 4 [Telemetry]: Interactive HTML Dashboard & Unified Markdown Report
"""

import argparse
import datetime
import json
import pathlib
import subprocess
import sys

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'
ORCHESTRATOR = ROOT / '.agents' / 'skills' / 'multi-model-unified-pipeline' / 'scripts' / 'orchestrator.py'
RUN_JSON = SCRATCH / 'unified_pipeline_run.json'
REPORT_FILE = SCRATCH / 'daily_maintenance_report.md'
DASHBOARD_HTML = SCRATCH / 'unified_pipeline_dashboard.html'


def main():
    parser = argparse.ArgumentParser(description='Unified Daily Maintenance Runner (Multi-Model Team)')
    parser.add_argument('--limit', type=int, default=5, help='Batch limit for character enrichment and archive mining')
    parser.add_argument('--output', default=str(RUN_JSON), help='Output JSON path for unified pipeline telemetry')
    args = parser.parse_args()

    date_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'=== Antigravity Unified Daily Master Pipeline Runner [{date_str}] ===')

    cmd = [
        sys.executable,
        str(ORCHESTRATOR),
        'run-all',
        '--limit',
        str(args.limit),
        '--output',
        str(args.output),
    ]
    proc = subprocess.run(cmd, cwd=str(ROOT), text=True, encoding='utf-8')
    if proc.returncode != 0:
        print(f'Unified pipeline exited with code {proc.returncode}', file=sys.stderr)
        sys.exit(proc.returncode)

    print(f'\nUnified Maintenance Complete!')
    print(f'  • JSON Telemetry: {args.output}')
    print(f'  • Markdown Report: {REPORT_FILE}')
    print(f'  • HTML Dashboard:  {DASHBOARD_HTML}')


if __name__ == '__main__':
    main()
