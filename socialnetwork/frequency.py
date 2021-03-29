import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def unique_non_null(s):
    return s.dropna().unique()


predictionsCsv = pd.read_csv(r"C:\prediction_1-bitcoin_closed_comment_data_all.csv")


topTen=["sipa" , "TheBlueMatt"	,	"MarcoFalke",	"luke-jr"	,	"laanwj",	"jonasschnelli",	"gmaxwell",	"gavinandresen",	"fanquake",
        "Diapolo"]#derived from gephi. Top ten degrees

row = predictionsCsv["commenter"].unique()
col = unique_non_null(predictionsCsv["pred_label"])

devs_labels = pd.DataFrame(index=row, columns=col) #row=commenter names; col=prediction labels
for col in devs_labels.columns:#sets all values to 0; defaults to NaN without
    devs_labels[col].values[:]=0

for index, row in predictionsCsv.iterrows():#Fills table with instances of prediction labels. NaN values are avoided;
    #dropping NaN first? 2 pandas loops but may better due to pandas being 4x faster than regular python;
    #perhaps select indexes using predictionCsv's commenters then select label.Perhaps..devs_labels.loc[predCsv["commenter"],predCsv["pred_label"]]]+=1
    if pd.notna(row["pred_label"]):
        devs_labels.loc[row["commenter"], row["pred_label"]]+=1
        print(devs_labels.loc[row["commenter"]])

devs_labels.to_csv(r"C:\PycharmOut\frequency.csv")
dev_labels_topT=devs_labels[devs_labels.index.isin(topTen)]#fitlers to get top ten
dev_labels_topT.to_csv(r"C:\PycharmOut\frequencyTopTen.csv")

#ax = dev_labels_topT.plot.bar(rot=0)
#plt.show()


