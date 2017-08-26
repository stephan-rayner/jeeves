from slackbot.bot import respond_to
from slackbot.bot import listen_to
import socket
import re

from subprocess import call
call(["ls", "-l"])

regex = re.compile(r'\bWhat is your ip?\b', re.MULTILINE | re.IGNORECASE)

@respond_to(regex)
def ping(message):
    ip = os.popen("ifconfig | grep '192.168'").read().split(" ")[1]
    message.reply('My Ip is {}'.format(ip))
