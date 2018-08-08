#
# Feature Engineering
#

import numpy as np
import pandas as pd

# Pre-processing
from sklearn.preprocessing import StandardScaler

def transform(df, cols, sc=StandardScaler()):
    '''
    transform the select column data of input dataframe using the input scalar
    Default scalar is StandardScaler
    '''
#    sc = StandardScaler()
    sc.fit(df[cols])
    ndf = sc.transform(df[cols])
    ndf = pd.DataFrame(data=ndf, columns=cols, index=df.index)
    return ndf

