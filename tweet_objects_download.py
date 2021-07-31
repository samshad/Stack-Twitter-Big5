import tweepy
import json
import os
import pandas as pd
from Auth.auth import consumer_key, consumer_secret, access_key, access_secret


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

df = pd.read_csv('Data/Stack+Twitter+Ocean Data.csv')
users = []
error_users = []

for index, row in df.iterrows():
    users.append(str(row['Twitter ID']).split('https://twitter.com/')[1])

cnt = 0
for user in users:
    print(user)
    cnt += 1
    print('Count: ', str(cnt))
    name = user
    tweet_objects = []
    alltweets = []

    try:
        new_tweets = api.user_timeline(screen_name=name, count=200)

        for i in new_tweets:
            tweet_objects.append(i)

        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        while len(new_tweets) > 0:
            print("getting tweets before %s" % (oldest))
            new_tweets = api.user_timeline(screen_name=name, count=200, max_id=oldest)
            for i in new_tweets:
                tweet_objects.append(i)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
            print("...%s tweets downloaded so far" % (len(alltweets)))

        for i in tweet_objects:
            path = 'Data/Tweets/' + name + '/'
            if not os.path.exists(path):
                os.makedirs(path)

            with open(path + i.id_str + '.json', 'w', encoding='utf-8') as f:
                json.dump(i._json, f, ensure_ascii=False, indent=4)
    except:
        print("error >>> " + name)
        error_users.append(name)

z = pd.DataFrame(error_users, columns=['users'])
z.to_csv('Data/error_users.csv', index=False)
print("done...")
