import subprocess
import json

out = subprocess.check_output(['powershell', '-Command', "Get-CimInstance Win32_Process -Filter \"ProcessId = 24720\" | Select-Object ProcessId, ParentProcessId, CommandLine | ConvertTo-Json"]).decode('utf-8', errors='ignore')
print(out)
