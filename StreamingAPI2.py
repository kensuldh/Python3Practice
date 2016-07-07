# -*- coding: utf-8 -*-
# easy_install python_twitter
import twitter
import sys
import codecs
import dateutil.parser
import datetime
import time
from peewee import *


db = SqliteDatabase('twitter_stream.sqlite')


class Twitte(Model):
    createAt = DateTimeField(index=True)
    idStr = CharField(index=True)
    contents = CharField()

    class Meta:
        database = db


# easy_install の最新版でGetStreamFilterがなければ下記のコード追加
# https://github.com/bear/python-twitter/blob/master/twitter/api.py
def GetStreamFilter(api,
                    follow=None,
                    track='#spiknsk',
                    locations=None,
                    delimited=None,
                    stall_warnings=None):
    '''Returns a filtered view of public statuses.

    Args:
      follow:
        A list of user IDs to track. [Optional]
      track:
        A list of expressions to track. [Optional]
      locations:
        A list of Latitude,Longitude pairs (as strings) specifying
        bounding boxes for the tweets' origin. [Optional]
      delimited:
        Specifies a message length. [Optional]
      stall_warnings:
        Set to True to have Twitter deliver stall warnings. [Optional]

    Returns:
      A twitter stream
    '''
    if all((follow is None, track is None, locations is None)):
        raise ValueError({'message': "No filter parameters specified."})
    url = '%s/statuses/filter.json' % api.stream_url
    data = {}
    if follow is not None:
        data['follow'] = ','.join(follow)
    if track is not None:
        data['track'] = ','.join(track)
    if locations is not None:
        data['locations'] = ','.join(locations)
    if delimited is not None:
        data['delimited'] = str(delimited)
    if stall_warnings is not None:
        data['stall_warnings'] = str(stall_warnings)

    json = api._RequestStream(url, 'POST', data=data)
    for line in json.iter_lines():
        if line:
            data = api._ParseAndCheckTwitter(line)
            yield data


def main(argvs, argc):
    if argc != 6:
        print ('Usage #python %s consumer_key consumer_secret access_token_key access_token_secret #tag1,#tag2 ' % argvs[0])
        #, argvs[0] ,
        return 1
    consumer_key = argvs[1]
    consumer_secret = argvs[2]
    access_token_key = argvs[3]
    access_token_secret = argvs[4]
    # UNICODE変換する文字コードは対象のターミナルに合わせて
    track = argvs[5].decode('cp932').split(',')

    db.create_tables([Twitte], True)

    api = twitter.Api(base_url="https://api.twitter.com/1.1",
                      consumer_key="PUhRhZcpxbcpd2eUWgjdvxb1N",
                      consumer_secret="qb3JPFWXCfEWSM8EVFHbrZHnaDCEOx84YptoXNhsCrTpNDeVES",
                      access_token_key="353684623-PCGotpXstvhmaHEYBPsEpagmf0cKigfkJP560bmW",
                      access_token_secret="T8VPkk1bygJ6eRkZ5UcKamzPQKR9n1kYL5ZWvslpFZPFd")
    for item in GetStreamFilter(api, track=track):
        print ("'---------------------'")
        if 'text' in item:
            print (item['id_str'])
            print (dateutil.parser.parse(item['created_at']))
            print (item['text'])
            print (item['place'])
            row = Twitte(createAt=dateutil.parser.parse(item['created_at']),
                         idStr=item['id_str'],
                         contents=item['text'])
            row.save()
            row = None

if __name__ == '__main__':
    sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='backslashreplace')
    argvs = sys.argv
    argc = len(argvs)
    sys.exit(main(argvs, argc))