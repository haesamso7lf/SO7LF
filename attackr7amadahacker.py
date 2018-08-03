import socket
import subprocess
import sys

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.bind((host, port))
s.listen(5)

conn, addr = s.accept()
print("conection from", addr)
#data = s.recv(1024).decode('utf-8')
#print(data)