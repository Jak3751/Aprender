import json
from twitter import Twitter, OAuth
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

file = open("access_twitter.json", "r")
access_twitter = json.loads(file.read())

ACCESS_TOKEN = access_twitter["acessToken"]
ACCESS_TOKEN_SECRET = access_twitter["acessTokenSecret"]
CONSUMER_KEY = access_twitter["consumerKey"]
CONSUMER_SECRET = access_twitter["consumerSecret"]

auth = OAuth(
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    CONSUMER_KEY,
    CONSUMER_SECRET
)
twitter = Twitter.trends.place(_id = 455825)
rj_topicos = []
rj = { "tweets":[] }

for location in results_rio:
    trends = location['trends']
    for item in trends:
        if item['tweet_volume']:
            rj_topicos.append(item['name'])
            rj['tweets'].append(item['tweet_volume'])

df = pd.DataFrame(rj, index=rj_topicos)
df

fig=plt.figure(figsize=(18, 13), dpi=80, facecolor='w', edgecolor='k')
plt.rcParams.update({'font.size':22})
df["tweets"].plot.barth(title="Tendências no Twitter")
<matplotlib.axes._subplots.AxesSubplot at 0x9b5f950>

<figure size 1440x1040 with 0 Axes>

