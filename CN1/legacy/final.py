from multiprocessing import Process

def server():
    while 1:
        print("a")

def commandlistener():
    while 1:
        print("b")

if __name__ == '__main__':
    Process(target=server).start()
    Process(target=commandlistener).start()