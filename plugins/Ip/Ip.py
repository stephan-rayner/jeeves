from slackbot.bot import respond_to
from slackbot.bot import listen_to
import os
import re

# regex = re.compile(r'\bipconfig\b', re.IGNORECASE)

@respond_to("ipconfig")
def find_ip(message):
    ip = os.popen("ifconfig | grep '192.168'").read().split(" ")[1]
    message.reply('My Ip is {}'.format(ip))
