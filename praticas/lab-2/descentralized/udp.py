import socket
import threading
import sys
import json

def sendmbase(udp_socket, toA, message ):
    udp_socket.sendto(message.encode(),(toA[0],toA[1]))

def recembase(udp_socket):
    data, addr = udp_socket.recvfrom(1024)
    return data.decode(), addr 

def sendJS(udp_socket,toA,message):
    sendmbase(udp_socket,toA,json.dumps(message))

def broadcastms(udp_socket,message, peers):
    for p in peers.values():
        sendmbase(udp_socket,p,message)

def broadcastJS(udp_socket,message, peers):
    for p in peers.values():
        sendJS(udp_socket,p,message)

def rece(udp_socket):
    while 1:
        data,addr = recembase(udp_socket)
        print(data)

def send(udp_socket):
    while True:
        msg = input("please input message and port:")
        l = msg.split()
        port = int(l[-1])
        s = ' '.join(l[:-1])
        toA = ('127.0.0.1', port)
        sendmbase(udp_socket, toA, s)

def main():
    port = int(sys.argv[1]) 
    fromA = ("127.0.0.1",port)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((fromA[0],fromA[1]))
    t1 = threading.Thread(target=rece, args=(udp_socket,))
    t2 = threading.Thread(target=send, args=(udp_socket,))
    t1.start()
    t2.start()
 
 
if __name__ == '__main__':
    main()