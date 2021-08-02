from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import pandas as pd


#personality_insights = PersonalityInsightsV3(version="2017-10-13", iam_apikey='F91VJPHvze7_bD17qLwfvZtLvd-ij9jGwG7oAaiLEyMp', url='https://gateway.watsonplatform.net/personality-insights/api')

#authenticator = IAMAuthenticator('F91VJPHvze7_bD17qLwfvZtLvd-ij9jGwG7oAaiLEyMp')
authenticator = IAMAuthenticator('rKKOOaC5nd8haGRmAAFFeCXt196bYI5qhWogSapG_zlJ')
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

#personality_insights.set_service_url('https://gateway.watsonplatform.net/personality-insights/api')
personality_insights.set_service_url('https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/66b10b97-021d-47ae-b5c2-fec4f691fc69')

er_cnt = 0
cnt = 0
er_users = []

df = pd.read_csv('Data/twitter_data.csv')

for index, row in df.iterrows():
    cnt += 1
    user = row['users']
    tweet = row['tweets']

    print(cnt, " => ", user)

    try:
        profile = personality_insights.profile(tweet, content_type='text/plain', accept_language='en',
                                               accept='application/json').get_result()

        with open('Data/Personality_Tweets/' + user + '_personality.json', 'w') as json_file:
            json.dump(profile, json_file, indent=4)
    except:
        print('########## Error: ', user)
        er_users.append(user)
        er_cnt += 1

print('Done...', er_cnt)
print(er_users)
