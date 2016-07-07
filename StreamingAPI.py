import requests
from requests_oauthlib import OAuth1

api_key = "PUhRhZcpxbcpd2eUWgjdvxb1N"
api_secret = "qb3JPFWXCfEWSM8EVFHbrZHnaDCEOx84YptoXNhsCrTpNDeVES"
access_token = "353684623-PCGotpXstvhmaHEYBPsEpagmf0cKigfkJP560bmW"
access_secret = "T8VPkk1bygJ6eRkZ5UcKamzPQKR9n1kYL5ZWvslpFZPFd"

url = "https://stream.twitter.com/1.1/statuses/filter.json"

auth = OAuth1(api_key, api_secret, access_token, access_secret)

r = requests.post(url, auth=auth, stream=True, data={"follow":"nasa9084","track":"emacs"})
print(r.json())

for line in r.iter_lines():
  print(line["text"])