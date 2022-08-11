#!/usr/bin/python

import http.client as httplib
import sys

_len_arg = len(sys.argv)

if _len_arg == 1:
    print("Usage : "+sys.argv[0]+" hostname [port]")
    exit()

path = '/'
hostname = sys.argv[1]
if len(sys.argv) == 3:
    port = int(sys.argv[2])
else:
    port = 80

conn = httplib.HTTPConnection(hostname, port)
conn.request("GET", path)
r = conn.getresponse()

print("Response is %i (%s)\n\n" % (r.status, r.reason))
print(r.read())
