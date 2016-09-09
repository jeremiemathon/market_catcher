#!/usr/bin/python3
 
import BaseHTTPServer
import CGIHTTPServer

def server_start(port, address, directory): 
	server_address = (address, port)

	server = BaseHTTPServer.HTTPServer
	handler = CGIHTTPServer.CGIHTTPRequestHandler
	handler.cgi_directories = [directory]
	print "Serveur actif sur le port :", PORT

	httpd = server(server_address, handler)
	httpd.serve_forever()
