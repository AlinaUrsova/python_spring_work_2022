import socket
import base64

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()
print(addr)


while True:
     data = conn.recv(1024)
     #print(data)
     if not data:
         break
     with open('ava.jpg', "rb") as image2string:
         converted_string = base64.b64encode(image2string.read())
     conn.send(converted_string)



conn.close()