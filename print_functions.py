#!/usr/bin/python3

class color:
        #POSITIVE = '\033[42m'
        #NEGATIVE = '\033[41m'
        POSITIVE = '\033[30;42m'
        NEGATIVE = '\033[1;30;41m'
        MIDDLE = '\033[1;30;43m'
        BOLD = '\033[1m'
        END = '\033[0m'

def colorize_print_value(value):
	if value < 0:
		return color.NEGATIVE + str('%-8.2f' % (value)) + color.END
	return color.POSITIVE + str('%-8.2f' % (value)) + color.END

def print_table_values(d):
	print('%-15s' % ('NAME'), '%-8s' % ('PRU'),'%-8s' % ('PRICE'),'%-8s' % ('%DAY'),'%-8s' % ('DAY'),'%-8s' % ('TOTAL'))
	for v in d["values"]:
		#pru = colorize_print_value(v["pru"])
		pru = str('%-8.2f' % (v["pru"]))
		price = colorize_print_value(v["c"])
		price = str('%-8.2f' % (v["c"]))
		pc_day = colorize_print_value(v["cp_fix"])
		day = colorize_print_value(v["c_fix"]*v["nb"])
		total = colorize_print_value(v["nb"]*(v["c"]-v["pru"]))
		print('%-15s' % (v["name"]), pru, price, pc_day, day, total)


def print_table_globals(d):
	print('%-15s' % ('NAME'), '%-8s' % ('PRICE'),'%-8s' % ('%DAY'))
	for v in d["globals"]:
		price = colorize_print_value(v["c"])
		pc_day = colorize_print_value(v["cp_fix"])
		print('%-15s' % (v["name"]), price, pc_day)

def print_totals(data):
	total = colorize_print_value(data["total"])
	day = colorize_print_value(data["total"] - data["total_fix"])
	total_variation = colorize_print_value(data["total"] - data["total_pru"])
	total_performance = colorize_print_value(100 * (data["total"] - data["total_pru"] + data["wallet_cash"]) / data["wallet_total_transfers"])
	

	print('%-15s' % ('TOTAL'), '%-8s' % (total))
	print('%-15s' % ('DAY'), '%-8s' % (day))
	print('%-15s' % ('PERF'), '%-8s' % (total_variation))
	print('%-15s' % ('%PERF'), '%-8s' % (total_performance))