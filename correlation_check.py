import pandas as pd
from scipy.stats import linregress


df = pd.read_csv('Data/main_dataset.csv')

personality_features = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Emotional range']
numeric_features = ['reputation']

# print(linregress(df['gender_num'], df['total_cheap']).rvalue)
# print(type(linregress(df['gender_num'], df['total_cheap'])))

arr = []

for x in personality_features:
    for y in numeric_features:
        r = round(linregress(df[x], df[y]).rvalue, 5)
        p = round(linregress(df[x], df[y]).pvalue, 5)
        # print(x, y, r, p)
        arr.append([x, r, p])

tf = pd.DataFrame(arr, columns=['x', 'R-value', 'P-value'])
tf.to_csv('Data/big5_reputation_correlation.csv', index=False)


