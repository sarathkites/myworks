import socket
import threading
from algo import *
import time
import os

class FileServer:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def child_thread(conn):
        from_client = ''
        while True:
            data = conn.recv(1024)
            if not data: break
            
            msg = data.decode("utf-8")
            if msg == 'FILESEND':
                data = conn.recv(1024)
                filename = data.decode("utf-8")
                print(f'Name = {filename}')
                data = conn.recv(1024)
                filesz = data.decode("utf-8")
                print(f'Size = {filesz}')
                cnt = 0
                sz = int(filesz)
                totaldata=b''
                while True:
                    data = conn.recv(1024)
                    cnt += len(data)
                    totaldata += data   
                    if cnt == sz: break
                #print(totaldata)
                milli_sec = int(round(time.time() * 1000))
                print(str(milli_sec)+'_'+filename)
                a = Algo()
                a.write_to_file2(str(milli_sec)+'_'+filename,totaldata)
                print('done')
                break
            elif msg == 'FILEGET':
                data = conn.recv(1024)
                filename = data.decode("utf-8")
                print(f'Name = {filename}')
                a = Algo()
                head, tail = os.path.split(filename)
                blocks = a.get_file_blocks(filename,1024)
                filesz = os.stat(filename).st_size
                conn.send(tail.encode())
                time.sleep(.5)
                conn.send(str(filesz).encode())
                time.sleep(.5)
        
                for block in blocks:
                    conn.send(block)
        
                time.sleep(.5)
        
                break
            else:
                from_client += data.decode("utf-8") 
                #print (from_client)
                conn.send(b'I am SERVER')
        conn.close()    

    def start_server(self,port):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.bind(('0.0.0.0', port))
        self.serv.listen(5)
        print('server started > {}'.format(port))
        while True:
            conn, addr = self.serv.accept()
            th = threading.Thread(target=FileServer.child_thread, args=(conn,))
            th.start()
        print ('client disconnected')

def main():
    port =1234
    s = FileServer()
    s.start_server(port)
    
if __name__ == "__main__":
    main()