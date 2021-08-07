import pandas as pd
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json


df = pd.read_csv('Data/main_dataset.csv')
users = list(df['stackoverflow_id'])

answers = pd.read_csv('Data/stackoverflow_answers.csv')
questions = pd.read_csv('Data/stackoverflow_questions.csv')

cnt = 1

authenticator = IAMAuthenticator('F91VJPHvze7_bD17qLwfvZtLvd-ij9jGwG7oAaiLEyMp')
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

personality_insights.set_service_url('https://gateway.watsonplatform.net/personality-insights/api')

for user in users[:1]:
    ans = answers[answers['stackoverflow_id'] == user]
    texts = ''
    for i, r in ans.iterrows():
        texts += ' ' + str(r['answers'])

    print(type(texts))

    # ques = questions[questions['stackoverflow_id'] == user]
    # for i, r in ques.iterrows():
    #     texts += ' ' + str(r['questions'])

    profile = personality_insights.profile(texts, content_type='text/plain', accept_language='en',
                                           accept='application/json').get_result()
    print(profile)
    with open('Data/Personality_Ques_Ans/' + str(user) + '.json', 'w') as json_file:
        json.dump(profile, json_file, indent=4)
    print(cnt)
    cnt += 1

