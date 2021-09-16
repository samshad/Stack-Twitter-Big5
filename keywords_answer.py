from keybert import KeyBERT
import pandas as pd


questions = pd.read_csv('Data/stackoverflow_answers.csv')
dataset = pd.read_csv('Data/main_dataset.csv')
kw_model = KeyBERT()

cnt = 1

for i, r in dataset.iterrows():
    tf = questions[questions['stackoverflow_id'] == r['stackoverflow_id']]
    doc = list(tf['answers'])[0]
    keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None)
    print(keywords)
    cnt += 1
    if cnt > 10:
        break
