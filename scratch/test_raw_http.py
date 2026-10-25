import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3.0)
s.connect(('127.0.0.1', 9222))

# Let's test a simple HTTP GET /json/version
req = (
    "GET /json/version HTTP/1.1\r\n"
    "Host: 127.0.0.1:9222\r\n"
    "User-Agent: curl/7.68.0\r\n"
    "Accept: */*\r\n\r\n"
)
s.sendall(req.encode())
try:
    resp = s.recv(4096)
    print("Response to /json/version:")
    print(resp.decode('utf-8', errors='ignore'))
except Exception as e:
    print("Error:", e)
finally:
    s.close()
