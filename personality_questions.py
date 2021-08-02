import pandas as pd
from get_personality import Get_Personality
import json


df = pd.read_csv('Data/main_dataset.csv')
users = list(df['stackoverflow_id'])

questions = pd.read_csv('Data/stackoverflow_questions.csv')

cnt = 1

for user in users[2:]:
    tf = questions[questions['stackoverflow_id'] == user]

    texts = ''
    for i, r in tf.iterrows():
        texts += ' ' + str(r['questions'])
    profile = Get_Personality(texts)
    with open('Data/Personality_Questions/' + str(user) + '.json', 'w') as json_file:
        json.dump(profile, json_file, indent=4)
    print(cnt)
    cnt += 1

