import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)
s.connect(('127.0.0.1', 9222))
req = (
    "GET /devtools/browser/6a9a1596-d1ba-4ea4-ac7b-198d604f4563 HTTP/1.1\r\n"
    "Host: 127.0.0.1:9222\r\n"
    "Upgrade: websocket\r\n"
    "Connection: Upgrade\r\n"
    "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
    "Sec-WebSocket-Version: 13\r\n"
    "\r\n"
)
s.sendall(req.encode())
resp = s.recv(4096)
print("Response without Origin:")
print(resp.decode(errors='replace'))
s.close()
