import images as startrek
from slackbot.bot import listen_to
from random import random
from random import randint
import re

teaRegex = re.compile(ur'\btea\b', re.MULTILINE | re.IGNORECASE)
@listen_to(teaRegex)
def picard_tea(message):
	images = startrek.tea
	picardTeaImage = images[randint(0, len(images) - 1)]
	message.send("Tea? I'll have some.")
	message.send(picardTeaImage)

aleRegex = re.compile(ur'\bale\b', re.MULTILINE | re.IGNORECASE)
@listen_to(aleRegex)
def picard_ale(message):
	message.send("Ale? That might be fun ...")
	message.send(startrek.ale[0])

captainLogRegex = re.compile(ur'\bcaptain\b|\blog\b', re.IGNORECASE)
@listen_to(captainLogRegex)
def captain_log(message):
	image = startrek.log[randint(0, len(startrek.log) - 1)]
	message.send(image)

