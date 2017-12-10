import socket
req = 'Hey!!'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(1)
s.connect(('127.0.0.1', 1234))
print(2)
s.send(req.encode())
print(3)
#response = s.recv(1024)
s.close()

