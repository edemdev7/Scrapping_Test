import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time

consumer_key = "zd0yCHwwRJksvoDaJjhzb7Bda"
consumer_secret = "zg2OsiB4npUqzwXc18XMGPCbL0qt68At6vbBwBAQJ7C9wYtFLo"
access_token = "583099927718248449-WxjnFna4KzJG8yzBuGpfKYTzbKodLn"
access_token_secret = "qQ7ZsJzVlQ9WimuRCtnLEab3lNR8lYMxoDJBehT4RjwOq"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


df_query_based_tweets = pd.DataFrame()
text_query = 'nepal'

try:
    # Creation of query method using appropriate parameters
    tweets = tweepy.Cursor(api.search,q=text_query).items(count)

    # Pulling information from tweets iterable object and adding relevant tweet information in our data frame
    for tweet in tweets:
        df_query_based_tweets = df_query_based_tweets.append(
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