import unirest
from random import random

class RandomRedditRetriever(object):
	def __init__(self, url):
		super(RandomRedditRetriever, self).__init__()
		self.url = url

	def getRandomUrl(self):
		response = unirest.get(self.url)
		result = response.body
		urls = []
		for child in result['data']['children']:
			if child['data']['domain'] != "self.babyelephants":
				urls.append(child['data']['url'])
		if len(urls) <= 0:
			# message.reply("I couldn't find anything cute")
			return "I couldn't find anything cute"
		randInt = int(random() * len(urls))
		elephantGif = urls[randInt]
		print elephantGif
		return elephantGif