import socket
import sys
import os

filename = str(sys.argv[1])
path = './downloads'

s = socket.socket()
host = socket.gethostname()
port = 60001

s.connect((host, port))
s.send(filename.encode('utf-8'))

full_path = os.path.join(path, filename)

with open(full_path, 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        # print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')