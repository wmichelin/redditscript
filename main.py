import praw

user_agent = ("comment scraper by /u/wmichelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)

all_comments = r.get_comments('nfl')

print 'before for each loop'

for comment in all_comments:
	tempString = comment.body
	words = []
	words = tempString.split()
	
	for word in words:
		word = word.lower()
		if 'the' in word:
			print 'found!'
		