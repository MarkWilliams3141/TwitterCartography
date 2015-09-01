#from Twython import Twython
import tweepy

consumer_key = 'RFaZb68C3r9PNqVW05MNHSLoO'
consumer_secret = '5UopifHHVPbSBr7XRPOaIA3rQlFeHpyCTkhmyHW8soufLi0MYS'
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text


print "hi"
