#!/usr/bin/python3

import time
import datetime
import sys
import os
import bs4
from market_functions import *
from print_functions import *
from twitter import *
from boursorama import *
import argparse
import io
import cgitb
import cgi
import re

def parsing():
	parser = argparse.ArgumentParser()
	parser.add_argument("--cli", help="start in cli mode",action='store_true')
	args = parser.parse_args()
	if args.cli:
		return True
	return False

#def store_json_file(d):
#	with open(".market_catcher.json", "w") as file:
#		file.write(str(d))
	

if __name__ == '__main__':
	cgitb.enable()
	now = datetime.datetime.now()
	d = fulfill_data_file()
	file = open("main.json","w")
	file.write(str(d).replace("'",'"'))
	file.close()
	#server.create_server_instance('0.0.0.0',8888,d)
	if parsing():
		while 1:
			print(d)
			os.environ['TERM'] = 'xterm'
			os.system('clear')
			print_totals(d)
			print('\n')
			print_table_values(d)
			
			print('\n')
			print_table_globals(d)
			time.sleep(10)
			exit(0)
			os.system('clear')
	
	print("Content-Type: text/html;charset=\"utf-8\"\n\n")
	print("<meta http-equiv=\"refresh\" content=\"30\" />")
	print("<meta http-equiv=\"cache-control\" content=\"max-age=0\" />")
	print("<meta http-equiv=\"cache-control\" content=\"no-cache\" />")
	print("<meta http-equiv=\"expires\" content=\"0\" />")
	print("<meta http-equiv=\"expires\" content=\"Tue, 01 Jan 1980 1:00:00 GMT\" />")
	print("<meta http-equiv=\"pragma\" content=\"no-cache\" />")
	font = "<STYLE TYPE=\"text/css\">body{color: white;}</STYLE>"
	font = "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/style.css\">" 
	print("<html><head>" + font + "<title>STOCKS</title></head><body bgcolor=\"#000000\" font-size=\"50%\">")
	print(now.strftime("%Y-%m-%d %H:%M"))
	arguments = cgi.FieldStorage()
	for i in arguments.keys():
		 print(arguments[i].value)
	print("<table class=\"stock_table\"><tr><th width=\"25%\">INDICES</th><th width=\"50%\">PORTFOLIO</th><th width=\"25%\">TOTALS</th></tr><tr valign=\"top\"><td>")
	print_html_globals(d)
	print("</td><td>")
	print_html_values(d)
	print("</td><td>")
	print_html_totals(d)
	print("</td></tr></table>")
	print("<table height=\"70%\" width=\"100%\"><tr><td>")
	twitter()
	print("</td><td>")
	parse_boursorama_forum("ALCLS")
	print("</td></tr></table>")
	print("</body></html>")
