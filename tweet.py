#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import codecs, sys
#sys.stdout = codecs.getwriter('cp932')(sys.stdout)

from requests_oauthlib import OAuth1Session
import json

#consumer_key="PUhRhZcpxbcpd2eUWgjdvxb1N",
#                      consumer_secret="qb3JPFWXCfEWSM8EVFHbrZHnaDCEOx84YptoXNhsCrTpNDeVES",
#                      access_token_key="353684623-PCGotpXstvhmaHEYBPsEpagmf0cKigfkJP560bmW",
#                      access_token_secret="T8VPkk1bygJ6eRkZ5UcKamzPQKR9n1kYL5ZWvslpFZPFd")
CK = 'PUhRhZcpxbcpd2eUWgjdvxb1N'                             # Consumer Key
CS = 'qb3JPFWXCfEWSM8EVFHbrZHnaDCEOx84YptoXNhsCrTpNDeVES'         # Consumer Secret
AT = '353684623-PCGotpXstvhmaHEYBPsEpagmf0cKigfkJP560bmW' # Access Token
AS = 'T8VPkk1bygJ6eRkZ5UcKamzPQKR9n1kYL5ZWvslpFZPFd'         # Accesss Token Secert

# ツイート投稿用のURL
#url = "https://api.twitter.com/1.1/statuses/update.json"
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# ツイート本文
#params = {"status": "Hello, World!"}
params = {}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
#req = twitter.post(url, params = params)
req = twitter.get(url, params = params)

# レスポンスを確認
#if req.status_code == 200:
#    print ("OK")
#else:
#    print ("Error: %d" % req.status_code)

if req.status_code == 200:
    # レスポンスはJSON形式なので parse する
    #timeline = json.loads(req.text)
    timeline = json.dumps(req.text)
    decode_timeline = json.loads(timeline)
    #encode_json_data = req.text.dumps(json_data, indent=4)
    print (decode_timeline)
    #print(timeline)
    # 各ツイートの本文を表示
    #for tweet in decode_timeline:
        #sys.stdout.write(tweet["text"])
        #print(str(tweet['text']))
else:
    # エラーの場合
    print ("Error: %d" % req.status_code)