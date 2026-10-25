import subprocess
import json

out = subprocess.check_output(
    ["powershell", "-NoProfile", "-Command", "Get-CimInstance Win32_Process -Filter \"Name='chrome.exe'\" | Select-Object ProcessId, CommandLine | ConvertTo-Json"],
    text=True
)

procs = json.loads(out)
if isinstance(procs, dict):
    procs = [procs]

for p in procs:
    cmd = p.get('CommandLine') or ''
    pid = p.get('ProcessId')
    print(f"PID: {pid} -> {cmd[:120]}")
