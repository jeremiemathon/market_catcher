import json
import urllib.request

class color:
	#POSITIVE = '\033[42m'
	#NEGATIVE = '\033[41m'
	POSITIVE = '\033[30;42m'
	NEGATIVE = '\033[1;30;41m'
	MIDDLE = '\033[1;30;43m'
	BOLD = '\033[1m'
	END = '\033[0m'

def fetchMarket(symbol):
	try:
		lo=0
		hi=0
		op=0
		link = "https://www.google.com/finance/info?infotype=infoquoteall&q="
		url = link+"%s" % (symbol)
		headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36' }
		req = urllib.request.Request(url, None, headers)
		u = urllib.request.urlopen(req)
		data = json.loads(u.read().decode(u.info().get_param('charset') or 'utf-8')[3:])
		info = data[0]
		t = str(info["lt"])    # time stamp
		c = float(info["l"].replace(',',''))    # current price (previous trading day)
		#lo = float(info["lo"].replace(',',''))   # stock price in pre-market (after-hours)
		#hi = float(info["hi"].replace(',',''))  # highest stock price
		#op = float(info["op"].replace(',',''))  # open stock price
		fix = float(info["pcls_fix"].replace(',','')) # fix
		cp_fix = float(info["cp_fix"].replace(',','')) # percent from fix
		c_fix = float(info["c_fix"].replace(',','')) # difference from fix
		return (t,c,fix,cp_fix,c_fix)
	except:
		raise
		return (0,0,0,0,0,0,0,0)



def read_data_file():
	with open('stocks.json') as data_file:
		return json.load(data_file)
		

def fulfill_data_file():
	json_data_file = read_data_file()
	json_data_file["total_fix"]=0
	json_data_file["total"]=0
	json_data_file["total_pru"]=0
	
	num=0 #id of the value
	
	for value in json_data_file["values"]:
		t, c, fix, cp_fix, c_fix = fetchMarket(value["name"])
		json_data_file["values"][num]["t"] = t
		json_data_file["values"][num]["c"] = c
		json_data_file["values"][num]["fix"] = fix
		json_data_file["values"][num]["cp_fix"] = cp_fix
		json_data_file["values"][num]["c_fix"] = c_fix
		json_data_file["total"] = json_data_file["total"] + json_data_file["values"][num]["c"] * json_data_file["values"][num]["nb"]
		json_data_file["total_fix"] = json_data_file["total_fix"] + json_data_file["values"][num]["fix"] * json_data_file["values"][num]["nb"]
		json_data_file["total_pru"] = json_data_file["total_pru"] + json_data_file["values"][num]["pru"] * json_data_file["values"][num]["nb"]
		num += 1
	
	num=0
	for global_value in json_data_file["globals"]:
		t, c, fix, cp_fix, c_fix = fetchMarket(global_value["name"])
		json_data_file["globals"][num]["cp_fix"] = cp_fix
		json_data_file["globals"][num]["c"] = c
		num +=1

	return json_data_file

def myWallet():
	total_fix = 0 #total amount of eur at the beginning of the day
	total_price = 0 #total amount of eur at time t
