import pandas as pd
import numpy as np
from combinationDef import createCombo2Df
import itertools as it
import math as mt


df1=pd.DataFrame([[2,2],[1,1]],columns=["A","B"])
df2=pd.DataFrame([[1,1],[2,2]],columns=["A","B"])
print(df1.eq(df2))