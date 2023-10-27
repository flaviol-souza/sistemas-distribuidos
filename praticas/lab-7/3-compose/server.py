from socket import *

HOST = gethostname()
PORT = 5001

def setup():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    
    return s

def upper_rpc(s):
    (conn, addr) = s.accept()
    data = conn.recv(1024)
    
    if data:
        conn.send(data.upper())
        print(f"'{data.decode()}' from {addr}")

if __name__ == "__main__":
    s = setup()
    
    while True:
        upper_rpc(s)