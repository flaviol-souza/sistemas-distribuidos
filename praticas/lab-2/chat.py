import argparse
import json 
import time
import threading
import socket
import sys
from xxlimited import Str 
from datetime import datetime

import udp as pu 

IP = "127.0.0.1"
PORT = 8891

class Node:
    seed = (IP, PORT)
    peers = {}
    idNode = ""
    udp_socket = {}

    def __init__(self, ip, port, idNode):
        #self.seed = (ip, port)
        self.idNode = idNode

    def receive(self):
        while True:
            data, addr = pu.recembase(self.udp_socket)
            action = json.loads(data)
            # print(action["type"])
        #     self.dispatch(action, addr)
        # def dispatch(self, action,addr):
            if action['type'] == 'newpeer':
                self.peers[action['data']] = addr
                pu.sendJS(self.udp_socket, addr, {
                    "type":'peers',
                    "data":self.peers
                })         

            if action['type'] == 'peers':
                self.peers.update(action['data'])
                pu.broadcastJS(self.udp_socket, {
                    "type":"introduce",
                    "data": self.idNode
                },self.peers) 

            if action['type'] == 'introduce':
                print(action['data'] + " entrou no chat IFSP P2P")
                self.peers[action['data']] = addr   

            if action['type'] == 'input':
                now = datetime.now()
                date_time = now.strftime("%m/%d/%y, %H:%M")
                print("["+date_time+"] <"+action['user']+">  "+action['data'])  

            if action['type'] == 'exit':
                if(self.idNode == action['data']):
                    time.sleep(0.5) 
                    break;
                value, key = self.peers.pop(action['data'])
                print( action['data'] + " saiu do chat IFSP P2P.")          
            
    def startPeer(self):
        pu.sendJS(self.udp_socket, self.seed, {
            "type": "newpeer",
            "data": self.idNode
        })

    def send(self):
        while True: 
            msg_input = input("$:")
            if msg_input == "exit":
                pu.broadcastJS(self.udp_socket, {
                    "type":"exit",
                    "data":self.idNode
                },self.peers)
                break    

            if msg_input == "friends":
                print(self.peers) 
                continue      

            pu.broadcastJS(self.udp_socket, {
                "type": "input",
                "user": self.idNode,
                "data": msg_input
            }, self.peers) 

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--NICK', '-n', help='Nick, Default: IFSP anonymous', type= str, default='IFSP anonymous')
    parser.add_argument('--IP', '-ip', help='IP, Default: '+IP, type= str, default=IP)
    parser.add_argument('--PORT', '-p', help='Port, Default: '+str(PORT), type= int, default= PORT)

    args = parser.parse_args()

    return args

def main(args):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((args.IP, args.PORT))
    peer = Node(args.IP, args.PORT, args.NICK)
    peer.udp_socket = udp_socket
    
    peer.startPeer()
    
    t1 = threading.Thread(target=peer.receive, args=())
    t2 = threading.Thread(target=peer.send, args=())

    t1.start()
    t2.start()


if __name__ == '__main__':
    args = arguments()
    main(args)           