import hashlib

def gethash():
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	with open('sad.mp4', 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	print(hasher.hexdigest())

def getfilelist()
	