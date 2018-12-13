import tweepy
from textblob import TextBlob
consumer_key= 'CONSUMER_KEY'
consumer_secret= 'CONSUMER_SECRET'
access_token='ACCESS_TOKEN'
access_token_secret='ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.search('ANY_TOPIC')


for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
print("END")
