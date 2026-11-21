import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.gridspec as gridspec

from Pandas.General_Cleaning import champions,TAGS
"Flattening dataframe for first plot"
df = champions[TAGS].copy()
df_flat = df.explode('tags')

roleslist = []
for roles in df_flat['tags']:
    if roles not in roleslist:
        roleslist.append(roles)

"Counting how many champions have 1 role and how many have 2 roles and etc"

df["role_count"] = df['tags'].str.len()
count = df['role_count'].value_counts()

Roles_1 = df[df["role_count"] == 1].explode('tags')
# Roles_1=Roles_1.to_frame()
roles_1_countdictionary = {}
for role in roleslist:
    for item_in_tags in Roles_1['tags']:
        if role == item_in_tags:
            if role in roles_1_countdictionary:
                roles_1_countdictionary[role] += 1
            else:
                roles_1_countdictionary[role] = 1

Roles_2 = df[df["role_count"] == 2].explode("tags")
# Roles_2=Roles_2.to_frame()
roles_2_countdictionary = {}
for role in roleslist:
    for item_in_tags in Roles_2['tags']:
        if role == item_in_tags:
            if role in roles_2_countdictionary:
                roles_2_countdictionary[role] += 1
            else:
                roles_2_countdictionary[role] = 1

Roles_2[['tags','difficulty']]
Roles_1[['tags','difficulty']]

print(Roles_1[Roles_1['tags']=='Support']['difficulty'])


print(roleslist)
print(roles_1_countdictionary)
print(roles_2_countdictionary)