#!/usr/bin/python3

import socket
import sys

buffer_size = 4096
forward_to = ('ifsp.edu.br', 80)

class Forward:
    def __init__(self):
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port):
        try:
            self.forward.connect((host, port))
            return self.forward
        except Exception as e:
            print(e)
            return False

class Proxy:
    input_list = []
    channel = {}

    def __init__(self, host, port):
        self.s = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(200)

    def start(self):
        
        while True:
            clientsock, clientaddr = self.socket.accept()
            forward = Forward().start(forward_to[0], forward_to[1])
            
            if forward:
                print(clientaddr, "has connected")
                self.input_list.append(clientsock)
                self.input_list.append(forward)
            else:
                print("Can't establish connection with remote server.", end=' ')
                print("Closing connection with client side", clientaddr)
                clientsock.close()

            ref = 1
            for self.idx, self.s in enumerate(self.input_list):
                self.data = self.s.recv(buffer_size)
                print(self.s.getsockname()[0]+':'+str(len(self.data)))
                print(self.data)
                if len(self.data) == 0:
                    self.input_list[0].close()  
                    self.input_list[1].close() 
                    print('Close sockets')
                    break
                else:
                    self.input_list[self.idx+ref].send(self.data)
                ref*=-1
            self.input_list.clear()
            
if __name__ == '__main__':
    proxy = Proxy('localhost', 33333)
    try:
        proxy.start()
    except KeyboardInterrupt:
        print("Ctrl C - Stopping proxy")
        sys.exit(1)