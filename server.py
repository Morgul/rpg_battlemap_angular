import sys
from optparse import OptionParser

import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

# Add basic argument parsing
parser = OptionParser()
parser.add_option("-a", "--address", dest="address", help="The address to serve on.", default="0.0.0.0")
parser.add_option("-p", "--port", dest="port", help="The port to serve on.", default=9000)

(options, args) = parser.parse_args()

server_address = (options.address, options.port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()