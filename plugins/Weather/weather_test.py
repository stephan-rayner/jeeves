import sys
sys.path.append("../..")
import slackbot_settings

import urllib2
import json

def weather(message):
	wunderground_token = slackbot_settings.WUNDERGROUND_TOKEN
	forecast_url = 'http://api.wunderground.com/api/' + wunderground_token + '/forecast/q/'

	text = message.body['text'].lower().strip()
	if "," in text:
		# Has country
		leftovers,country = text.split(", ")
		country = country.replace(" ", "_")
		city = leftovers.split("weather ")[1].replace(" ", "_")
		url = forecast_url + country +'/'+ city +'.json'
	else:
		# No country specified, its in Canada
		if len(text.split(" "))>1:
			#Specified City
			city = text.split("weather ")[1].replace(" ", "_")
			url = forecast_url +  'Canada/'+ city +'.json'
		else:
			#default to Victoria, BC
			url = forecast_url + 'Canada/Victoria.json'
	#print url
	f=urllib2.urlopen(url)

	json_string = f.read()

	parsed_json = json.loads(json_string)
	#print parsed_json
	forecastday = parsed_json['forecast']['txt_forecast']['forecastday']
	response = ""
	for i,forecast in enumerate(forecastday):
		if(i > 1):
			break
		report = forecast['title'] + ' will be ' + forecast['fcttext_metric']
		response += report + "\n"
	print response
	f.close()

if __name__ == '__main__':

	class Message(object):
		"""docstring for Message"""
		def __init__(self, text):
			super(Message, self).__init__()
			self.text = text
			self.body = {"text":self.text}
	message = Message("weather Colombo, Sri Lanka")
	weather(message)