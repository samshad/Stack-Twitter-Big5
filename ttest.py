import pandas as pd
from scipy.stats import ttest_rel


df = pd.read_csv('Data/tweet vs stack personality.csv')

arr = []

x = df['Openness']
y = df['openness']

t, p = ttest_rel(x, y)
arr.append(['openness', t, p])

x = df['Conscientiousness']
y = df['conscientiousness']

t, p = ttest_rel(x, y)
arr.append(['conscientiousness', t, p])

x = df['Extraversion']
y = df['extraversion']

t, p = ttest_rel(x, y)
arr.append(['extraversion', t, p])

x = df['Agreeableness']
y = df['agreeableness']

t, p = ttest_rel(x, y)
arr.append(['agreeableness', t, p])

x = df['Emotional range']
y = df['emotional range']

t, p = ttest_rel(x, y)
arr.append(['emotional range', t, p])

df = pd.DataFrame(arr, columns=['big5', 't-value', 'p-value'])
df.to_csv('Data/t-test_P-value.csv', index=False)

