import json

BUFFER_MSG = 1024
#python chat.py -n Flavio -p 8081 -iph 127.0.0.1 -poh 8080
def __send_base(from_socket, to_socket, message):
    from_socket.sendto(message.encode(), (to_socket[0], to_socket[1]))

def __receive_base(from_socket):
    return from_socket.recvfrom(BUFFER_MSG)

def broadcast_json(peer_socket, peers_to, message):
    for peer_key, peer_value in peers_to.items(): 
        send_json(peer_socket, peer_value, message)

def send_json(peer_socket, peer_to, message):
    __send_base(peer_socket, peer_to, json.dumps(message))

def receive_json(peer_socket):
    data, addr = __receive_base(peer_socket)
    return addr, json.loads(data)