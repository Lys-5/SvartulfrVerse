# Script di arresto programmato del tunnel remoto Cloudflare per Wyvern Proxy
$logPath = "E:\repository\SvartulfrVerse\proxy\proxy_debug.log"
$timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
$cfProcs = Get-Process -Name cloudflared -ErrorAction SilentlyContinue
if ($cfProcs) {
    $cfProcs | Stop-Process -Force
    Add-Content -Path $logPath -Value "$timestamp [INFO] 🛑 [REMOTE TUNNEL] Chiusura automatica programmata completata con successo (processo cloudflared terminato)." -Encoding UTF8
    Write-Host "Cloudflared terminato con successo."
} else {
    Add-Content -Path $logPath -Value "$timestamp [INFO] ℹ️ [REMOTE TUNNEL] Timer scaduto: nessun processo cloudflared attivo trovato." -Encoding UTF8
    Write-Host "Nessun processo cloudflared attivo."
}
