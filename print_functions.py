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
		ret = ret + "bgcolor=\"#FF0000\" width=\"70\"><font color=\"black\">" + str('%-8.2f' % (value))
	if value >= 0 and colorize:
		ret = ret + "bgcolor=\"#00FF00\" width=\"70\"><font color=\"black\">" + str('%-8.2f' % (value))
	if not colorize:
		ret = ret + " width=\"70\"><font color=\"white\">" + str('%-8.2f' % (value))

	
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
		ret = ret + + str('%-8.2f' % (value))

	
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
	
	print("<table cellspacing=\"3\"><tr><td width=70>TOTAL</font></td>" + total + "</tr>")
	print("<tr><td width=\"70\">DAY</font></td>" + day + "</tr>")
	print("<tr><td width=\"70\">PERF</font></td>" + total_variation + "</tr>")
	print("<tr><td width=\"70\">%PERF</font></td>" + total_performance + "</tr></table>")

def print_html_globals(d):
	print("<table cellspacing=\"3\"><tr><th width=\"150\">NAME</th><th width=\"70\">PRICE</th><th width=\"70\">%DAY</th></tr>")
	for v in d["globals"]:
		price = colorize_html_value(v["c"],"none",False)
		pc_day = colorize_html_value(v["cp_fix"],"percent",True)
		print("<tr><td width=70><font color=\"white\">" + v["name"] + "</font>" + price + pc_day )
	print("</table>")


def print_html_values(d):
	print("<table cellspacing=\"3\"><tr><th width=\"150\">NAME</th><th width=\"70\">INVEST</th><th width=\"70\">PRU</th><th width=\"70\">PRICE</th><th width=\"70\">%DAY</th><th width=\"70\">DAY</th><th width=\"70\">TOTAL</th><th width=\"70\">%TOTAL</th>\n</tr>")
	for v in d["values"]:
		pru = colorize_html_value(v["pru"],"euro",False)
		price = colorize_html_value(v["c"],"euro",False)
		pc_day = colorize_html_value(v["cp_fix"],"percent",True)
		day = colorize_html_value(v["c_fix"]*v["nb"],"euro",True)
		total = colorize_html_value(v["nb"]*(v["c"]-v["pru"]),"euro",True)
		invest = colorize_html_value(v["nb"]*v["pru"],"euro",False)
		pc_total = colorize_html_value(100 * (v["nb"]*(v["c"]-v["pru"])) / (v["nb"]*v["pru"]),"percent",True)
		name = "<tr>\n\t<td width=\"70\"><font color=\"white\">" + str('%-8s' % (v["name"])) + "</font></td>"
		print(name + invest + pru + price + pc_day + day + total + pc_total +"\n</tr>")
	print("</table>")
