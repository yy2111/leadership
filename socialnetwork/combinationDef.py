import pandas as pd
import numpy as np
import math as mh
def createCombo2Df(list, column1, column2):
    dfRows=mh.comb(len(list),2)
    print("SIZE", dfRows)
    df = pd.DataFrame(pd.DataFrame(pd.NA, index=range(dfRows), columns=[column1, column2]))
    loop1Len=len(list)-1
    loop2Len=len(list)
    for i in range(loop1Len):
        col1El=list[i]
        for j in range(i+1,loop2Len):
            print(j)
            col2El=list[j]
            df.iloc[j-1,0]=col1El
            df.iloc[j-1,1]=col2El
            print(df.iloc[j-1])
    return df


