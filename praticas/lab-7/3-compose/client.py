from socket import *

HOST = "192.168.1.2"
PORT = 5001
 
def upper_rcp(msg):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(msg.encode())
    data = s.recv(1024)
    s.close()

    return data.decode()

if __name__ == "__main__":
    msg = input("say> ")
    resp = upper_rcp(msg)
    print(f"echo> {resp}")