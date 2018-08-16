#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import sys
X
PORT = 9000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()


logfile = open('logfile.log','w+')
sys.stdout = logfile
sys.stdin = logfile
sys.stderr = logfile

