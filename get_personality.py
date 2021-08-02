from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json


#personality_insights = PersonalityInsightsV3(version="2017-10-13", iam_apikey='F91VJPHvze7_bD17qLwfvZtLvd-ij9jGwG7oAaiLEyMp', url='https://gateway.watsonplatform.net/personality-insights/api')

#authenticator = IAMAuthenticator('F91VJPHvze7_bD17qLwfvZtLvd-ij9jGwG7oAaiLEyMp')
authenticator = IAMAuthenticator('rKKOOaC5nd8haGRmAAFFeCXt196bYI5qhWogSapG_zlJ')
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)

#personality_insights.set_service_url('https://gateway.watsonplatform.net/personality-insights/api')
personality_insights.set_service_url('https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/66b10b97-021d-47ae-b5c2-fec4f691fc69')


def Get_Personality(text):
    try:
        profile = personality_insights.profile(text, content_type='text/plain', accept_language='en',
                                               accept='application/json').get_result()

        return profile
    except Exception as e:
        print(e)
        return {}

