#!/usr/bin/python3
from currency_converter import CurrencyConverter


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

anonymous = "off"

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

def colorize_html_value(value,currency,colorize,anonymous):
	if "crypto" in currency:
		ret = "<td "
		ret = ret + "width=\"70\">" + str('%-8.6f' % (value))
		ret = ret + "</font></td>"
		return ret

	ret = "<td "
	if value < 0 and colorize:
		if anonymous:
			temp = "width=\"70\"><font color=\"#FF0000\">-### "
		else: temp = "width=\"70\"><font color=\"#FF0000\">" + str('%-8.2f' % (value))
		#ret = ret + "bgcolor=\"#FF0000\" width=\"70\"><font color=\"black\">" + str('%-8.2f' % (value))
		ret = ret + temp
	if value > 0 and colorize:
		if anonymous:
			temp = "width=\"70\"><font color=\"#00FF00\">### "
		else: temp = "width=\"70\"><font color=\"#00FF00\">" + str('%-8.2f' % (value))
		#ret = ret + "bgcolor=\"#00FF00\" width=\"70\"><font color=\"black\">" + str('%-8.2f' % (value))
		ret = ret + temp
	if value == 0 and colorize:
		if anonymous:
			temp = "width=\"70\"><font color=\"#6E6E6E\">### "
		else: temp = "width=\"70\"><font color=\"#6E6E6E\">" + str('%-8.2f' % (value))
		ret = ret + temp
	if not colorize:
		if anonymous:
			temp = "width=\"70\">### "
		else: temp = "width=\"70\">" + str('%-8.2f' % (value))
		ret = ret + temp

	
	if "euro" in currency:
		ret = ret + "&#8364;</font></td>"
	if "dollar" in currency:
		c = CurrencyConverter()
		eur = c.convert(value,'USD','EUR')
		ret = ret + "&#36;/" + str('%-8.2f' % (eur)) + "&#8364;</font></td>"
	if "percent" in currency:
		ret = ret + "%</font></td>"
	if "none" in currency:
		ret = ret + "</font></td>"
	return ret


def print_html_totals(data):
	global anonymous
	if data["anonymous"] == "on":
		anonymous = True
	else: anonymous = False
	total = colorize_html_value(data["total"] + data["wallet_cash"],"euro",True,anonymous)
	day = colorize_html_value(data["total_fix"],"euro",True,anonymous)
	total_variation  = colorize_html_value(data["total"] - data["total_pru"],"euro",True,anonymous)
	total_performance = colorize_html_value(100 * (data["total"] - data["total_pru"] + data["wallet_cash"]) / data["wallet_total_transfers"],"percent",True,False)
	wallet_variation = colorize_html_value(data["total"] + data["wallet_cash"] - data["wallet_total_transfers"],"euro",True,anonymous)
	wallet_performance = colorize_html_value(100 * (data["total"] + data["wallet_cash"] - data["wallet_total_transfers"]) / data["wallet_total_transfers"],"percent",True,False)
	old_variation = colorize_html_value(data["wallet_cash"] - data["wallet_total_transfers"] + data["total_pru"],"euro",True,False)
	
	print("<table cellspacing=\"3\" width=\"100%\"><tr><td width=\"70\" class=\"totals_td\">TOTAL</td>" + total + "</tr>")
	print("<tr><td width=\"70\" class=\"totals_td\">DAY</td>" + day + "</tr>")
	print("<tr><td width=\"70\" class=\"totals_td\">POS PERF</td>" + total_variation + "</tr>")
	print("<tr><td width=\"70\" class=\"totals_td\">%POS PERF</td>" + total_performance + "</tr>")
	print("<tr><td width=\"70\" class=\"totals_td\">INVEST PERF</td>" + wallet_variation + "</tr>")
	print("<tr><td width=\"70\" class=\"totals_td\">%INVEST PERF</td>" + wallet_performance + "</tr>")
	print("<tr><td width=\"70\" class=\"totals_td\">OLD POS</td>" + old_variation + "</tr></table>")

def print_html_globals(d):
	global anonymous
	if d["anonymous"] == "on":
		anonymous = False
	else: anonymous = False
	
	print("<table cellspacing=\"3\" width=\"100%\"><tr><th width=\"125\">NAME</th><th width=\"100\">PRICE</th><th width=\"70\">%DAY</th></tr>")
	for v in d["globals"]:
		if 'US' in v["real_name"]:
			price = colorize_html_value(v["c"],"dollar",False,anonymous)
		else :
			price = colorize_html_value(v["c"],"none",False,anonymous)
		pc_day = colorize_html_value(v["cp_fix"],"percent",True,anonymous)
		print("<tr><td width=70>" + v["real_name"] + "</font>" + price + pc_day )
	for v in d["cryptos"]:
		if v["real_name"] == "Ripple":
			price = colorize_html_value(v["c"]*1200,"euro",False,anonymous)
			pc_day = colorize_html_value(v["o"],"percent",True,anonymous)
			print("<tr><td width=70>" + v["real_name"] + "</font>" + price + pc_day)
		else:
			price = colorize_html_value(v["c"],"crypto",False,anonymous)
			pc_day = colorize_html_value(v["o"],"percent",True,anonymous)
			print("<tr><td width=70>" + v["real_name"] + "</font>" + price + pc_day)
	print("</table>")


def print_html_values(d):
	global anonymous
	if d["anonymous"] == "on":
		anonymous = True
	else: anonymous = False
	print("<table cellspacing=\"3\" width=\"100%\"><tr><th width=\"150\">NAME</th><th width=\"70\">INVEST</th><th width=\"70\">PRU</th><th width=\"70\">PRICE</th><th width=\"70\">%DAY</th><th width=\"70\">DAY</th><th width=\"70\">TOTAL</th><th width=\"70\">%TOTAL</th>\n</tr>")
	for v in d["values"]:
		pru = colorize_html_value(v["pru"],"euro",False,anonymous)
		price = colorize_html_value(v["c"],"euro",False,False)
		pc_day = colorize_html_value(v["cp_fix"],"percent",True,False)
		day = colorize_html_value(v["c_fix"]*v["nb"],"euro",True,anonymous)
		total = colorize_html_value(v["nb"]*(v["c"]-v["pru"]),"euro",True,anonymous)
		invest = colorize_html_value(v["nb"]*v["pru"],"euro",False,anonymous)
		pc_total = colorize_html_value(100 * (v["nb"]*(v["c"]-v["pru"])) / (v["nb"]*v["pru"]),"percent",True,False)
		name = "<tr>\n\t<td width=\"70\">" + str('%-8s' % (v["real_name"])) + "</font></td>"
		print(name + invest + pru + price + pc_day + day + total + pc_total +"\n</tr>")
	print("</table>")
