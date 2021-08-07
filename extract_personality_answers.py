import pandas as pd
import json
import os


files = os.listdir('Data/Personality_Answers/')

arr = []
for file in files:
    tmp = [file.split('.json')[0]]

    with open('Data/Personality_Answers/' + file, 'r') as f:
        data = json.load(f)

    try:
        for i in data['personality']:
            # print(i['name'], i['percentile'])
            tmp.append(i['percentile'])

        for i in data['values']:
            # print(i['name'], i['percentile'])
            tmp.append(i['percentile'])
    except Exception as e:
        for _ in range(10):
            tmp.append(None)

    arr.append(tmp)

df = pd.DataFrame(arr, columns=['users', 'Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness',
                                'Emotional range', 'Conservation', 'Openness to change', 'Hedonism',
                                'Self-enhancement', 'Self-transcendence'])

df.to_csv('Data/personality_answers.csv', index=False)

"""
Openness
Conscientiousness
Extraversion
Agreeableness
Emotional range
Conservation
Openness to change
Hedonism
Self-enhancement
Self-transcendence
"""
