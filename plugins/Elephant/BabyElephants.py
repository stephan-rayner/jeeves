from slackbot.bot import respond_to
from utils.RandomRedditRetriever import RandomRedditRetriever
import re

@respond_to('elephant me', re.IGNORECASE)
def elephant_me(message):
    print("elephant plugin hit")
    url = "http://www.reddit.com/r/babyelephants.json"
    randomRedditRetriever = RandomRedditRetriever(url)
    message.reply(randomRedditRetriever.getRandomUrl())