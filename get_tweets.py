# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:37:20 2018

@author: Darren Huang
"""

# =============================================================================
# 1. Download the tweets for a given user to create a corpus of text.
# 2. Use the corpus to generate a sentence in the style of the Tweeter.
#
# Example: https://filiph.github.io/markov/
# Explanation: http://setosa.io/ev/markov-chains/
# =============================================================================
import tweepy, csv, re

consumer_key = "YOURCONSUMERKEY"
consumer_secret = "YOURCONSUMERSECRET"
access_key = "YOURACCESSKEY"
access_secret = "YOURACCESSSECRET"

def get_all_tweets(screen_name):
    all_tweets = []
    new_tweets = []
 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    client = tweepy.API(auth)
    new_tweets = client.user_timeline(screen_name=screen_name, count=200)
 
    while len(new_tweets) > 0:
        for tweet in new_tweets:
            all_tweets.append(tweet.text.encode("utf-8"))
 
        print( "We've got %s tweets so far" % (len(all_tweets)))
        max_id = new_tweets[-1].id - 1
        new_tweets = client.user_timeline(screen_name=screen_name,
                                          count=200, max_id=max_id)
 
    return all_tweets

def clean_tweet(tweet):
    #tweet = re.sub("https?\:\/\/\S+", "", tweet) #links
    #tweet = re.sub("#\S+", "", tweet)            #hashtags
    #tweet = re.sub("@\S+", "", tweet)            #at mentions
    tweet = re.sub("RT.+", "", tweet)            #Retweets
    tweet = re.sub("Video\:", "", tweet)         #Videos
    tweet = re.sub("\n", "", tweet)              #new lines
    tweet = re.sub("^\.\s.", "", tweet)          #leading whitespace
    tweet = re.sub("\s+", " ", tweet)            #extra whitespace
    tweet = re.sub("&amp;", "and", tweet)        #encoded ampersands
    tweet = re.sub("&gt;", ">", tweet)           #encoded greater than
    tweet = re.sub("&lt;", "<", tweet)           #encoded less than
    return tweet


def write_tweets_to_csv(tweets):
    with open('tweets.csv', 'w', newline='\n') as f:
        writer = csv.writer(f)
        for tweet in tweets:
            tweet = tweet.decode('utf-8')
            tweet = clean_tweet(tweet)
            tweet = tweet.encode()
            if tweet != b' ' and tweet != b'':
                writer.writerow([tweet])

def main():
    tweets = get_all_tweets('realDonaldTrump')  #Someone's Twitter ID
    write_tweets_to_csv(tweets)


if __name__ == '__main__':
    main()


