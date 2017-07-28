from slackbot.bot import respond_to
from lib.RandomRedditRetriever import RandomRedditRetriever
from random import random
import re
import unirest

@respond_to('elephant me', re.IGNORECASE)
def elephant_me(message):
	url = "http://www.reddit.com/r/babyelephants.json"
	randomRedditRetriever = RandomRedditRetriever(url)
	message.reply(randomRedditRetriever.getRandomUrl())