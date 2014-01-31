import praw

user_agent = ("comment scraper by /u/wmichelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)

all_comments = r.get_comments('nfl')
seattleCount = 0
denverCount = 0

for comment in all_comments:
	tempString = comment.body
	words = []
	words = tempString.split()
	
	for word in words:
		print word
		tempString = ''
		word = word.lower()
		if 'seattle' in word:
			print 'SEATTLE'
			seattleCount = seattleCount + 1
		if 'denver' in word:
			print 'DENVER'
			denverCount = denverCount + 1 


tempString = 'Times seattle mentioned: '
tempString += str(seattleCount)
print tempString
tempString = ''

tempString = 'Times denver mentioned: '
tempString += str(denverCount)
print tempString



		