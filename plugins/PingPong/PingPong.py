from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

regex = re.compile(r'^ping$', re.IGNORECASE)

@respond_to(regex)
def ping(message):
    message.reply('PONG')
