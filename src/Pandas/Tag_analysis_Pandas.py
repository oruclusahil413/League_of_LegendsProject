import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from Pandas.General_Cleaning import champions,TAGS
"Flattening dataframe for first plot"
df=champions[TAGS].copy()

df_flat=df.explode('tags')

# print(df)

"Counting how many champions have 1 role and how many have 2 roles and etc"

df["role_count"]=df['tags'].str.len()

count=df['role_count'].value_counts()
# print(count)

Roles_1=df[df["role_count"]==1]['name']
Roles_1=Roles_1.to_frame()

Roles_2=df[df["role_count"]==2]['name']
Roles_2=Roles_2.to_frame()
print(Roles_2)

# print("Ümumi çempion sayı:",len(df))
# print("1 rolu olanların sayı:",len(Roles_1))
# print("2 rolu olanların sayı:",len(Roles_2))

df_flat['tags'].value_counts().to_dict()

# print(df_flat['tags'].value_counts().to_dict())
# for roles,countof_roles