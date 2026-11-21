import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from Pandas.Tag_analysis_Pandas import (df_flat,roles_1_countdictionary,
                                        roles_2_countdictionary,Roles_1,Roles_2,roleslist)

"PLOT"
color_palette = {
     "primary": "#264653",
    "secondary": "#287271",
    "tertiary": "#2A9D8F",
    "accent": "#8AB17D",
    "light": "#E9C46A",
    "background": "#F4F1DE"
}

mycolor=[]
for key,value in color_palette.items():
  mycolor.append(value)

fig,ax=plt.subplots(1,1,figsize=(15,4))
sns.countplot(data=df_flat,y='tags',ax=ax,
              palette=mycolor)
ax.set_title("ROLES")
ax.set_ylabel("ROLE_DISTRIBUTION")
ax.set_xlabel("COUNT")

plt.show()

fig,axes=plt.subplots(1,2,figsize=(20,7))


axes[0].pie(x=roles_1_countdictionary.values(),
            labels=roles_1_countdictionary.keys(),
            colors=mycolor,
            autopct='%1.1f%%',
            textprops={
                'fontsize':15,
                'fontweight':'bold'
            },
            radius=1)

axes[1].pie(x=roles_2_countdictionary.values(),
            labels=roles_2_countdictionary.keys(),
            colors=mycolor,
            autopct='%1.1f%%',
            radius=1,
            textprops={
                'fontsize':15,
                'fontweight':'bold'
            }
            )
plt.show()

fig,axes=plt.subplots(1,2,figsize=(18,6),sharey=True)
plt.subplots_adjust(wspace=0.05)

sns.boxplot(data=Roles_1,
            x="tags",y='difficulty',
            hue='tags',
            legend=False,
            ax=axes[0],
            hue_order=roleslist,
            order=roleslist,
            palette=mycolor
                         )
sns.boxplot(data=Roles_2,
            x='tags',y='difficulty',
            hue='tags',
            legend=False,
            ax=axes[1],
            hue_order=roleslist,
            order=roleslist,
            palette=mycolor)
plt.show()