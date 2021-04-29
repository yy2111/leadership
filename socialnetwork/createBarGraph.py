import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def swap(a,b):
    temp = a
    a=b
    b=a

def doubleSort(ref, curr): #takes an reference array and a differently sorted array. Returns the indexes of the references' elements within the different array
    size=len(ref)
    indexes=list(range(size))
    print(indexes)
    for i in range(size):
        if ref[i] != curr[i]:
            print("difference")
            for j in range(size):
                if ref[i] == curr[j]:
                    temp1=curr[i]
                    curr[i]=curr[j]
                    curr[j]=temp1
                    temp2=indexes[i]
                    indexes[i]=indexes[j]
                    indexes[j]=temp2
    print(curr)
    return indexes
#function unnecessary

df=pd.read_csv(r"C:\PycharmOut\frequencyTopTenAtom.csv")
print(df.columns)
df.rename(columns={'Unnamed: 0':"Contributors"}, inplace=True)
df = df.set_index("Contributors")

ax = df.plot.bar(rot=0, color={"IS":"green","SC1":"red",
"SC4":"purple","SC5":"pink","SC6":"orange", "SC7":"brown"})
ax.set_ylabel("Number of user associations (degree)")
handles, labels = ax.get_legend_handles_labels()
# sort both labels and handles by labels
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
ax.legend(handles, labels)


"""
handles, labels = plt.gca().get_legend_handles_labels()
truelabels=["IS","SC1","SC4","SC5","SC6","SC7"]
print(truelabels)
print(labels)
#order = doubleSort(truelabels, labels)
#order = [0,1,2,3,4,5]

print(order)
p#lt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
print()
"""
plt.show()
