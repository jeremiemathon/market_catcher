import tweepy
import datetime
import bs4
import re

_link = re.compile(r'(?:(https://)|(www\.))(\S+\b/?)([!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]*)(\s|$)', re.I)
def convertLinks(text): 
    def replace(match):
        groups = match.groups()
        protocol = groups[0] or ''  # may be None
        www_lead = groups[1] or ''  # may be None
        return '<a href="https://{1}{2}" rel="nofollow">{0}{1}{2}</a>{3}{4}'.format(
            protocol, www_lead, *groups[2:])
    return _link.sub(replace, text)


def twitter():
	ret = ""
	consumer_key = "DMWAx7FHGFjZQfx21DhSzJkIT"
	consumer_secret = "ddfJbY7vz2mzqrhMQWgJySn73pqyMfN8EWoB44VqtCUMKZe2Ch"
	access_token = "518453941-bTtdPih06bEPrwzrJUowhOi3XxSWY2za5mElbGQU"
	access_token_secret = "5cGtJb8HtmJS9AcIl2ghVV4nk3gKrQKUIHbK1VDOSZ3YN"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	search = api.search("Cellectis", count=25)
	print("<table class=\"twitter\"><th colspan=\"2\" class=\"twitter_th\">TWITTER</th>")
	for i in search:
		text = i.text.encode('ascii','xmlcharrefreplace').decode('ascii')
		#text = i.text.replace(u"\u2026", "...").replace(u"\u2019", "'").replace(u"\xe9", "e").replace(u"\u201c","\"").replace(u"\u201d","\"").replace(u"\xe7", "c")
		if i.created_at.day == datetime.datetime.now().day:
			# print(dir(i))
			print("<tr><td><font class=\"twitter_today\">" + str(i.created_at)[:-9] + " @"  + str(i.user.screen_name) + "</font></td><td>" + convertLinks(text) + "</td></tr>")
		else: print("<tr><td>" + str(i.created_at)[:-9] + " @" + str(i.user.screen_name) + "</td><td>" + text + "</td></tr>")
	print("</table>")
