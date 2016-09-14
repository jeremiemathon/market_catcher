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

	search = api.search("Cellectis", count=10)
	print("<br><br>")
	for i in search:
		text = i.text.replace(u"\u2026", "...").replace(u"\u2019", "'").replace(u"\xe9", "e")
		print(str(i.created_at)[:-9] + "\t" + text + "<br>")
