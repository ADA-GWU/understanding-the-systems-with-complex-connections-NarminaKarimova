import socket
s = socket.socket()
print('Socket created')
port = 9001
s.bind(('',port))
print(f'socket binded to port{port}')
s.listen(3)
print('Socket is listening')
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    message = ('Thanks for coonection')
    c.send(message.encode())
    c.close()