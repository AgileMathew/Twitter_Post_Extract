import json
import oauth2 as oauth

#replace *'s shown below with twitter-app consumer keys and access tokens
CONSUMER_KEY = "72spKdzAGbQ0g0P5GeIvbOPz9"
CONSUMER_SECRET = "1reH3X56lr92Jp9dzOli9iR9mFnnw80iQv76Ra6bPFR7dVwGLR"
ACCESS_KEY = "720163033482440704-hKU73c6XRpuF2N8IKw1KILa4xPZKySN"
ACCESS_SECRET = "bQ8q4rimVkiubjvPzRsJyWAjllCkR17MIYGiFLAKmvKds"

# Set up instances of our Token and Consumer.
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)



#url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count="+count
url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BillGates&count=10"
# Create our client.
client = oauth.Client(consumer, token)

# The OAuth Client request 
response, content = client.request(url)


# json string to list
tweets = json.loads(content)

for tweet in tweets:
    try:
        print tweet['text']
    except:
        pass
print('\t')
