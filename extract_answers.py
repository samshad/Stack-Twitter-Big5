import pandas as pd
from clean_text import get_clean
import os
import json


path = 'Data/answers/'
df = pd.read_csv('Data/main_dataset.csv')

users = list(df['stackoverflow_id'])

out = pd.DataFrame(columns=['stackoverflow_id', 'answers'])
out.to_csv('Data/stackoverflow_answers.csv', index=False)

cnt = 1

for user in users:
    print(cnt)
    cnt += 1

    try:
        with open('Data/answers/' + str(user) + '.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data['items']:
            txt = ' ' + get_clean(item['body'])

            tf = pd.DataFrame([[user, txt]])
            tf.to_csv('Data/stackoverflow_answers.csv', mode='a', header=False, index=False)
    except Exception as e:
        print(e)
        tf = pd.DataFrame([[user, '']])
        tf.to_csv('Data/stackoverflow_answers.csv', mode='a', header=False, index=False)

print('done...')
