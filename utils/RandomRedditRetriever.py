# import unirest
import urllib.request # Python 3
import json
import requests
from random import random

class RandomRedditRetriever(object):
	def __init__(self, url):
		super(RandomRedditRetriever, self).__init__()
		self.url = url

	# def getRandomUrlOld(self):
	# 	response = unirest.get(self.url)

	# 	result = response.body
	# 	urls = []
	# 	for child in result['data']['children']:
	# 		if child['data']['domain'] != "self.babyelephants":
	# 			urls.append(child['data']['url'])
	# 	if len(urls) <= 0:
	# 		# message.reply("I couldn't find anything cute")
	# 		return "I couldn't find anything cute"
	# 	randInt = int(random() * len(urls))
	# 	gif = urls[randInt]
	# 	print(gif)
	# 	return gif

	def getRandomUrl(self):
		
		with urllib.request.urlopen(self.url) as response:
			result = json.loads(response.read())
			urls = []
			for child in result['data']['children']:
				if child['data']['domain'] != "self.babyelephants":
					urls.append(child['data']['url'])
			if len(urls) <= 0:
				# message.reply("I couldn't find anything cute")
				return "I couldn't find anything cute"
			randInt = int(random() * len(urls))
			return urls[randInt]
