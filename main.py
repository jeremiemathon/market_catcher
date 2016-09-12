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
	#parser.add_argument("file", help="output file to generate json")
	args = parser.parse_args()

def store_json_file(d):
	with open(".market_catcher.json", "w") as file:
		file.write(str(d))
	


if __name__ == '__main__':
	d = fulfill_data_file()
	store_json_file(d)
	#server.create_server_instance('0.0.0.0',8888,d)
	while 1:
		os.system('clear')
		print_totals(d)
		print('\n')
		print_table_values(d)
		
		print('\n')
		print_table_globals(d)
		time.sleep(10)
		os.system('clear')
