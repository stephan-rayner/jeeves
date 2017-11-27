from slackbot.bot import respond_to
import urllib.request
import json
import re
from random import random

URL = "http://www.reddit.com/r/babyelephants.json"

@respond_to('elephant me', re.IGNORECASE)
def elephant_me(message):
    result = fetch(URL)
    url = extract_url(result)
    print(url)
    message.reply(url)


def fetch(url: str, rec_count=0):
    print("Fetching Data")
    if rec_count > 3:
        raise Exception("Unable to succesfully connect to reddit.")
    with urllib.request.urlopen(url) as r:
        result = json.loads(r.read())
        if r.status>= 400 and r.status < 500:
            if r.status == 429:
                print("RECURSION TIME")
                return fetch(url, rec_count+1)
        return result


def extract_url(result: dict) -> list:
    print("Extracting URL")
    urls = [child["data"]["url"] for child in result["data"]["children"]]
    randInt = int(random() * len(urls))
    return urls[randInt]