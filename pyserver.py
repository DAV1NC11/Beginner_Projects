import os
from http.server import HTTPServer, CGIHTTPRequestHandler

#Make sure the server is created at current directory
os.chdir('.')
#Create server object listening at port 80
server_object = HTTPServer(server_address = ('192.168.0.103', 80),
RequestHandlerClass = CGIHTTPRequestHandler)
server_object.serve_forever()