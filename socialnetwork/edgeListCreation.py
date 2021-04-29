import pandas as pd
import numpy as np
from itertools import combinations
from collections import defaultdict

print("Start: ")
predictionsCsv = pd.read_csv(r"C:\Users\Brandon\Documents\prediction_5-atom_closed_comment_data_all.csv")

names = predictionsCsv["commenter"].unique() #1674 unique; total comb=1,400,000 >

group = predictionsCsv.groupby("issue_no")#condenses table into issue_no
namesPerIssue = group["commenter"].unique() #creates a list of commenters per issue_no

i=0#counter to see progress

nameDict= defaultdict(int)
for names in namesPerIssue:
    comboList = combinations(names,2)
    i+=1
    print(i, "/", len(namesPerIssue))
    for pair in comboList:
        pairTup=tuple(pair)
        if pairTup[::-1] in nameDict:#If the reverse exists, then add to it. Don't create new row
            pairTup=pairTup[::-1]
        nameDict[pairTup]+=1

df = pd.Series(nameDict).to_frame().reset_index().rename(columns={'level_0': 'Source', 'level_1': 'Target', 0: 'Weight'})
df1 = pd.Series(nameDict).to_frame()
df2 = pd.Series(nameDict)
print(df2.index)
print(df1.reset_index())
#df.to_csv(r"C:\PycharmOut\atom.csv", index=False)
