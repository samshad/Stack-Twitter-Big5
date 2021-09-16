from keybert import KeyBERT
import pandas as pd


questions = pd.read_csv('Data/stackoverflow_questions.csv')
dataset = pd.read_csv('Data/main_dataset.csv')
kw_model = KeyBERT()

for i, r in dataset.iterrows():
    if int(r['question_count']) >= 500:
        tf = questions[questions['stackoverflow_id'] == r['stackoverflow_id']]
        doc = list(tf['questions'])[0]
        keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None)
        print(keywords)
