import numpy as np
import pandas as pd
from collections import defaultdict

predictionsCsv = pd.read_csv(r"C:\PycharmOut\bitcoinEdgeList.csv")

dict=defaultdict(int)
for index, row in predictionsCsv.iterrows():
    dict[row["Source"]]=dict[row["Source"]]+row["Weight"]
    dict[row["Target"]]=dict[row["Target"]]+row["Weight"]

s = pd.Series(dict)
sSorted = s.sort_values(ascending=False)
df = sSorted.to_frame().reset_index().rename(columns={"index":"Names",0:"Contributions"})

df.to_csv(r"C:\PycharmOut\bitcoinContributions.csv")
dfSorted=df.head(10)
dfSorted.to_csv(r"C:\PycharmOut\bitcoinContributions10.csv")
#Create Parieto chart from top ten