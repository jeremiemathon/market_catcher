#!/usr/bin/python3

import time
import datetime
import sys
import os
from market_functions import *
from print_functions import *
from market_webserver import server
import argparse
import io


def parsing():
	parser = argparse.ArgumentParser()
	parser.add_argument("--cli", help="start in cli mode",action='store_true')
	args = parser.parse_args()
	if args.cli:
		return True
	return False

def store_json_file(d):
	with open(".market_catcher.json", "w") as file:
		file.write(str(d))
	

if __name__ == '__main__':
	os.environ['TERM'] = 'xterm'
	d = fulfill_data_file()
	#server.create_server_instance('0.0.0.0',8888,d)
	if parsing():
		while 1:
			os.system('clear')
			print_totals(d)
			print('\n')
			print_table_values(d)
			
			print('\n')
			print_table_globals(d)
			time.sleep(10)
			os.system('clear')
	
	print("Content-type: text/html; charset=utf-8\n\n")
	print("<html><head><title>Répertoire local</title></head><body>")
	import cgitb
	cgitb.enable()
	print_html_totals(d)
	print("</body></html>")
	sys.exit(0)
