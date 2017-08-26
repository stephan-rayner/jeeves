from slackbot.bot import listen_to
from random import random
from random import randint
import re

# WTF: https://stackoverflow.com/questions/42263962
from . import images

teaRegex = re.compile(r'\btea\b', re.MULTILINE | re.IGNORECASE)
@listen_to(teaRegex)
def picard_tea(message):
	tea_imgs = images.tea
	picardTeaImage = tea_imgs[randint(0, len(tea_imgs) - 1)]
	message.send("Tea? I'll have some.")
	message.send(picardTeaImage)

aleRegex = re.compile(r'\bale\b', re.MULTILINE | re.IGNORECASE)
@listen_to(aleRegex)
def picard_ale(message):
	message.send("Ale? That might be fun ...")
	message.send(images.ale[0])

captainLogRegex = re.compile(r'\bcaptain\b|\blog\b', re.IGNORECASE)
@listen_to(captainLogRegex)
def captain_log(message):
	image = images.log[randint(0, len(images.log) - 1)]
	message.send(image)

