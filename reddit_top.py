import requests
import datetime

n_news = 10
date_beg = int(datetime.datetime(2017, 5, 3, 0, 1).timestamp())
date_end = int(datetime.datetime(2017, 5, 3, 23, 59).timestamp())
subreddit = 'worldnews'
params = {'subreddit':subreddit, 'after':date_beg, 'before':date_end, 'size':n_news, 'sort_type':'num_comments', 'sort':'desc'}
uri = 'https://api.pushshift.io/reddit/search/submission'

petition = requests.get(uri, params = params)
news = petition.json()

for new in news['data']:
	print(new['title'])