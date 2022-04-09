import tweepy
import configparser
import pandas as pd
import json


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

# # GET
# user = api.get_user(screen_name = 'NASA') #enter user screen name
# my_public_tweets = api.home_timeline() #personal timeline
user_public_tweets = api.user_timeline(screen_name = 'NASA') #enter user
# search_tweets = api.search_tweets(q='text' ,geocode='lat,lot,**km') #enter text, latitude, longitude, radius
user_followers_id = api.get_follower_ids(screen_name = 'NASA') # get id's of users followers

# # POST
# api.update_status('Hey!') # Post status tweet
# api.destroy_status(id) # remove status tweet
# api.create_favorite(id) # like tweet
# api.destroy_favorite(id) # remove like
# api.retweet(id) # enter tweet id to retweet
# api.unretweet(id) # enter tweed id to unretweet

data = []

#append data
for tweet in user_public_tweets: #(pick search type)
    if len(data) < 1:
        data.append([
            tweet.user.id,
            tweet.user.name,
            tweet.user.screen_name,
            tweet.user.description,
            tweet.created_at, 
            tweet.text, 
            tweet.user.followers_count, 
            tweet.user.friends_count,
            tweet.user.location
            ])

#Write data to json file
with open('test.json', 'w') as file_object:
    json.dump(data, file_object, default=str, indent=4, sort_keys=True)

# #Write user data to json file
# with open('user.json', 'w') as file_object:
#     json.dump(user, file_object, default=str, indent=4, sort_keys=True)

# #Get Users Friends
# friend_data_list = []
# user = api.get_user(screen_name = 'NASA') #Change name
# with open('friend.json', 'w') as file_object:
#     for friend in user.friends():
#         friend_data = api.get_user(screen_name = friend.screen_name)
#         friend_data_list.append([friend_data.screen_name, friend_data.id, friend_data.followers_count])
#     json.dump(friend_data_list, file_object, default=str, indent=4, sort_keys=True)


# #Write data to CSV file
# friend_columns = ['Name' , 'Id', 'follower_count']
# df = pd.DataFrame(friend_data_list, columns = friend_columns)
# df.to_csv('friend_data.csv')   


