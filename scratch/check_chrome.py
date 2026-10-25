import subprocess
import json

cmd = ["powershell", "-NoProfile", "-Command", "Get-Process chrome | Select-Object Id, MainWindowTitle"]
res = subprocess.run(cmd, capture_output=True, text=True)
print("=== CHROME PROCESSES ===")
print(res.stdout)

# Check DevToolsActivePort
with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    print("DevToolsActivePort content:", lines)

# Check curl to /json
curl_res = subprocess.run(["curl.exe", "-i", f"http://127.0.0.1:{lines[0]}/json"], capture_output=True, text=True)
print("Curl /json:", curl_res.stdout)

curl_res2 = subprocess.run(["curl.exe", "-i", f"http://127.0.0.1:{lines[0]}/json/version"], capture_output=True, text=True)
print("Curl /json/version:", curl_res2.stdout)
