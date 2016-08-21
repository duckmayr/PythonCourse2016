"""This script's getTargetData function will provide, for any target Twitter user, eight pieces of information: their most active follower, their most popular follower, their most active layman friend, their most active expert friend, their most active celebrity friend, the most active user of their followers and their followers' followers (excluding celebrities), and the most popular of their followers and their followers' followers (excluding celebrities). For the purposes of this script, the most active Twitter user among a group of users is the one with the most total Tweets, a layman user is one with less than 100 followers, an expert user is one with between 100 and 1000 followers (inclusive), and a celebrity user is one with more than 1000 followers. The execution of this script requires the tweepy and time modules, and that its user have a Twitter API account."""

import tweepy
import time
	
def classifyUser(userID, api):
	"""Given a Twitter user's handle, returns the user's classification as a layman, expert, or celebrity."""
	if api.get_user(userID).followers_count > 1000: return 'celebrity'
	if api.get_user(userID).followers_count >= 100: return 'expert'
	return 'layman'
	
def getMost(userList, kind, api):
	"""Given a list of Twitter user IDs, returns the handle for the user with the highest value for the requested statistic."""
	userDict = {}
	for userID in userList:
		not_finished = True
		while not_finished:
			try:
				tmp_user = api.get_user(userID)
				if kind == 'active': userDict[userID] = tmp_user.statuses_count
				if kind == 'popular': userDict[userID] = tmp_user.followers_count
				not_finished = False
			except tweepy.error.RateLimitError: time.sleep(1)
			# I used my own account as the target to test this code. There are two followers of my followers with protected tweets, which causes an authorization error, so we have be able to skip them or the loop will go on forever without result:
			except tweepy.TweepError: 
				print userID
				not_finished = False
	return api.get_user(userDict.keys()[userDict.values().index(max(userDict.values()))]).screen_name.encode('utf-8')
	
def getMostActive(userList, api):
	"""Given a list of Twitter user handles, returns the handle for the user with the most total Tweets."""
	return getMost(userList, 'active', api)

def getMostPopular(userList, api):
	"""Given a list of Twitter user handles, returns the handle for the user with the most followers."""
	return getMost(userList, 'popular', api)
	
def getPeopleDict(user, kind, api):
	if type(user) != tweepy.models.User: user = api.get_user(user)
	if kind == 'friends': peopleDict = {'Celebrities':[],'Experts':[],'Laymen':[],'All':api.friends_ids(user.id)}
	if kind == 'followers': peopleDict = {'Celebrities':[],'Experts':[],'Laymen':[],'All':api.followers_ids(user.id)}
	for person in peopleDict['All']:
		not_finished = True
		while not_finished:
			try: 
				status = classifyUser(person, api)
				if status == 'celebrity': peopleDict['Celebrities'].append(person)
				if status == 'expert': peopleDict['Experts'].append(person)
				if status == 'layman': peopleDict['Laymen'].append(person)
				not_finished = False
			except tweepy.RateLimitError: time.sleep(1)
			except tweepy.TweepError: 
				print person
				not_finished = False
	return peopleDict
	
def getMore(population, kind, api):
	endList = []
	for person in (population['Laymen'] + population['Experts']):
		not_finished = True
		while not_finished:
			try: 
				if kind == 'friends': endList.extend(api.friends_ids(person))
				if kind == 'followers': endList.extend(api.followers_ids(person))
				not_finished = False
			except tweepy.RateLimitError: time.sleep(1)
			except tweepy.TweepError: 
				print person
				not_finished = False
	return endList

def getTargetData(target):
	"""Takes a target Twitter user's handle as a string and returns their most active follower, their most popular follower, their most active layman friend, their most active expert friend, their most active celebrity friend, the most active user of their followers and their followers' followers (excluding celebrities), and the most popular of their followers and their followers' followers (excluding celebrities)."""

	auth = tweepy.OAuthHandler(input('Please provide your consumer key: '),input('Please provide your consumer secret: ')) 
	auth.set_access_token(input('Please provide your access token: '),input('Please provide your access token secret: ')) 
	api = tweepy.API(auth)
	target = api.get_user(target)
	targetFriends = getPeopleDict(target, 'friends', api)
	targetFollowers = getPeopleDict(target, 'followers', api)
	followersFollowers = getMore(targetFollowers, 'followers', api)
	friendsFriends = getMore(targetFriends, 'friends', api)
	targetInfo = [getMostActive(targetFollowers['All'], api), getMostPopular(targetFollowers['All'], api), getMostActive(targetFriends['Laymen'], api), getMostActive(targetFriends['Experts'], api), getMostActive(targetFriends['Celebrities'], api), getMostPopular(targetFriends['All'], api), getMostActive(followersFollowers, api), getMostActive(friendsFriends, api)]
	return "The target's most active follower is %s, most popular follower is %s, most active layman friend is %s, most active expert friend is %s, most active celebrity friend is %s, most popular friend is %s, most active extended follower is %s, and most active extended friend is %s." %(targetInfo[0],targetInfo[1],targetInfo[2],targetInfo[3],targetInfo[4],targetInfo[5],targetInfo[6],targetInfo[7])
#	
## I used these functions to answer the homework questions for my account ('jb_duckmayr'):
## Among the followers of your target who is the most active? 'pockybotz'
## Among the followers of your target who is the most popular? 'quackzombie'
## Among the friends of your target, who is the most active layman? 'overheardinPC'
## Among the friends of your target, who is the most active expert? 'pockybotz' 
## Among the friends of your target, who is the most active celebrity? 'APSAtweets' 
## Among the friends of your target who is the most popular? 'APSAtweets'
## Among the followers of your target and their followers, who is the most active? 'ChadSchimke' 
## Among the friends of your target and their friends, who is the most active? 'Nettaaaaaaaa' 