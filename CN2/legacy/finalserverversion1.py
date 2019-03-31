import socket
import os 
import hashlib 
import time

PORT = 60001
HOST = socket.gethostname()

def sendfile(path,filename,conn):
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

def generatehash():
	try:
	    os.remove(os.path.join("./components", "hashtable"))
	except Exception as e:
	    print("no hashtable created yet ..... creating" )
	f = open(os.path.join('./components', "hashtable"), "a")
	path = './shared'
	files = os.listdir(path)
	for name in files:
	    full_path = os.path.join(path, name)
	    inode = os.stat(full_path)
	    tstamp_e = inode.st_mtime
	    fsize = inode.st_size
	    tstamp=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tstamp_e))
	    BLOCKSIZE = 65536
	    hasher = hashlib.md5()
	    with open(full_path, 'rb') as afile:
	        buf = afile.read(BLOCKSIZE)
	        while len(buf) > 0:
	            hasher.update(buf)
	            buf = afile.read(BLOCKSIZE) 
	    f.write(str(name) + str(' ') + str(fsize) + str(' ') + str(tstamp_e) + str(' ') + str(hasher.hexdigest()) + "\n")
	f.close()

def updatelog(logline):
	pass

def main():
	s = socket.socket()
	s.bind((HOST, PORT))     
	s.listen(5)
	print('Server B listening....')

	while True:
		conn, addr = s.accept()     # Establish connection with client.
		print('Got connection from', addr)
		command = conn.recv(1024).decode("utf-8")
		# updatelog(command)
		if command == 'send_hashtable':
			generatehash()
			sendfile('./components','hashtable',conn)
			# sendfile('./components','logs',conn)
		else:
			sendfile('./shared',command,conn)
		conn.close()

if __name__ == "__main__":
    main()