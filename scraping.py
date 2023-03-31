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

##### Covid

# Define search query
query = 'covid'

for i in range(int(max_tweets / tweets_per_request)):
    if i == 0:
        results = twitter.search_tweets(q=query, lang='en', count=tweets_per_request)
    else:
        results = twitter.search_tweets(q=query, lang='en', count=tweets_per_request, max_id=oldest_id - 1)
    
    if not results:
        break

    tweets.extend(results)
    oldest_id = results[-1].id

data = []

# Extract tweet data and append to list
for tweet in tweets:
    tweet_data = {
        'user_name': tweet.user.name,
        'user_followers': tweet.user.followers_count,
        'user_friends': tweet.user.friends_count,
        'user_statuses': tweet.user.statuses_count,
        'user_listed': tweet.user.listed_count,
        'user_location': tweet.user.location,
        'user_description': tweet.user.description,
        'tweet_text': tweet.text,
        'tweet_date': tweet.created_at.date(),
        'time_time': tweet.created_at.time(), 
        'retweet_count': tweet.retweet_count,
        'tweet_source': tweet.source
    }
    data.append(tweet_data)

# Create a DataFrame from the tweet data
df = pd.DataFrame(data)

# fill spaces with NaN

df.replace('', pd.np.nan, inplace=True)

# create column with the query

df['query'] = query

##### Vaccine

# Define search query

query1 = 'vaccine'

for i in range(int(max_tweets / tweets_per_request)):
    if i == 0:
        results = twitter.search_tweets(q=query1, lang='en', count=tweets_per_request)
    else:
        results = twitter.search_tweets(q=query1, lang='en', count=tweets_per_request, max_id=oldest_id - 1)
    
    if not results:
        break

    tweets.extend(results)
    oldest_id = results[-1].id

data = []

# Extract tweet data and append to list
for tweet in tweets:
    tweet_data = {
        'user_name': tweet.user.name,
        'user_followers': tweet.user.followers_count,
        'user_friends': tweet.user.friends_count,
        'user_statuses': tweet.user.statuses_count,
        'user_listed': tweet.user.listed_count,
        'user_location': tweet.user.location,
        'user_description': tweet.user.description,
        'tweet_text': tweet.text,
        'tweet_date': tweet.created_at.date(),
        'time_time': tweet.created_at.time(), 
        'retweet_count': tweet.retweet_count,
        'tweet_source': tweet.source
    }
    data.append(tweet_data)
    
# Create a DataFrame from the tweet data
df1 = pd.DataFrame(data)

# fill spaces with NaN

df1.replace('', pd.np.nan, inplace=True)

# create column with the query

df1['query'] = query1

# Merge the data 

df = df.append(df1)

# Export

df.to_excel('tweets.xlsx', index=False)
# ciao
