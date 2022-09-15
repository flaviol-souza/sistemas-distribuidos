#!/usr/bin/python

import socket, sys, time
# Server runs on all IP addresses by default
HOST=''
# 8080 can be used without root priviledges
PORT=8080
BUFLEN=8192 # buffer size

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

try:
    print("\nStarting HTTP server on port ", PORT)
    s.bind((HOST,PORT,0,0))
except socket.error :
    print("Cannot bind to port :", PORT)
    sys.exit(-1)

s.listen(10) # maximum 10 queued connections

while True:
    # a real server would be multithreaded and would catch exceptions
    conn = None
    try:
        conn, addr = s.accept()
        print("\nConnection from ", addr)
        data=''

        while not '\n' in data : # wait until first line has been received
            data = data + conn.recv(BUFLEN).decode('utf-8')

        if data.startswith('GET'):
            # GET request
            #conn.send('HTTP/1.0 404 Not Found\r\n'.encode())
            conn.send('HTTP/1.0 200 OK\n'.encode())
            conn.send('Content-Type: text/html\n'.encode())
            conn.send('\n'.encode()) # header and body should be separated by additional newline
            conn.send("""
                <html>
                <body>
                <h1>Hello World</h1> this is my server!
                </body>
                </html>
            """.encode()) # Use triple-quote string.
        else:
            # other type of HTTP request
            conn.send('HTTP/1.0 501 Not implemented\r\n')
            
        now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        conn.send(('Date: ' + now +'\r\n').encode())
        conn.send('Server: IFSP Lab SD Server\r\n'.encode())
        conn.send('\r\n'.encode())
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
    except KeyboardInterrupt:
        if conn:  # <---
            conn.close()
        break  
    