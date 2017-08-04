from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

regex = re.compile(r'\bping\b', re.IGNORECASE)

@listen_to(regex)
@respond_to(regex)
def ping(message):
    message.send('PONG')
