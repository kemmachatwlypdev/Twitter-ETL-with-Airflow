import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    access_key="-------------------------" #API Key 
    access_secret="----------------------" #API Key Secret
    consumer_key="-----------------------" #Access Token
    consumer_secret="--------------------" #Access Token Secret

    #Twitter authentication
    auth=tweepy.OAuth1UserHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    #Creating an API object
    api=tweepy.API(auth)

    tweets=api.user_timeline(screen_name='@elonmusk',
                            count=200,
                            include_rts=False,
                            tweet_mode='extended'
                            )

    tweet_list=[]
    for tweet in tweets:
        text=tweet.json["full_text"]

        refinded_tweet={"user":tweet.user.screen_name,
                        'text':text,
                        'favorite_count':tweet.favorite_count,
                        'retweet_count':tweet.retweet_count,
                        'created_at':tweet.created_at}
        
        tweet_list.append(refinded_tweet)

    df=pd.DataFrame(tweet_list)
    df.to_csv("------bucket-----path") #CloudBucketPath