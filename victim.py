import socket

host = '127.0.0.1'
port = 5000
s = socket.socket()
s.connect((host, port))

msg = input("enter your commands: ")