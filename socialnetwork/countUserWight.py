import pandas as pd
df = pd.read_csv(r"C:\PycharmOut\data4.csv")

df2 = df.loc[(df["Source"]=='laanwj') | (df["Target"] == 'laanwj')]["Weight"].sum()

print(df2)