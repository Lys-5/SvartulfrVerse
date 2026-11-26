import socket

def test_forbidden_body():
    active_port_file = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort'
    with open(active_port_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    port = int(lines[0])
    path = lines[1]
    
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
            "Origin: http://127.0.0.1:9222",
            "\r\n"
        ]
        req = "\r\n".join(headers)
        s.sendall(req.encode('utf-8'))
        resp = s.recv(4096)
        print("Full 403 response:")
        print(resp.decode('utf-8', errors='replace'))
    finally:
        s.close()

if __name__ == '__main__':
    test_forbidden_body()
