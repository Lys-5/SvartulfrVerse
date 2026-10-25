import socket

def test_raw_ws():
    active_port_file = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort'
    with open(active_port_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    port = int(lines[0])
    path = lines[1]
    
    print(f"Target: 127.0.0.1:{port}{path}")
    
    test_origins = [
        None,
        "http://127.0.0.1:9222",
        "http://localhost:9222",
        "chrome-devtools://devtools",
        "https://app.wyvern.chat"
    ]
    
    for origin in test_origins:
        print(f"\n--- Testing Origin: {origin} ---")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.0)
        try:
            s.connect(('127.0.0.1', port))
            headers = [
                f"GET {path} HTTP/1.1",
                f"Host: 127.0.0.1:{port}",
                "Upgrade: websocket",
                "Connection: Upgrade",
                "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==",
                "Sec-WebSocket-Version: 13",
            ]
            if origin:
                headers.append(f"Origin: {origin}")
            headers.append("\r\n")
            req = "\r\n".join(headers)
            s.sendall(req.encode('utf-8'))
            
            resp = s.recv(4096)
            print("Response status line & headers:")
            print(resp.decode('utf-8', errors='replace').split("\r\n\r\n")[0])
        except Exception as e:
            print(f"Error: {e}")
        finally:
            s.close()

if __name__ == '__main__':
    test_raw_ws()
