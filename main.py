#!/usr/bin/python3

from pprint import pprint
from market_functions import *
from print_functions import *


if __name__ == '__main__':
	d = fulfill_data_file()
	while 1:
		os.system('clear')
		print_totals(d)
		print('\n')
		print_table_values(d)
		
		print('\n')
		print_table_globals(d)
		time.sleep(10)
		os.system('clear')
