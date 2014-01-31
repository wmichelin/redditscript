import praw
import time

seattleCount = 0
denverCount = 0
alreadyDone = []
user_agent = ("NFL superbowl mention counter by walter michelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)

rNFL = r.get_subreddit('nfl')

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
				if 'seattle' in word:
					print 'SEATTLE'
					seattleCount = seattleCount + 1
				if 'denver' in word:
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
	
	time.sleep(300)



		