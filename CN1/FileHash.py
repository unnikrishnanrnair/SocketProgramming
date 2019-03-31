import socket
import sys
import os

arg = str(sys.argv[1])
if len(sys.argv) == 3:
	filename = str(sys.argv[2])

command = 'send_hashtable'
path = './components'

s = socket.socket()
host = socket.gethostname()
port = 60001

s.connect((host, port))
s.send(command.encode('utf-8'))

full_path = os.path.join(path, command)

with open(full_path, 'wb') as f:
    # print('file opened')
    while True:
        # print('receiving data...')
        data = s.recv(1024)
        if not data:
            break
        f.write(data)
f.close()
# print('Successfully retrieved the hashtable')
s.close()
# print('connection closed')
f = open(full_path, "r")
lines = f.readlines()
for x in lines:
	table = x.split(" ")
	if arg == "verify":
		if  table[0]==filename:
			print(table[2], table[3].strip())
	elif arg == "checkall":
		print(table[0],table[2],table[3])
