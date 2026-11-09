Set WinScriptHost = CreateObject("WScript.Shell")
' Avvia Python eseguendo lo script in background con reindirizzamento log (0 = finestra nascosta)
WinScriptHost.Run "cmd /c start /B """" ""C:\Users\mande\AppData\Local\Python\pythoncore-3.14-64\python.exe"" ""E:\repository\SvartulfrVerse\proxy\free_tier_proxy.py"" > ""E:\repository\SvartulfrVerse\proxy\uvicorn.log"" 2>&1", 0, False
Set WinScriptHost = Nothing
