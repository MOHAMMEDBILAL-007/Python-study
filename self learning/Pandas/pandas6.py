#merging
import pandas as pd

df1 = pd.DataFrame({
    "Id": [12,19,20,20,5,34,45,28,23],
    "name": ["luffy","nami","zoro","sanji","chopper","brook","jimbe","robin","frankie"],
    "shoping":[2021,2023,2020,2021,2024,2016,2025,2019,2024]
})
df2 = pd.DataFrame({
    "Id" :[12,19,20,76,45,65,3],
    "name":["luffy","nami","zoro","ace","jimbe","bon","lily"],
    "shopping":[2020,2021,2024,2016,2025,2019,2024]
})
print(df1)
print()
print(df2)