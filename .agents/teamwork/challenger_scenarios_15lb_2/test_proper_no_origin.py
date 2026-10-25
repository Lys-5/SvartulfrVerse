import socket

def test_proper_no_origin():
    active_port_file = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort'
    with open(active_port_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    port = int(lines[0])
    path = lines[1]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5.0)
    try:
        s.connect(('127.0.0.1', port))
        req = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: 127.0.0.1:{port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            "\r\n"
        )
        print("Sending proper HTTP request without Origin header...")
        s.sendall(req.encode('utf-8'))
        resp = s.recv(4096)
        print("Response received:")
        print(resp.decode('utf-8', errors='replace'))
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        s.close()

if __name__ == '__main__':
    test_proper_no_origin()
