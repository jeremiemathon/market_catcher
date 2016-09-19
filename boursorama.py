import bs4
import urllib.request

def parse_boursorama_forum(value):
	url = "http://www.boursorama.com/forum-cellectis-1rEPALCLS-1"
	headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36' }
	req = urllib.request.Request(url, None, headers)
	u = urllib.request.urlopen(req)
	soup = bs4.BeautifulSoup(u,'html.parser')
	print(str(soup.find('td',attrs={"class":u"tdv-sujet"})).encode('ASCII', 'ignore').decode('ascii'))

