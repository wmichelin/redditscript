import praw
import time
from datetime import datetime
import tweepy
import string 
import sys

class countObj:
	global word
	global count
	word = ''
	count = 0
	
	def __init__(self, word, count):
		self.word = word
		self.count = count

	def __str__(self):
		temp = ''
		temp += self.word
		temp += ' count: '
		temp += str(self.count)
		return temp
		
	def setcount(num):
		self.count = num
		
	def __lt__(self, other):
		return (self.count > other.count)
		
	def copy(self):
		temp = countObj(self.word, (self.count+1))
		return temp
		
	def getCount(self):
		return count
			
		
alreadyDone = []
user_agent = ("reddit trending words by walter michelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)
sub = 'gaming'
all = r.get_subreddit(sub)

consumer_key = 'Ud6dfcMuiQGV2uh6kpkDng'
consumer_secret = 'OsArxd12XeLXrCzCqJKf1I9fhIZNWAGFeq7D7o2uM'

access_token = '2329099704-SHifsHTY91SH1UckrlcK3lpWOnHyjiROwZC4hqA'
access_secret = 'nWomFXS2kzblfbv1VHQ06mB4CHB9ht6LrzxCLPTaMQvwu'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def tweet(self, input):
	api.update_status(input)

#api.update_status('hello world')

common = 'the be to of and a in that have i it for not on with he as you do at word this but his by'
common = common + ' from they we say her she or an will my one all would there their what word'
common = common + ' so up out if about who get which go me when make can like time no just'
common = common + ' him know take word people into year your good some could them see other than then'
common = common + ' now look only come its over think also back after use two how our work first'
common = common + ' well way even new want because any these give day most us'
common = common + ' oh thats is was are im thru has too lol here someone were very id cant'
common = common + ' 1 2 3 4 5 6 7 8 9 0 . .. ... .... .....'
common = common + ' become dont'

common_words = []
common_words = common.split()

obj = []
duplicate = []

timesrun = 0
timestarted = str(datetime.now())

while True:	
	for x in range (0 , 4):
		sys.stdout.write('\r....')
		sys.stdout.write('\r' + 'loading' + '.' * x)
		sys.stdout.flush()
		
	checker = False 
	dupechecker = False
	all_comments = r.get_comments(all, limit=None)
	anynew = False
	
	for comment in all_comments:
		if comment.body not in alreadyDone:
			anynew = True
			alreadyDone.append(comment.body)
	 		tempString = comment.body
			words = []
			words = tempString.split()
			

			#checking words from comments against previous words
			i = 0
			for word in words:
				for c in string.punctuation:
					word = word.replace(c,"")
				word = word.lower()
				word = word.strip()
				if word not in common_words:	
					print word
					checker = False
					for x in obj:
						if x.word is word:
							checker = True
					if checker:
						j = 0
						dupechecker = False
						for thing in duplicate:
							if thing.word is word:
								dupechecker = True
								tempcount = thing.count
								temp = duplicate[j].copy()
								temp.setcount(tempcount + 1)
								duplicate[j] = temp
							j = j+1
						if not dupechecker:
							temp = x.copy()
							duplicate.append(temp)
					else:
						temp = countObj(word, 0)
						obj.append(temp)
					
					
		

	print 'size of object array: ' + str(len(obj))
	print 'size of DUPLICATE array: ' + str(len(duplicate))
	print '****************SORTING AND PRINTING DUPLICATES******************'
	duplicate.sort()
	for thing in duplicate:
		print thing
		
	output = 'Top 5 trending words on /r/' + sub + ' since ' + timestarted
	output += '\n'
	for x in range (0, 5):
		output += duplicate[x].word + ' has been mentioned ' + str(duplicate[x].count + 1) + ' times.'
		output += '\n'
	print str(timesrun)
	print output
	if anynew:
		timesrun =  timesrun + 1
		
	if (timesrun%10 == 0):
		tweet(output)
		print '*********** NEW TWEET ****************'
		
	
	time.sleep(10)
	
	
	
		
	



		