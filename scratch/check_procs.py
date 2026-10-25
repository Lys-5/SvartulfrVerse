import subprocess
import json

out = subprocess.check_output(['powershell', '-Command', "Get-CimInstance Win32_Process -Filter \"Name = 'chrome.exe'\" | Select-Object ProcessId, ParentProcessId, CommandLine | ConvertTo-Json"]).decode('utf-8', errors='ignore')
data = json.loads(out)
if isinstance(data, dict):
    data = [data]
for p in data:
    print(f"PID: {p['ProcessId']}, Parent: {p['ParentProcessId']}")
    print(f"  CMD: {p.get('CommandLine')}")
