import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Pandas.Rol_Analysis_Pandas import df
from Python_ANI import GameCharacter

df_Sorted_by_hp=df.sort_values(by='hp',ascending=True)

bincount=int(2*np.sqrt(len(df)))

fig,axes=plt.subplots(1,3,figsize=(15,5))

sns.histplot(data=df_Sorted_by_hp,x='hp',color='#228B22',alpha=0.45,ax=axes[0],bins=bincount)
axes[0].set_title('HP DISTRIBUTION')
axes[0].set_xlabel('HP')
axes[0].set_ylabel('NUMBER OF CHAMPIONS')

axes[0].axvline(df['hp'].mean(), color='#000000', linestyle='--', linewidth=2.4,
                label=f"MEAN{df['hp'].mean():.0f}")


sns.histplot(data=df_Sorted_by_hp,x='stats.armor',color='#FF0000',alpha=0.45,ax=axes[1],bins=bincount)
axes[1].set_title('ARMOR DISTRIBUTION')
axes[1].set_xlabel('ARMOR')
axes[1].set_ylabel('NUMBER OF CHAMPIONS')

axes[1].axvline(df['stats.armor'].mean(),color="#000000",linestyle='--',linewidth=2.4)

sns.histplot(data=df_Sorted_by_hp,x='move_speed',ax=axes[2],color='#0000FF',alpha=0.45,bins=bincount-10)
axes[2].set_title('SPEED DISTRIBUTION')
axes[2].set_xlabel('SPEED')
axes[2].set_ylabel('NUMBER OF CHAMPIONS')

axes[2].axvline(df['move_speed'].mean(),color='#000000',linestyle='--',linewidth=2.4)


# sns.kdeplot(data=df_Sorted_by_hp,ax="",'KERNEL DISTRIBUTION ESTIMATION')

plt.tight_layout()
plt.show()