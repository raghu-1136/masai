import pandas as pd

data = {
   "patient_id": [1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12],
   "actual":[ 1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0],
   "predicted" :[ 1,  1,  1,  0,  0,  1,  1,  0,  0,  0,  0,  0]
   }

df = pd.DataFrame(data)

TN = 0
TP = 0
FN = 0
FP = 0

for i,row in df.iterrows():
    if row['actual'] == 1:
        if row['predicted'] == 1:
            TP = TP + 1
        else:
            FN = FN + 1
    else:
        if row['predicted'] == 1:
            FP = FP + 1
        else:
            TN = TN + 1
def metrics():
    a = round((TP + TN)/(TP+TN+FP+FN),4)
    p = TP/(TP+FP)
    r = TP/(TP + FN)
    f = 2*p*r/(p+r)
    return a,p,r,f
a,p,r,f = metrics()
print(f"TP = {TP} \nFP = {FP} \nTN = {TN} \nFN = {FN}")
print(f"Accuracy = {a} \nPrecision = {p} \nRecall = {r} \nF1 Score = {f}") 
