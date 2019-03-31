import os
import time
import hashlib 

path = './shared'

try:
    os.remove(os.path.join(path, "hashtable"))
except Exception as e:
    print("no hashtable created yet ..... creating" )

f = open(os.path.join(path, "hashtable"), "a")
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