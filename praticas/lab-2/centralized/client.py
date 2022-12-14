# Python program to implement client side of chat room.
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:
	#sockets_list = [sys.stdin, server]
	sockets_list = [socket.socket(), server]
	read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])
	read = [read_sockets, sys.stdin]
	for socks in read:
		if socks == read_sockets:
			message = server.recv(2048)
			if message:
				print(message.decode("utf-8"))
		else:
			message = sys.stdin.readline()
			server.send(message.encode())
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush()

server.close()
