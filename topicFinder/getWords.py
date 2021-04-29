import numpy as np
import pandas as pd

def getCommentsByLabel(df, label):
    labelFilter = df[df["pred_label"]==label]
    comments=labelFilter["comment_content"]
    return comments

predictionsCsv=pd.read_csv(r"C:\Users\Brandon\Documents\prediction_1-bitcoin_closed_comment_data_all.csv")

commentCsv=predictionsCsv["comment_content"]
commentCsvDf=commentCsv.to_frame()

#commentCsvDf.to_csv(r"C:\PycharmOut\comments2.csv", index=False) #done
labelList=["IS","SC1","SC4","SC5","SC6","SC7"]
for label in labelList:
    commentsByLabel=getCommentsByLabel(predictionsCsv,label)
    path="comments"+label+".csv"
    print(path)
    commentsByLabel.to_csv(path, index=False)


