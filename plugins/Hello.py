from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

regex = re.compile(ur"\bhello\b", re.IGNORECASE)
@listen_to(regex)
def hello_send(message):
    message.send('Hello!')
