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
		
alreadyDone = []
user_agent = ("reddit trending words by walter michelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)
sub = 'nfl'
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


common = 'the be to of and a in that have i it for not on with he as you do at word this but his by'
common = common + ' from they we say her she or an will my one all would there their what word'
common = common + ' so up out if about who get which go me when make can like time no just'
common = common + ' him know take word people into year your good some could them see other than then'
common = common + ' now look only come its over think also back after use two how our work first'
common = common + ' well way even new want because any these give day most us'
common = common + ' oh thats is was are im thru has too lol here someone were very id cant'
common = common + ' 1 2 3 4 5 6 7 8 9 0 . .. ... .... .....'
common = common + ' become dont has more ever said ive every off sure had didnt same much'
common = common + ' put many ill did'

common_words = []
common_words = common.split()

global tempword
tempword = ''
global tempobject
tempobject = countObj('', 0)

obj = []

timesrun = 0
timestarted = str(datetime.now())

while True:	
	for x in range (0 , 4):
		sys.stdout.write('\r....')
		sys.stdout.write('\r' + 'loading' + '.' * x)
		sys.stdout.flush()
		time.sleep(.1)
	
	anynew = False
	samechecker = False 
	addchecker = False
	index = 0
	indextoadd = 0
	all_comments = r.get_comments(all, limit=None)
	
	for comment in all_comments:
		if comment.body not in alreadyDone:
			anynew = True
			alreadyDone.append(comment.body)
	 		tempString = comment.body
			words = []
			words = tempString.split()
			
			for x in words:
				x = x.lower()
				for c in string.punctuation:
					x = x.replace(c,"")
				if x:
					if x not in common_words:
						if len(x) < 18:
							if len(x) > 1:
								tempword = x
								samechecker = False
								addchecker = False
								index = 0
								if len(obj) == 0 or len(obj) == 1:
									print str(len(obj)) + ' items in obj... populating'
									addchecker = True
								else:
									print 'PRINTING OBJ LIST OF SIZE ' + str(len(obj))
									
									for thing in range (0, 20):
										try:
											print obj[thing]
										except:
											pass
									print '**************************'
									for thing in obj:
										if tempword == thing.word:
											samechecker = True
											indextoadd = index
											temp = countObj(thing.word, thing.count + 1)
											addchecker = False
										index = index + 1
								if not samechecker:
									addchecker = True
								if samechecker:
									print 'duplicate! incrementing!'
									obj[indextoadd] = temp
									obj.sort()
								if addchecker:
									print 'new word! adding!'
									temp = countObj(x, 0)
									obj.append(temp)
									obj.sort()
								
	output = 'Top 3 trending words on /r/' + sub + ' since ' + timestarted
	output += '\n'
	obj.sort()
	for x in range(0, 3):
		try:
			output += obj[x].__str__()
			output += '\n'
		except: 
			print 'errors!!!!!!!!!!!!!!****'
			pass
			
		
	if anynew:
		timesrun = timesrun + 1
	print 'PROGRAM RAN ' + str(timesrun) + ' times!!!!'
	print output
	#api.update_status(output)

	
	if timesrun%5 == 0:
		api.update_status(output)
	time.sleep(30)		