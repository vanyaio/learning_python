import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)
while True:
    conn, adr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            print('the end')
            break
        print(data)
    conn.close()

    
