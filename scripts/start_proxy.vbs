Set WinScriptHost = CreateObject("WScript.Shell")
' Avvia Python eseguendo lo script in background (0 = finestra nascosta)
WinScriptHost.Run """C:\Users\mande\AppData\Local\Python\pythoncore-3.14-64\python.exe"" ""E:\repository\SvartulfrVerse\scripts\free_tier_proxy.py""", 0, False
Set WinScriptHost = Nothing