from slackbot.bot import respond_to
from slackbot.bot import listen_to
import socket
import re

regex = re.compile(ur'\bWhat is your ip?\b', re.MULTILINE | re.IGNORECASE)

@respond_to(regex)
def ping(message):
	ip = socket.gethostbyname(socket.gethostname())
	message.reply('My Ip is {}'.format(ip))
