import praw
import time
import tweepy
import string 
import sys

class countObj:
	word = ''
	global count
	count = 0
	
	def __init__(self, word):
		self.word = word
		self.count = 0

	def __str__(self):
		temp = ''
		temp += self.word
		temp += ' count: '
		temp += str(self.count)
		return temp
		
	def __lt__(self, other):
		return (self.count > other.count)
		
	def get(self):
		return self
			
	def increment(self):
		global count
		count += 1
		#print '*******INCREMENTING********'
		#print count
		
alreadyDone = []
user_agent = ("reddit trending words by walter michelin"
			  "github.com/wmichelin")

r = praw.Reddit(user_agent=user_agent)
all = r.get_subreddit('all')

consumer_key = 'Ud6dfcMuiQGV2uh6kpkDng'
consumer_secret = 'OsArxd12XeLXrCzCqJKf1I9fhIZNWAGFeq7D7o2uM'

access_token = '2329099704-SHifsHTY91SH1UckrlcK3lpWOnHyjiROwZC4hqA'
access_secret = 'nWomFXS2kzblfbv1VHQ06mB4CHB9ht6LrzxCLPTaMQvwu'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#api.update_status('hello world')

common = 'the be to of and a in that have i it for not on with he as you do at word this but his by'
common = common + ' from they we say her she or an will my one all would there their what word'
common = common + ' so up out if about who get which go me when make can like time no just'
common = common + ' him know take word people into year your good some could them see other than then'
common = common + ' now look only come its over think also back after use two how our work first'
common = common + ' well way even new want because any these give day most us'
common = common + ' oh thats is was are im thru has too lol here someone were very id cant'
common = common + ' 1 2 3 4 5 6 7 8 9 0 . .. ... .... .....'

common_words = []
common_words = common.split()

obj = []
duplicate = []

while True:	
	for x in range (0 , 4):
		sys.stdout.write('\r....')
		sys.stdout.write('\r' + 'loading' + '.' * x)
		sys.stdout.flush()
		time.sleep(.2)
		
		
	tempString = ''
	checker = False 
	all_comments = r.get_comments(all, limit=None)

	for comment in all_comments:
		if comment.body not in alreadyDone:
			alreadyDone.append(comment.body)
	 		tempString = comment.body
			words = []
			words = tempString.split()
	
			for word in words:
				for c in string.punctuation:
					word = word.replace(c,"")
				word = ''.join(word.split())
				if word is not '':
					if len(word) > 1:
						if len(word) < 18:
							temp = countObj('')
							checker = False
							word = word.lower()
							print word

							if word not in common_words:
								for thing in obj:
									if word is thing.word:
										print word
										checker = True
										print '*************DUPLICATE!!!!!!**********' + word
										thing.get().increment()
									
								if checker == False:
										temp = countObj(word) 
										obj.append(temp)
										tempstr = temp.__str__()
										print 'appending! ' + tempstr
								
		#for thing in obj:
	#print 'PRINT OBJECT ARRAY HERE'
	for thing in obj:
		if thing.count > 0:
			if thing not in duplicate:
				duplicate.append(thing)
				print thing.word
				print thing.count
	
	if len(duplicate) > 0:	
		duplicate.sort()
	
	
	print '*****************PRINTING DUPLICATE!!!!!!************************'
	print str(len(duplicate))
	for item in duplicate:
		print item.word
		print item.count
	
	
	
	
	print 'sleeping'
	time.sleep(15)
	
	



		