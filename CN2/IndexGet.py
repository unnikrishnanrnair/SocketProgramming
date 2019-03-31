import socket
import sys
import os

longorshort = str(sys.argv[1])
starttime = float(sys.argv[2])
endtime = float(sys.argv[3])
if len(sys.argv) == 5:
	filetype = str(sys.argv[4])

def get_historyA(filename,path):
	s = socket.socket()
	host = socket.gethostname()
	port = 60003
	s.connect((host, port))
	s.send(filename.encode('utf-8'))
	full_path = os.path.join(path, filename)
	with open(full_path, 'wb') as f:
	    # print('file opened')
	    while True:
	        # print('receiving data...')
	        data = s.recv(1024)
	        # print('data=%s', (data))
	        if not data:
	            break
	        # write data to a file
	        f.write(data)
	f.close()
	# print('Successfully get the file')
	s.close()
	# print('connection closed')

def logupdate():
	if len(sys.argv) == 5:
		f = open(os.path.join('./components', "historyB"), "a")
		f.write(str(sys.argv[0])+str(sys.argv[1])+str(sys.argv[2])+str(sys.argv[3])+str(sys.argv[4])+'\n')
		f.close()
	else:
		f = open(os.path.join('./components', "historyB"), "a")
		f.write(str(sys.argv[0])+str(sys.argv[1])+str(sys.argv[2])+str(sys.argv[3])+'\n')
		f.close()

command = 'send_hashtable'
path = './components'

s = socket.socket()
host = socket.gethostname()
port = 60003

s.connect((host, port))
s.send(command.encode('utf-8'))

full_path = os.path.join(path, command)

with open(full_path, 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)
f.close()
s.close()
f = open(full_path, "r")
lines = f.readlines()
for x in lines:
	table = x.split(" ")
	if longorshort == "shortlist":
		if len(sys.argv) == 5:
			if starttime <= float(table[2]) <= endtime and table[0].split('.')[1].strip() == filetype.split('.')[1].strip():
				print(table[0])
		if len(sys.argv) == 4:
			if starttime <= float(table[2]) <= endtime:
				print(table[0])	
	else:
		if len(sys.argv) == 5:
			if starttime <= float(table[2]) <= endtime and table[0].split('.')[1].strip() == filetype.split('.')[1].strip():
				print(table[0],table[2],table[3])
		if len(sys.argv) == 4:
			if starttime <= float(table[2]) <= endtime:
				print(table[0],table[2],table[3])
logupdate()
get_historyA('historyA','./components')
