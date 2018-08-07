import numpy as np
import pandas as pd


def age_group(age):
    """ Given an input Age as number, this method returns the groups it belongs to -- baby, child, teen, adults, aged. """
    if(age == np.nan):
        return np.nan
    elif(age<3): 
        return 'baby'
    elif(age<12): 
        return 'child'
    elif(age<20): 
        return 'teen'
    elif(age<60): 
        return 'adult'
    else: 
        return 'aged'


age_map = pd.read_csv('data/age_map.csv', index_col='Title')
age_map = age_map['Age'] # Converting DataFrame to Series
def guess_age(row):
#     print(type(row)) # <class 'pandas.core.series.Series'?
    t = row['Title']
    row['Age'] = age_map[t]
    return row


def rounded_fare(fare):
    """ Rounds input param fare to nearest 10 """
    return round( (fare/10) ) * 10


def title(name):
    titles = ['Mr.','Mrs.','Miss.', 'Ms.', 'Master.', 'Major.', 'Mme.', 
              'Mlle.', 'Sir.', 'Lady.', 'Dr.', 'Rev.', 'Col.', 'Capt.', 'Don.', 'Dona.',
             'Countess.', 'Jonkheer.']
    for t in titles:
        if (t in name):
            return t

    