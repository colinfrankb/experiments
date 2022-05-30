# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    value = ''

    while value != 'close':
        value = input()
        s.sendall(bytes(value, 'utf-8'))

    s.close()
