import pandas as pd


def normalize(x, mn, mx):
    return (x - mn) / (mx - mn)


df = pd.read_csv('Data/randomly_selected_100.csv')

arr = []

for i, r in df.iterrows():
    arr.append([r['stackoverflow_id']
                , round(normalize(r['question_count'], df['question_count'].min(), df['question_count'].max()), 2)
                , round(normalize(r['answer_count'], df['answer_count'].min(), df['answer_count'].max()), 2)
                , round(normalize(r['reputation'], df['reputation'].min(), df['reputation'].max()), 2)])

# print(tf.head().to_string(index=False))
tf = pd.DataFrame(arr, columns=['stackoverflow_id', 'question_count', 'answer_count', 'reputation'])
tf.to_csv('Data/randomly_selected_100_normalized.csv', index=False)
