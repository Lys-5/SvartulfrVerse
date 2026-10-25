import socket

def test_origins():
    active_port_file = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort'
    with open(active_port_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    port = int(lines[0])
    path = lines[1]
    
    candidate_origins = [
        "null",
        "file://",
        "chrome://newtab",
        "chrome://devtools",
        "devtools://devtools",
        "vscode-file://vscode-app",
        "vscode-webview://",
        "http://localhost",
        "http://127.0.0.1",
        "",
    ]
    
    for origin in candidate_origins:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        try:
            s.connect(('127.0.0.1', port))
            headers = [
                f"GET {path} HTTP/1.1",
                f"Host: 127.0.0.1:{port}",
                "Upgrade: websocket",
                "Connection: Upgrade",
                "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==",
                "Sec-WebSocket-Version: 13",
                f"Origin: {origin}",
                "\r\n"
            ]
            req = "\r\n".join(headers)
            s.sendall(req.encode('utf-8'))
            resp = s.recv(1024)
            status_line = resp.decode('utf-8', errors='replace').split("\r\n")[0]
            print(f"Origin: {origin:25} -> {status_line}")
        except Exception as e:
            print(f"Origin: {origin:25} -> Error: {e}")
        finally:
            s.close()

if __name__ == '__main__':
    test_origins()
