import socket
import sys
import os
import select
import hashlib

filename = str(sys.argv[2])
method = str(sys.argv[1])
path = './downloads'
command = method + str(" ") + filename

def tcp_downloader(filename,path):	
	s = socket.socket()
	host = socket.gethostname()
	port = 60003
	s.connect((host, port))
	s.send(command.encode('utf-8'))
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

def udp_downloader(filename,path):
	host="127.0.0.1"
	port = 60004
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host,port))
	addr = (host,port)
	buf=1024
	data,addr = s.recvfrom(buf)
	# print ("Received File:",data.strip())
	full_path = os.path.join(path, filename)
	f = open(full_path,'wb')
	data,addr = s.recvfrom(buf)
	try:
	    while(data):
	        f.write(data)
	        s.settimeout(2)
	        data,addr = s.recvfrom(buf)
	except socket.timeout:
	    f.close()
	    s.close()
	    # print("File Downloaded")

def gethash(filepath):
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	with open(filepath, 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	return str(hasher.hexdigest())

def checkhash():
	command = 'send_hashtable'
	path = './components'
	full_path = os.path.join(path, command)
	f = open(full_path, "r")
	lines = f.readlines()
	for x in lines:
		table = x.split(" ")
		if filename == table[0]:
			if str(table[3]).strip() == gethash(os.path.join('./downloads', filename)):
				# print("file has no errors")
				# print(str(table[3]).strip())
				# print(gethash(os.path.join('./downloads', filename)))
				print(table[0],table[1],table[2],table[3])
			else:
				print("redownload please")

def main():	
	if method=="UDP":
		s = socket.socket()
		host = socket.gethostname()
		port = 60001
		s.connect((host, port))
		s.send(command.encode('utf-8'))
		s.close()
		udp_downloader(filename,path)
	else:
		tcp_downloader(filename,path)
	checkhash()

if __name__ == "__main__":
    main()
