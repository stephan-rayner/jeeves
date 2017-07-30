from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

regex = re.compile(ur'\bping\b', re.MULTILINE | re.IGNORECASE)

@respond_to(regex)
def ping(message):
    message.reply('PONG')
