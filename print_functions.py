#!/usr/bin/python3

class color:
        #POSITIVE = '\033[42m'
        #NEGATIVE = '\033[41m'
        #POSITIVE = '\033[30;42m'
        #NEGATIVE = '\033[1;30;41m'
        #MIDDLE = '\033[1;30;43m'
        POSITIVE = '\033[1;32m'
        NEGATIVE = '\033[1;31m'
        MIDDLE = '\033[1;33m'
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

def colorize_html_value(value,currency,colorize):
	ret = "<td "
	if value < 0 and colorize:
		ret = ret + "bgcolor=\"#FF0000\" width=\"100\"><font color=\"black\">" + str('%-8.2f' % (value))
	if value >= 0 and colorize:
		ret = ret + "bgcolor=\"#00FF00\" width=\"100\"><font color=\"black\">" + str('%-8.2f' % (value))
	if not colorize:
		ret = ret + " width=\"100\"><font color=\"white\">" + str('%-8.2f' % (value))

	
	if "euro" in currency:
		ret = ret + "&#8364;</font></td>"
	if "percent" in currency:
		ret = ret + "%</font></td>"
	if "none" in currency:
		ret = ret + "</font></td>"
	return ret

def colorize_html2_value(value,currency,colorize):
	ret = ""
	if value < 0 and colorize:
		ret = ret + "<font color=\"black\">" + str('%-8.2f' % (value))
	if value >= 0 and colorize:
		ret = ret + "<font color=\"black\">" + str('%-8.2f' % (value))
	if not colorize:
		ret = ret + "<font color=\"white\">" + str('%-8.2f' % (value))

	
	if "euro" in currency:
		ret = ret + "&#8364;</font>"
	if "percent" in currency:
		ret = ret + "%</font>"
	if "none" in currency:
		ret = ret + "</font>"
	return ret

def print_html_totals(data):
	total = colorize_html_value(data["total"],"euro",True)
	day = colorize_html_value(data["total"] - data["total_fix"],"euro",True)
	total_variation  = colorize_html_value(data["total"] - data["total_pru"],"euro",True)
	total_performance = colorize_html_value(100 * (data["total"] - data["total_pru"] + data["wallet_cash"]) / data["wallet_total_transfers"],"percent",True)
	
	print("<table><tr><td width=210><font color=\"white\">TOTAL</font></td>" + total + "</tr>")
	print("<tr><td width=210><font color=\"white\">DAY</font></td>" + day + "</tr>")
	print("<tr><td width=210><font color=\"white\">PERF</font></td>" + total_variation + "</tr>")
	print("<tr><td width=210><font color=\"white\">%PERF</font></td>" + total_performance + "</tr></table>")
	#print("<div class=\"wrapper\"><div class=\"table\"><div class=\"row\"><div class=\"cell\">TOTAL</div><div class=\"cell\">" + total + "</div></div>")
	#print("<div class=\"row\"><div class=\"cell\">DAY</div><div class=\"cell\">" + day + "</div></div>")
	#print("<div class=\"row\"><div class=\"cell\">PERF</div><div class=\"cell\">" + total_variation + "</div></div>")
	#print("<div class=\"row\"><div class=\"cell\">%PERF</div><div class=\"cell\">" + total_performance + "</div></div></div></div>")

def print_html_globals(d):
	print("<p>&nbsp;</p><table cellspacing=\"3\"><tr><td width=\"100\">NAME</td><td width=\"100\">PRICE</td><td width=\"100\">%DAY</td></tr>")
	for v in d["globals"]:
		price = colorize_html_value(v["c"],"none",False)
		pc_day = colorize_html_value(v["cp_fix"],"percent",True)
		print("<tr><td width=210><font color=\"white\">" + v["name"] + "</font>" + price + pc_day )
	print("</table>")


def print_html_values(d):
	print("<p>&nbsp;</p>\n<table cellspacing=\"3\">\n<tr>\n\t<td width=210>NAME    </td><td width=100>PRU</td><td width=100>PRICE</td><td width=100>%DAY</td><td width=100>DAY</td><td width=100>TOTAL</td>\n</tr>")
	for v in d["values"]:
		pru = colorize_html_value(v["pru"],"euro",False)
		price = colorize_html_value(v["c"],"euro",False)
		pc_day = colorize_html_value(v["cp_fix"],"percent",True)
		day = colorize_html_value(v["c_fix"]*v["nb"],"euro",True)
		total = colorize_html_value(v["nb"]*(v["c"]-v["pru"]),"euro",True)
		name = "<tr>\n\t<td width=100><font color=\"white\">" + str('%-8s' % (v["name"])) + "</font></td>"
		print(name + pru + price + pc_day + day + total + "\n</tr>")
	print("</table>")
