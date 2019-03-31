import socket
import os 

path = './shared'

port = 60001
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))     
s.listen(5)            

print('Server B listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    filename = conn.recv(1024).decode("utf-8")
    print('Server received request for download of ', str(filename))
    full_path = os.path.join(path, filename)
    f = open(full_path,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       # print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()