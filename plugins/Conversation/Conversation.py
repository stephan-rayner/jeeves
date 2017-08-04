from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

hiRegex = re.compile(r'\bhi\b', re.IGNORECASE)
@respond_to(hiRegex)
def hi(message):
    message.reply('I can understand hi or HI!')

@listen_to('thank you', re.IGNORECASE)
def thanks(message):
    message.send('No worries, I try')
    message.react('+1')

@respond_to('what are you doing', re.IGNORECASE)
def chupacabra_libre(message):
    message.send('... plausible deniability ...')

@listen_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?')
def help(message):
    message.reply('Yes, I can!')

hello_regex = re.compile(r"\bhello\b", re.IGNORECASE)
@listen_to(hello_regex)
def hello_send(message):
    message.send('Hello!')
