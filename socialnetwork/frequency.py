import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def unique_non_null(s):
    return s.dropna().unique()

def get_top10(df):#insert degree table
    sorted = df.sort_values(by='Weight', ascending=False)
    print(sorted.shape)
    topTen=sorted.loc[:10]
    print(sorted.head(10))

predictionsCsv = pd.read_csv(r"C:\Users\Brandon\Documents\prediction_5-atom_closed_comment_data_all.csv")
#edgeList = pd.read_csv(r"C:\PycharmOut\data4.csv")
#print(edgeList)

#get_top10(edgeList)

topTenEmber=["rwjblue","stefanpenner","pixelhandler","wagenet","mixonic",
             "krisselden","machty","Serabe","locks","wycats"]
topTenAtom=["50Wliu","lee-dohm","ghost","kevinsawicki","mnquintana",
            "rsese","benogle", "Zireael07","izuzak","maxbrunsfeld"]
topTenBrew=["MikeMcQuaid","nickwph","carlocab","mistydemeo","Bo98"
            ,"SMillerDev","RandomDSdevel","fxcoudert","jonchang","timsutton"]
topTenSciKit=["jnothman","amueller","GaelVaroquaux","lesteve","rth",
              "agramfort","raghavrv","cmarmo","glemaitre","ogrisel"]

topTenBitcoin=["sipa" , "TheBlueMatt"	,	"MarcoFalke",	"luke-jr"	,	"laanwj",	"jonasschnelli",	"gmaxwell",	"gavinandresen",	"fanquake",
        "Diapolo"]#derived from gephi. Top ten degrees
topTen=topTenAtom

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


devs_labels.to_csv(r"C:\PycharmOut\frequencyAtom.csv")
dev_labels_topT=devs_labels[devs_labels.index.isin(topTen)]#fitlers to get top ten
print(dev_labels_topT.head(10))
dev_labels_topT.to_csv(r"C:\PycharmOut\frequencyTopTenAtom.csv")

#labelList=["IS","SC1","SC4","SC5","SC6","SC7"]
ax = dev_labels_topT.plot.bar(rot=0, color={"SC6":"orange", "IS":"green","SC1":"red",
"SC4":"purple","SC7":"brown","SC5":"pink"})
plt.show()



