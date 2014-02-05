import praw
import time
import tweepy
import urllib

seattleCount = 0
denverCount = 0
alreadyDone = []
user_agent = ("NFL superbowl mention counter by walter michelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)
rNFL = r.get_subreddit('nfl')

consumer_key = 'Ud6dfcMuiQGV2uh6kpkDng'
consumer_secret = 'OsArxd12XeLXrCzCqJKf1I9fhIZNWAGFeq7D7o2uM'

access_token = '2329099704-SHifsHTY91SH1UckrlcK3lpWOnHyjiROwZC4hqA'
access_secret = 'nWomFXS2kzblfbv1VHQ06mB4CHB9ht6LrzxCLPTaMQvwu'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

api.update_status('hello world')




while True:	
	
	tempString = ''

	all_comments = r.get_comments(rNFL, limit=None)

	for comment in all_comments:
		if comment.body not in alreadyDone:	 
			tempString = comment.body
			words = []
			words = tempString.split()
	
			for word in words:
				word = word.lower()
				if 'seattle' in word or 'seahawks' in word:
					print 'SEATTLE'
					seattleCount = seattleCount + 1
				if 'denver' in word or 'broncos' in word:
					print 'DENVER'
					denverCount = denverCount + 1 

			alreadyDone.append(comment.body)


	tempString = 'Total times Seattle mentioned: '
	tempString += str(seattleCount)
	print tempString
	tempString = ''

	tempString = 'Total times Denver mentioned: '
	tempString += str(denverCount)
	print tempString
	
	time.sleep(10)



		