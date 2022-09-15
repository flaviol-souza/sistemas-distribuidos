#!/usr/bin/python

import socket
import sys

_len_arg = len(sys.argv)

if _len_arg == 1:
    print("Usage : "+sys.argv[0]+" hostname [port]")
    exit()

hostname = sys.argv[1]

if _len_arg == 3:
    port = int(sys.argv[2])
else:
    print("Usage default web port: 8080")
    port = 8080

READBUF = 16384
s = None

for res in socket.getaddrinfo(hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res

    try:
        s = socket.socket(af, socktype, proto)
    except socket.error:
        s = None
        continue

    try:
        print("\nTrying "+sa[0])
        s.connect(sa)
    except:
        print(socket.error+" "+msg)

        s.close()
        s = None
        continue

    if s:
        print("\nConnected to "+sa[0])

        url = "GET / HTTP/1.1\r\nHost:"+hostname+"\r\n\r\n"
        s.send(url.encode())
        finished = False
        count = 0

        while not finished:
            data = s.recv(READBUF)
            count = count+1
            if len(data) != 0:
                print(repr(data))
            else:
                finished = True

        s.shutdown(socket.SHUT_WR)
        s.close()
        print("\nData was received in "+str(count)+" recv calls")
        break
