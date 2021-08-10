import pandas as pd


# df = pd.read_csv('Data/main_dataset.csv')
df = pd.read_csv('Data/personality_questions_answers.csv')

# personality_features = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Emotional range']
personality_features = ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional range']

arr = []
for x in personality_features:
    arr.append([x, df[x].mean()])

tf = pd.DataFrame(arr, columns=['Big5', 'mean'])
# tf.to_csv('Data/twitter_big5_mean.csv', index=False)
tf.to_csv('Data/stackoverflow_big5_mean.csv', index=False)
