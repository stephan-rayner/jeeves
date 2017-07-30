import sys
sys.path.append("../..")
import slackbot_settings
from slackbot.bot import respond_to
import urllib2
import json
import re

regex = re.compile(ur'\bweather\b', re.MULTILINE | re.IGNORECASE)

@respond_to(regex)
def weather(message):
	print("DOING STUFF?!?!?!")
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
	print("JSON STRING", json_string)
	forecastday = parsed_json['forecast']['txt_forecast']['forecastday']
	response = ""
	for i,forecast in enumerate(forecastday):
		if(i > 1):
			break
		report = '`' + forecast['title'] + '`' + ' will be ' + forecast['fcttext_metric']
		response += report + "\n"
	message.send(response)
	f.close()
