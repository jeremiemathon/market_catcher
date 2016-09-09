def colorize_print_value(d):
	return str(d)


def print_table_values(d):
	html = str('%-15s' % ('NAME') + '%-8s' % ('PRU') + '%-8s' % ('PRICE') + '%-8s' % ('%DAY') + '%-8s' % ('DAY') +'%-8s' % ('TOTAL'))
	for v in d["values"]:
		#pru = colorize_print_value(v["pru"])
		pru = str('%-8.2f' % (v["pru"]))
		price = colorize_print_value(v["c"])
		price = str('%-8.2f' % (v["c"]))
		pc_day = colorize_print_value(v["cp_fix"])
		day = colorize_print_value(v["c_fix"]*v["nb"])
		total = colorize_print_value(v["nb"]*(v["c"]-v["pru"]))
		html = str('%-15s' % (v["name"]) +  pru +  price + pc_day + day + total)
	return html


def build_page(d):
	html = "<html><meta http-equiv=\"refresh\" content=\"5\"><Title>Hello World</Title>" + print_table_values(d) + "</html>"
	return html
