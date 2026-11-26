import socket

def test_host_headers():
    active_port_file = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort'
    with open(active_port_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    port = int(lines[0])
    path = lines[1]
    
    hosts = [
        f"localhost:{port}",
        "localhost",
        f"127.0.0.1:{port}",
        "127.0.0.1",
    ]
    
    for h in hosts:
        print(f"\nTesting Host header: {h}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        try:
            s.connect(('127.0.0.1', port))
            req = (
                f"GET {path} HTTP/1.1\r\n"
                f"Host: {h}\r\n"
                "Upgrade: websocket\r\n"
                "Connection: Upgrade\r\n"
                "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
                "Sec-WebSocket-Version: 13\r\n"
                "\r\n"
            )
            s.sendall(req.encode('utf-8'))
            resp = s.recv(1024)
            print("Response:", resp.decode('utf-8', errors='replace').split("\r\n")[0])
        except Exception as e:
            print("Error:", e)
        finally:
            s.close()

if __name__ == '__main__':
    test_host_headers()
