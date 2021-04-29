import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df=pd.read_csv(r"C:\PycharmOut\bitcoinContri10.csv")
df= df.rename(columns={"Unnamed: 0":"Names", "0":"Contributions"})

df["cumpercentage"] = df["Contributions"].cumsum()/df["Contributions"].sum()*100


fig, ax = plt.subplots()
ax.bar(df["Names"], df["Contributions"], color="C0")
ax2 = ax.twinx()
ax2.plot(df["Names"], df["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
plt.show()

