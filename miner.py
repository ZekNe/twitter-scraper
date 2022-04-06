import tweepy
import configparser
import pandas as pd
import json


# read config 
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#make data list
public_tweets = api.home_timeline()
columns = ['Time', 'User', 'Tweet']
data = []

#append data
for tweet in public_tweets:
    if len(data) < 6:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

#Write data on json file
with open('test.json', 'w') as file_object:
    json.dump(data, file_object, default=str, indent=4, sort_keys=True)

# #Get User
# user = api.get_user(screen_name = 'name')
# with open('user.json', 'w') as file_object:
#     json.dump(user, file_object, default=str, indent=4, sort_keys=True)


#Get User Friends
friend_columns = ['Name' , 'Id']
friend_data_list = []
user = api.get_user(screen_name = 'name')
with open('friend.json', 'w') as file_object:
    for friend in user.friends():
        friend_data = api.get_user(screen_name = friend.screen_name)
        friend_data_list.append([friend_data.screen_name, friend_data.id])
    json.dump(friend_data_list, file_object, default=str, indent=4, sort_keys=True)


df = pd.DataFrame(friend_data_list, columns = friend_columns)
df.to_csv('friend_data.csv')   

# #Write data on CSV file
# df = pd.DataFrame(data, columns = columns)
# df.to_csv('tweets.csv')



# class IDPrinter(tweepy.Stream):

#     def on_status(self, status):
#         print(status.id)


# stream = tweepy.Stream(
#     api_key, api_key_secret,
#     access_token, access_token_secret
# )

# stream.sample()


# #Stream
# class TweetListener(tweepy.Stream):


#     def on_data(self, data):
#         try:
#             with open('test.json', 'a') as f:
#                 f.write(data)
#                 return True

#         except BaseException as e:
#             print("Error on_data: %s" % str(e))
#         return True

#     def on_error(self, status):
#         print(status)
#         return True

# twitter_stream = TweetListener(
#     api_key, api_key_secret,
#     access_token, access_token_secret
# )
