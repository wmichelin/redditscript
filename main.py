#written by Walter Michelin TCNJ Class of '15 CS Dept
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
#reddit autentication
user_agent = ("reddit trending words by walter michelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)
sub = 'all'
all = r.get_subreddit(sub)
#twitter authentication using OAuth
consumer_key = 'Ud6dfcMuiQGV2uh6kpkDng'
consumer_secret = 'OsArxd12XeLXrCzCqJKf1I9fhIZNWAGFeq7D7o2uM'

access_token = '2329099704-SHifsHTY91SH1UckrlcK3lpWOnHyjiROwZC4hqA'
access_secret = 'nWomFXS2kzblfbv1VHQ06mB4CHB9ht6LrzxCLPTaMQvwu'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#commonly used words
common = 'the be to of and a in that have i it for not on with he as you do at word this but his by'
common = common + ' from they we say her she or an will my one all would there their what word'
common = common + ' so up out if about who get which go me when make can like time no just'
common = common + ' him know take word people into year your good some could them see other than then'
common = common + ' now look only come its over think also back after use two how our work first'
common = common + ' well way even new want because any these give day most us'
common = common + ' oh thats is was are im thru has too lol here someone were very id cant'
common = common + ' 1 2 3 4 5 6 7 8 9 0 . .. ... .... .....'
common = common + ' become dont has more ever said ive every off sure had didnt same much'
common = common + ' put many ill did really been still why though those theyre am right'
common = common + ' should never need doesnt find youre great going hes shes got before'
common = common + ' better something is isnt another being around lot a while'
common = common + ' thing actually anything doing love while able things where yeah used'
common = common + ' wont looks simple does using might always maybe have having happen'
common = common + ' thanks since enough through may pretty probably please try both few'
common = common + ' made few ago case guy '

common_words = []
#list of commonly used words
common_words = common.split()

#used to access word from within different loops
global tempword
tempword = ''

#master list for all unique words 
obj = []

#counters
timesrun = 0
timestarted = str(datetime.now())

#infinite loop
while True:	
	#loading statement
	for x in range (0 , 4):
		sys.stdout.write('\r....')
		sys.stdout.write('\r' + 'loading' + '.' * x)
		sys.stdout.flush()
		time.sleep(.1)
	#checkers
	anynew = False
	samechecker = False 
	addchecker = False
	index = 0
	indextoadd = 0
	#access comments
	all_comments = r.get_comments(all, limit=None)
	#goes through each comment, makes sure it hasnt been seen before
	for comment in all_comments:
		if comment.body not in alreadyDone:
			#anynew is true if 
			anynew = True
			alreadyDone.append(comment.body)
	 		tempString = comment.body
			words = []
			words = tempString.split()
			#parses each word individually
			for x in words:
				x = x.lower()
				#removes all punctuation
				for c in string.punctuation:
					x = x.replace(c,"")
				if x:
					#checks word against commonly used words... still imperfect
					if x not in common_words:
						#checks size of word
						if len(x) < 18:
							if len(x) > 1:
								tempword = x
								samechecker = False
								addchecker = False
								index = 0
								#adds first two words to empty list
								if len(obj) == 0 or len(obj) == 1:
									print str(len(obj)) + ' items in obj... populating'
									addchecker = True
								else:
									#for debug purposes lists top 20 duplicated words
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
									#debug purposes
									print 'duplicate! incrementing!'
									obj[indextoadd] = temp
									obj.sort()
								if addchecker:
									#debug purposes
									print 'new word! adding!'
									temp = countObj(x, 0)
									obj.append(temp)
									obj.sort()
	#shows output that will be tweeted every X times the program runs							
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
		try:
			#tweets
			api.update_status(output)
			print '****PRINTED NEW TWEET****'
			time.sleep(10)
		except:
			pass
	time.sleep(30)		