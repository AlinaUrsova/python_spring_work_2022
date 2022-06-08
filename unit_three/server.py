import socket

sock = socket.socket()
sock.bind(('localhost', 1515))
sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()