#!/usr/bin/python3

import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
from .build_page import build_page

data=""

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		global data
		# Send response status code
		self.send_response(200)

		# Send headers
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send message back to client
		message = build_page(data)
		# Write content as utf-8 data
		self.wfile.write(bytes(message, "utf8"))
		return


def create_server_instance(server,port,d):
	global data
	data = d
	httpd = http.server.HTTPServer((server, port), RequestHandler)
	#httpd.socket = ssl.wrap_socket(httpd.socket, certfile='server.pem', server_side=True)
	httpd.serve_forever()
