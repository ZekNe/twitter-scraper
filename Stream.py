import tweepy
import configparser
import pandas as pd
import json
import sys

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

class StreamMiner(tweepy.Stream):

    # def on_status(self, status):
    #     print(status)
    #     try:
    #         with open('stream.json', 'a') as f:
    #             f.write("%s\n" %status)
    #             return True
    #     except BaseException as e:
    #         print("Error on_status: %s" % str(e))
    #     return True

    def on_data(self, data):
        try:
            with open('stream_data.json', 'a') as d:
                d.write('%s,\n' % data.decode('utf-8'))
                return True
        except BaseException as b:
            print("Error on_data: %s" % str(b))
            return True



miner = StreamMiner(
    api_key, api_key_secret,
    access_token, access_token_secret
)

#Change track
# miner.sample()
miner.filter(track=["test"]) 