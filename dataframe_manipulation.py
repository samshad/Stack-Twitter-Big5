import pandas as pd


personality = pd.read_csv('Data/personality_questions_answers.csv')
df = pd.read_csv('Data/randomly_selected_100_normalized.csv')

arr = []
for i, r in df.iterrows():
    tf = personality[personality['users'] == r['stackoverflow_id']]

    arr.append([r['stackoverflow_id'], r['question_count'], r['answer_count'],
                r['reputation'], list(tf['openness'])[0], list(tf['conscientiousness'])[0], 
                list(tf['extraversion'])[0], list(tf['agreeableness'])[0], list(tf['emotional range'])[0]])

out = pd.DataFrame(arr, columns=['stackoverflow_id', 'question_count', 'answer_count', 'reputation',
                                 'openness', 'conscientiousness', 'extraversion', 'agreeableness',
                                 'emotional range'])
out.to_csv('Data/selected_100_normalized_merged.csv', index=False)
