@echo off
title Wyvern Proxy - Cloudflare External Tunnel
echo ========================================================
echo   Avvio Tunnel Esterno Cloudflare per Wyvern Proxy (Porta 5005)
echo ========================================================
echo.
echo L'URL HTTPS pubblico temporaneo apparira tra pochi secondi.
echo Copia l'indirizzo 'https://....trycloudflare.com/v1' su Wyvern.
echo.
echo Premi CTRL+C o chiudi questa finestra per terminare il tunnel.
echo.
"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://127.0.0.1:5005
pause
