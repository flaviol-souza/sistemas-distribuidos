import socket, argparse, time, threading, udp
from datetime import datetime

IP = "127.0.0.1"
PORT = 8080

class Node:
    id_node = ""
    host = None
    seed = None
    peers = {}
    sockets = {}

    def __init__(self, id, ip, port, ip_host, port_host):
        self.id_node = id
        self.seed = (ip, port)
        self.host = (ip_host, port_host)

    def start(self):
        if self.host[0] == None: #node is host!
            self.peers[self.id_node] = self.seed
        else: #node is node!
            udp.send_json(self.sockets, self.host, {
                "type" : "newpeer",
                "data" : self.id_node
            })

        t_receive = threading.Thread(target=self.receive, args=())
        t_send = threading.Thread(target=self.send, args=())

        t_receive.start()
        t_send.start()
    
    def receive(self):
        while True:
            peer_addr, peer_json = udp.receive_json(self.sockets)

            if peer_json['type'] == 'newpeer':
                self.peers[peer_json['data']] = peer_addr
                udp.send_json(self.sockets, peer_addr, {
                    "type" : "peers",
                    "data" : self.peers
                })

            if peer_json['type'] == 'peers':
                self.peers.update(peer_json['data'])
                udp.broadcast_json(self.sockets, self.peers, {
                    'type':'introduce',
                    'data': self.id_node
                })

            if peer_json['type'] == 'introduce':
                print(peer_json['data'] + ' entrou no IFSP Chat P2P!')
                self.peers[peer_json['data']] = peer_addr

            if peer_json['type'] == 'input':
                now = datetime.now()
                date_time_format = now.strftime('%m/%d/%y, %H:%M')
                print("["+date_time_format+"] <"+peer_json['user']+"> "+peer_json['data'])

            if peer_json['type'] == 'exit':
                if self.id_node == peer_json['data']:
                    time.sleep(0.5)
                    break
                self.peers.pop(peer_json['data'])
                print(peer_json['data'] + " say: see you guys!")

    def send(self):
        while True:
            message = input('$:')

            if message == 'exit':
                udp.broadcast_json(self.sockets, self.peers, {
                    'type':'exit',
                    'data': self.id_node
                })
                break

            udp.broadcast_json(self.sockets, self.peers, {
                'type' : 'input',
                'user' : self.id_node,
                'data' : message
            })
        
##### END NODE CLASS

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--NICK', '-n', type=str, default='IFSP Anonymous', help='Define nickname, Default: IFSP Anonymous')
    parser.add_argument('--IP', '-ip', type=str, default=IP, help='Define IP Node, Default:'+str(IP))
    parser.add_argument('--PORT', '-p', type=int, default=PORT, help='Define PORT Node, Default:'+str(PORT))
    parser.add_argument('--IP_HOST', '-iph', type=str, help='Define IP Host')
    parser.add_argument('--PORT_HOST', '-poh', type=int, default=PORT, help='Define PORT Host, Default:'+str(PORT))

    arg = parser.parse_args()
    return arg

def main(args):
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    peer_socket.bind((args.IP, args.PORT))
    peer = Node(args.NICK, args.IP, args.PORT, args.IP_HOST, args.PORT_HOST)
    peer.sockets = peer_socket

    peer.start()

if __name__ == '__main__':
    args = arguments()
    main(args)