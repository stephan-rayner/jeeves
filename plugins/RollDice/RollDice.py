from slackbot.bot import respond_to
import re
from random import randint

@respond_to('roll', re.IGNORECASE)
def roll(message):
	summation = 0
	try:
		unpackedMessage = message.body['text'].lower().split("roll ")[1].split(" ")
		if len(unpackedMessage) > 3:
			raise Exception("Bad Input")
		releventText = flatten(unpackedMessage)
		numberToRoll, dieToRoll, modifier = extractTerms(releventText)
		if(numberToRoll > 12):
			message.reply('`I am not rolling this thing more than 12 times.`')
			return
		else:
			for index in xrange(numberToRoll):
				number = randint(1, dieToRoll)
				summation = summation + number
				message.send("Roll %d:  %d" % (index+1, number))
			message.send("Sum:  %d" % summation)
			message.send("Sum + modifier:  %d" % (summation + modifier))
	except Exception, e:
		message.reply(tryAgainMessage())
		return
def extractTerms(text):
	'''This is where the heavy thinking happens'''
	if('+' in text):
		numberToRoll, remaining = text.split("d")
		dieToRoll, modifier = remaining.split("+")
	else:
		numberToRoll, dieToRoll = text.split("d")
		modifier = 0
	return int(numberToRoll), int(dieToRoll), int(modifier)

def tryAgainMessage():
	option1 = "`roll [numberOfRolls]d[valueOfDie]`"
	option2 = "`roll [numberOfRolls]d[valueOfDie]+[modifier]`"
	option3 = "`roll [numberOfRolls]d[valueOfDie] + [modifier]`"
	return "It should look something like ...\n%s\nor\n%s\nor\n%s" % (option1, option2, option3)

def flatten(listOfStrings):
	returnText = ""
	for text in listOfStrings:
		returnText = returnText + text
	return returnText