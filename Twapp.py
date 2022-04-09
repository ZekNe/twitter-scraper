import tkinter
import tkinter.messagebox
import tweepy
import configparser
import pandas as pd
import json
from tkinter import *

# read config
config = configparser.ConfigParser()
config.read('config.ini')

# assign keys
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tkinter
top = tkinter.Tk()
top.geometry('250x150')

# grid
top.grid_rowconfigure(0, weight=1)
top.grid_rowconfigure(1, weight=10)
top.grid_rowconfigure(2, weight=1)
top.grid_columnconfigure(0, weight=1)
top.grid_columnconfigure(1, weight=3)
top.grid_columnconfigure(2, weight=1)

L1 = Label(top, text="SEARCH USER INFO")
L1.grid(row=1, column=1, sticky='n')
L2 = Label(top, text="Username:")
L2.grid(row=1, column=1, sticky='w')
E2 = Entry(top, bd=5)
E2.grid(row=1, column=1, sticky='e')

# Gets user data
def helloCallBack():
    user_name = E2.get()
    user_data = []
    name = api.user_timeline(screen_name=user_name)
    for tweet in name:
        if len(user_data) < 1:

            data = ()
            data = ('USER INFO\n__________\n\n-User id = %s\n\n -Username = %s\n\n -User Screen Name = %s\n\n -Description = %s\n\n -Created at = %s\n\n -Last Tweet = %s\n\n -Follower count = %s\n\n -Following count = %s\n\n -User location = %s' %
                    (tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.description, tweet.created_at, tweet.text, tweet.user.followers_count, tweet.user.friends_count, tweet.user.location))

    tkinter.messagebox.showinfo("Twapp", data)


# Button
B = tkinter.Button(top, text="Submit", command=helloCallBack)
B.grid(row=1, column=1, sticky='s')

# tkinter
top.mainloop()

