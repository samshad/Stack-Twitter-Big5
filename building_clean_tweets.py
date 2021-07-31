import pandas as pd
from clean_text import get_clean
import os
import json


path = 'Data/Tweets/'
users = os.listdir(path)
cnt = 1

x = pd.DataFrame(columns=['users', 'locations', 'tweets'])
x.to_csv('Data/twitter_data.csv', index=False)

for user in users:
    print(cnt, " => ", user)
    files = os.listdir(path + user + '/')

    tweet = ''
    location = set()

    for file in files:
        with open(path + user + '/' + file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        try:
            tweet += ' ' + get_clean(data['text'])
        except Exception as e:
            print(e)
            tweet += ' '

        try:
            location.add(data['user']['location'])
        except Exception as e:
            print(e)

    df = pd.DataFrame([[user, list(location), tweet]])
    df.to_csv('Data/twitter_data.csv', mode='a', header=False, index=False)
    cnt += 1

print('Done...')
