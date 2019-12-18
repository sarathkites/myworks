import socket
import time
from algo import *
import os
class FileClient:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @staticmethod
    def send_file(ip,port,filename):
        a = Algo()
        head, tail = os.path.split(filename)

        blocks = a.get_file_blocks(filename,1024)
        filesz = os.stat(filename).st_size
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))

        client.send(b'FILESEND')
        time.sleep(.5)
        client.send(tail.encode())
        time.sleep(.5)
        client.send(str(filesz).encode())
        time.sleep(.5)
        
        for block in blocks:
            client.send(block)
        
        time.sleep(.5)
        client.close()

    @staticmethod
    def get_file(ip,port,filename):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.send(b'FILEGET')
        time.sleep(.5)
        client.send(filename.encode())
        time.sleep(.5)
        data = client.recv(1024)
        filename = data.decode("utf-8")
        print(f'Name = {filename}')
        data = client.recv(1024)
        filesz = data.decode("utf-8")
        print(f'Size = {filesz}')
        cnt = 0
        sz = int(filesz)
        totaldata=b''
        while True:
            data = client.recv(1024)
            cnt += len(data)
            totaldata += data   
            if cnt == sz: break
        #print(totaldata)
        milli_sec = int(round(time.time() * 1000))
        print(str(milli_sec)+'_'+filename)
        a = Algo()
        a.write_to_file2(str(milli_sec)+'_'+filename,totaldata)
        print('Fetch File done')
        client.close()
                

def main():
    FileClient.get_file('127.0.0.1',1234,'1.txt')


if __name__ == "__main__":
    main()