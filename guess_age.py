import pandas as pd

age_map = pd.read_csv('data/age_map.csv', index_col='Title')
age_map = age_map['Age'] # Converting DataFrame to Series
def guess_age(row):
#     print(type(row)) # <class 'pandas.core.series.Series'?
    t = row['Title']
    row['Age'] = age_map[t]
    return row
