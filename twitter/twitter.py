import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time

consumer_key = "hXZanneCo4XFP2LFsriUfSTt5"
consumer_secret = "QJopNdUrPDXNj4P48fT5IKdXZrohJ7Q9cVIAynqghEtDAzjsTa"
access_token = "1583099927718248449-F2k4P2H0M9bnZ261GvcvzJtEKtgntx"
access_token_secret = "gBWdFFJe4EiCiiWzezVNcopHfJ70BfcQ4DPsGWI1qiUaW"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

username = 'sbu'
count = 150

df_user_tweets = pd.DataFrame()
try:     
    # Creation of query method using appropriate parameters
    tweets =    tweepy.Cursor(api.user_timeline,id=username).items(count)
 
    
    # Pulling information from tweets iterable object and adding relevant tweet information in our data frame
    for tweet in tweets:
        df_user_tweets = df_user_tweets.append(
                          {'Created at' : tweet._json['created_at'],
                                       'User ID': tweet._json['id'],
                              'User Name': tweet.user._json['name'],
                                        'Text': tweet._json['text'],
                     'Description': tweet.user._json['description'],
                           'Location': tweet.user._json['location'],
             'Followers Count': tweet.user._json['followers_count'],
                 'Friends Count': tweet.user._json['friends_count'],
               'Statuses Count': tweet.user._json['statuses_count'],
         'Profile Image Url': tweet.user._json['profile_image_url'],
                         }, ignore_index=True)
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)

df_user_tweets.shape
(150, 10)
df_user_tweets.head()