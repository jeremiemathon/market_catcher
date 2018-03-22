#!/usr/bin/python

import bs4
import urllib.request

def add_boursorama_url(value):
	position = value.find("href")
	return value[:position+6] + "http://www.boursorama.com" + value[position+6:]


def parse_boursorama_forum(value):
	url = "https://www.boursorama.com/bourse/forum/1rEPALCLS/"
	headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36' }
	req = urllib.request.Request(url, None, headers)
	u = urllib.request.urlopen(req)
	soup = bs4.BeautifulSoup(u,'html.parser')
	print("<table class=\"boursorama\"><th height=20 class=\"boursorama_th\">BOURSORAMA</th><tr><td valign=\"top\">")
	for subject in soup.findAll('div',attrs={"class":u"c-block__body"}):
		for data in subject.findAll('a', attrs={"class":u"c-link  c-link--regular c-link--neutral c-link--bold c-link--no-underline"}):
			print(data)
			#html = str(subject.find('a')).encode('ASCII', 'xmlcharrefreplace').decode('ascii')
			#html_boursorama = add_boursorama_url(html)
			print(html_boursorama + "<br>")
		#print(str(subject).encode('ASCII', 'ignore').decode('ascii'))
	print("</td></tr></table>")

if __name__ == '__main__':
	parse_boursorama_forum("ALCLS")
