import pandas as pd
import ast


main_data = pd.read_csv('Data/Stack+Twitter+Ocean Data.csv')
twitter = pd.read_csv('Data/twitter_data.csv')
personality = pd.read_csv('Data/personality_data_twitter.csv')
stackoverflow = pd.read_csv('Data/stackoverflow_data.csv')

# stackoverflow['top_tags_question'] = stackoverflow['top_tags_question'].apply(lambda x: ast.literal_eval(x))
# stackoverflow['top_tags_answers'] = stackoverflow['top_tags_answers'].apply(lambda x: ast.literal_eval(x))

arr = []
cnt = 1
for index, row in personality.iterrows():
    user = row['users']
    tmp = twitter[twitter['users'] == user]

    location = list(tmp['locations'])[0] if len(list(tmp['locations'])) > 0 else ''
    
    Openness = row['Openness']
    Conscientiousness = row['Conscientiousness']
    Extraversion = row['Extraversion']
    Agreeableness = row['Agreeableness']
    Emotional_range = row['Emotional range']
    Conservation = row['Conservation']
    Openness_to_change = row['Openness to change']
    Hedonism = row['Hedonism']
    Self_enhancement = row['Self-enhancement']
    Self_transcendence = row['Self-transcendence']

    tmp = main_data[main_data['Twitter ID'] == 'https://twitter.com/' + user]
    stack_id = list(tmp['STACK ID'])[0]
    stack_id = stack_id.split('/')[2]

    tmp = stackoverflow[stackoverflow['id'] == int(stack_id)]
    # print(tmp.head().to_string())

    answer_count = list(tmp['answer_count'])[0] if len(list(tmp['answer_count'])) > 0 else 0
    question_count = list(tmp['question_count'])[0] if len(list(tmp['question_count'])) > 0 else 0
    reputation = list(tmp['reputation'])[0] if len(list(tmp['reputation'])) > 0 else ''
    top_tags_question = list(tmp['top_tags_question'])[0] if len(list(tmp['top_tags_question'])) > 0 else ''
    top_tags_answers = list(tmp['top_tags_answers'])[0] if len(list(tmp['top_tags_answers'])) > 0 else ''

    arr.append([user, stack_id, location, question_count, answer_count, reputation, top_tags_question,
                top_tags_answers, Openness, Conscientiousness, Extraversion, Agreeableness, Emotional_range, 
                Conservation, Openness_to_change, Hedonism, Self_enhancement, Self_transcendence])

df = pd.DataFrame(arr, columns=['twitter_id', 'stackoverflow_id', 'location', 'question_count', 'answer_count',
                                'reputation', 'top_tags_question', 'top_tags_answers', 'Openness', 
                                'Conscientiousness', 'Extraversion', 'Agreeableness', 'Emotional range', 
                                'Conservation', 'Openness to change', 'Hedonism', 'Self-enhancement', 
                                'Self-transcendence'])
df.to_csv('Data/merged_data.csv', index=False)
