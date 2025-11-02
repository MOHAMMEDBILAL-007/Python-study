import pandas as pd
df = pd.read_csv("D:\learning\Python-study\self learning\Pandas\data.csv")
for i in df.columns:
    for j in df[i]:
        if j == None :
            print("null")