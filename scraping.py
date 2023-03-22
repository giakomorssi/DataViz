import tweepy
import datetime
import pandas as pd

pd.set_option('display.max_columns', None)

# Authenticate API credentials
consumer_key = 'LEtnKqkfr6mEUNS93KbchewPy'
consumer_secret = '1R9Nkyaom7bD1G6wCkllFuTjoQITVUtOg3f03PxTZkDKPKM6GJ'
bearer = 'AAAAAAAAAAAAAAAAAAAAAAMmmQEAAAAACzyrCrba8mUimEaBuq3D98o5W3c%3DgpdC12oOFCvEmN6P6XnU1fPE7g2e0zZBQLarV2KGPCqSFSyN0F'
access_token = '1072469075140505601-EfilHrYYRv1XQdRuLN5ns4qkdWv0i9'
access_token_secret = 'fRRqMHgvXqQC0JKhVSLxMVxxseJd5LCA5JXEP4eTfRWHN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize API
twitter = tweepy.API(auth)

max_tweets = 1000
tweets_per_request = 100
tweets = []













