import socket
import base64

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.sendall(b'hello, world!')

data = sock.recv(1024)
decode = open('ava.jpg', 'wb')
decode.write(base64.b64decode((data)))
decode.close()

sock.close()

