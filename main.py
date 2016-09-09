#!/usr/bin/python3

import time
import datetime
import sys
import os
from market_functions import *
from print_functions import *
from market_webserver import server


if __name__ == '__main__':
	d = fulfill_data_file()
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
