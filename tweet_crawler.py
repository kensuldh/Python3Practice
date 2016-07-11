#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

### Constants
oath_key_dict = {
    "consumer_key": "PUhRhZcpxbcpd2eUWgjdvxb1N",
    "consumer_secret": "qb3JPFWXCfEWSM8EVFHbrZHnaDCEOx84YptoXNhsCrTpNDeVES",
    "access_token": "353684623-PCGotpXstvhmaHEYBPsEpagmf0cKigfkJP560bmW",
    "access_token_secret": "T8VPkk1bygJ6eRkZ5UcKamzPQKR9n1kYL5ZWvslpFZPFd"
}

### Functions
def main():
    tweets = tweet_search("#Unity", oath_key_dict)
    #print(tweets)
    for tweet in tweets["statuses"]:
        tweet_id = tweet['id_str']
        text = tweet['text']
        created_at = tweet['created_at']
        user_id = tweet['user']['id_str']
        user_description = tweet['user']['description']
        screen_name = tweet['user']['screen_name']
        user_name = tweet['user']['name']
        #print ("tweet_id:", tweet_id)
        print ("text:", text)
        #print ("created_at:", created_at)
        #print ("user_id:", user_id)
        #print ("user_desc:", user_description)
        #print ("screen_name:", screen_name)
        #print ("user_name:", user_name)
    return


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
        "lang": "ja",
        #"result_type": "mixed",
        "count": "15"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print ("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

### Execute
if __name__ == "__main__":
    main()