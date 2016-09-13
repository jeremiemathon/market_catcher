import tweepy
import datetime
import bs4

def twitter():
	ret = ""
	consumer_key = "DMWAx7FHGFjZQfx21DhSzJkIT"
	consumer_secret = "ddfJbY7vz2mzqrhMQWgJySn73pqyMfN8EWoB44VqtCUMKZe2Ch"
	access_token = "518453941-bTtdPih06bEPrwzrJUowhOi3XxSWY2za5mElbGQU"
	access_token_secret = "5cGtJb8HtmJS9AcIl2ghVV4nk3gKrQKUIHbK1VDOSZ3YN"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	#        alcls_search = tweepy.api.search(api,"$alcls",10)
	alcls_search = api.search("$alcls")
	clls_search = api.search("cellectis")
	print("<br><br>")
	for i in clls_search:
		if i.created_at.day == datetime.datetime.now().day:
			#ret = ret + '<br>' + i.text.replace("\n","")
			i.text = i.text + "<br>"
		#	print(i.text.encode('utf-8'))
			print(str(i.text.encode('utf-8')).replace("b'","").replace("'",""))
			#print(printable[:100] + '\n' + printable[100:])
#	print(bs4.BeautifulSoup(ret.encode('utf-8').decode('utf-8','ignore'),'html.parser').prettify('utf-8'))

