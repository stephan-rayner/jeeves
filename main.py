#!/usr/bin/python

from slackbot.bot import Bot
import logging
import sys

def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    channel = logging.StreamHandler(sys.stdout)
    channel.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    channel.setFormatter(formatter)
    root.addHandler(channel)

def main():
    setup_logging()
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
