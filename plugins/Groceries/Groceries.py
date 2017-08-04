from slackbot.bot import respond_to
import re
import shelve
import logging

data = "./data/groceries.data"

# get_regex = re.compile(r'^groceries: \bget\b|\blist\b', re.MULTILINE | re.IGNORECASE)
get_regex = re.compile(r"\bgroceries.list\b", re.IGNORECASE)
@respond_to(get_regex)
def get_list(message):
    db = shelve.open(data)
    try:
        groceries = {key: db[key] for key in db}
        response = "\n"
        for key in db:
            if db[key] == "default":
                tts = key
            else:
                tts = "{} x{}".format(key, db[key])
            response = response + tts + "\n"
        message.reply(response)
    finally:
        db.close()

add_regex = re.compile(r'\bgroceries.add\b', re.MULTILINE | re.IGNORECASE)
@respond_to(add_regex)
def add_items(message):
    l = message.body["text"].lower().split("groceries.add")[1].replace(", ", ",").strip()
    items = l.split(",")

    db = shelve.open(data)
    try:
        for substing in items:
            item_quantity = substing.split(":")
            if len(item_quantity) == 1:
                item = item_quantity[0]
                quantity = "default"
            else:
                item = item_quantity[0]
                quantity = int(item_quantity[1])

            # FIXME: I feel str casting from unicode is dumb moving to py3 should fix this as strings are utf-8 as default
            db[item] = quantity
    finally:
        db.close()

remove_regex = re.compile(r"\bgroceries.remove\b", re.MULTILINE | re.IGNORECASE)
@respond_to(remove_regex)
def remove_items(message):
    l = message.body["text"].lower().split("groceries.remove")[1].replace(", ", ",").strip()
    items = l.split(",")

    db = shelve.open(data)
    try:
        for item in items:
            if item in db:
                del db[item]
    finally:
        db.close()

clear_regex = re.compile(r"\bgroceries.clear\b", re.IGNORECASE)
@respond_to(clear_regex)
def clear(message):
    db = shelve.open(data)
    try:
        for key in db:
            del(db[key])
    finally:
        db.close()
