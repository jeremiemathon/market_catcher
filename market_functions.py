import json
import bs4
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
		return (0,0,0,0,0,)
		link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
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
		try:
			cp_fix = float(info["cp_fix"].replace(',','')) # percent from fix
		except:
			cp_fix = float(0)
		try:
			c_fix = float(info["c_fix"].replace(',','')) # difference from fix
		except:
			c_fix = float(0)
		return (t,c,fix,cp_fix,c_fix)
	except:
		raise
		return (0,0,0,0,0,0,0,0)

def fetchMarket2(symbol):
	url = "https://www.boursorama.com/cours/1rEPALCLS/"
	link = "http://www.boursorama.com/cours.phtml?symbole="
	url = link+"%s" % (symbol)
	headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36' }
	req = urllib.request.Request(url, None, headers)
	u = urllib.request.urlopen(req)
	soup = bs4.BeautifulSoup(u,'html.parser')
        #print("<table class=\"boursorama\"><th height=20 class=\"boursorama_th\">BOURSORAMA</th><tr><td valign=\"top\">")
        #for subject in soup.findAll('div',attrs={"class":u"fv-name"}):
	for subject in soup.findAll('table',attrs={"class":u"info-valeur list"}):
		#print(subject.findAll('span',attrs={"class":u"cotation"}))
		subject3 = subject.findAll('span',attrs={"class":u"cotation"})
		subject2 = subject.findAll('span')
		#print(subject2)
		#print("====================")
		#print(subject2[5])
		#print(subject2[5].string)
		c = float(subject2[0].string.replace(" EUR","").replace(" Pts","").replace("USD","").replace(" ","").replace("(c)","").replace("Pts","").replace("(u)","").replace("(s)",""))
		cp_fix = float(subject2[2].string.replace("USD","").replace("%","").replace(" ","").replace("ND","0").replace("Pts",""))
		#print(symbol,subject2[0].string)
		#print(symbol,subject2[1].string)
		#print(symbol,subject2[2].string)
		#print(symbol,subject2[3].string)
		#print(symbol,subject2[4].string)
		#print(symbol,subject2[5].string)
		#print(symbol,subject2[6].string)
		#print(symbol,subject2[7].string)
		#print(symbol,subject2[8].string)
		#print(symbol,subject2[9].string)
		#print(symbol,subject2[10].string)
		#print(symbol,subject2[11].string)
		#print(symbol,subject2[12].string)
		#print(symbol,subject2[13].string)
		#print("<br>\r\n")
		c_fix = float(subject2[11].string.replace("EUR","").replace("USD","").replace(" ","").replace("(c)","").replace("ND","0").replace("Pts",""))
		#print(c,c_fix)
		#print("====================================================")
		#print(c, cp_fix, c_fix, c - c_fix)
		#print(soup.findAll('meta')[13]["content"])
		#print(str(subject).encode('ASCII', 'ignore').decode('ascii'))
	return (0,c,0,cp_fix,c - c_fix)

def fetchMarket3(symbol):
	url = "https://www.boursorama.com/cours/" + "%s" % (symbol) + "/"
	headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36' }
	req = urllib.request.Request(url, None, headers)
	u = urllib.request.urlopen(req)
	soup = bs4.BeautifulSoup(u,'html.parser')
	for subject in soup.findAll('div', attrs={"class":u"c-faceplate__company"}):
		c = subject.findAll('span',attrs={"class":u"c-instrument c-instrument--last"})[0].string.replace(" ","")
		cp_fix = subject.findAll('span',attrs={"class":u"c-instrument c-instrument--variation"})[0].string.replace("%","").replace(" ","")
	c_fix = soup.findAll('span',attrs={"class":u"c-instrument c-instrument--previousclose"})[0].string.replace(" ","")

	return (0,float(c),0,float(cp_fix),float(c) - float(c_fix))

def fetchCrypto(symbol,returnsymbol):
	try:
		link = "https://api.kraken.com/0/public/Ticker?pair="
		url = link+"%s" % (symbol)
		headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}
		req = urllib.request.Request(url, None, headers)
		u = urllib.request.urlopen(req)
		print(url)
		data = json.loads(u.read().decode(u.info().get_param('charset') or 'utf-8'))
		c =  float(data["result"][returnsymbol]["c"][0])
		o =  float(((c / float(data["result"][returnsymbol]["o"])) - 1)) * 100
		return (c,o)
		
	except:
		raise
		return (0)

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
		t, c, fix, cp_fix, c_fix = fetchMarket3(value["name"])
		json_data_file["values"][num]["t"] = t
		json_data_file["values"][num]["c"] = c
		json_data_file["values"][num]["fix"] = fix
		json_data_file["values"][num]["cp_fix"] = cp_fix
		json_data_file["values"][num]["c_fix"] = c_fix
		if "yes" in json_data_file["values"][num]["countable"]:
			json_data_file["total"] = json_data_file["total"] + json_data_file["values"][num]["c"] * json_data_file["values"][num]["nb"]
		if "yes" in json_data_file["values"][num]["countable"]:
			json_data_file["total_fix"] = json_data_file["total_fix"] + json_data_file["values"][num]["c_fix"] * json_data_file["values"][num]["nb"]
		if "yes" in json_data_file["values"][num]["countable"]:
			json_data_file["total_pru"] = json_data_file["total_pru"] + json_data_file["values"][num]["pru"] * json_data_file["values"][num]["nb"]
		num += 1
	
	num=0
	for global_value in json_data_file["globals"]:
		t, c, fix, cp_fix, c_fix = fetchMarket(global_value["name"])
		json_data_file["globals"][num]["cp_fix"] = cp_fix
		json_data_file["globals"][num]["c"] = c
		num +=1
	num=0
	for crypto_value in json_data_file["cryptos"]:
		c, o = fetchCrypto(crypto_value["name"],crypto_value["return_name"])
		json_data_file["cryptos"][num]["c"] = c
		json_data_file["cryptos"][num]["o"] = o
		num+=1

#	print(json.dumps(json_data_file, sort_keys=True, indent=4))
	return json_data_file

def myWallet():
	total_fix = 0 #total amount of eur at the beginning of the day
	total_price = 0 #total amount of eur at time t
