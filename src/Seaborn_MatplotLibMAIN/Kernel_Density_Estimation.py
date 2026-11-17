import seaborn as sns
import matplotlib.pyplot as plt

from Pandas.Rol_Analysis_Pandas import df
from Role_AnalysisMATPLOT import bincount,df_Sorted_by_hp

fig,axes=plt.subplots(1,3,figsize=(15,5))

sns.histplot(data=df_Sorted_by_hp,x='hp',ax=axes[0],bins=bincount,
             kde=True,line_kws={'color':'#FF0000',
                                 'linewidth':2})
axes[0].set_title('KERNEL DISTRIBUTION ESTIMATION(HP)')
axes[0].set_xlabel('HP')
axes[0].set_ylabel('NUMBER OF CHAMPIONS')

sns.histplot(data=df_Sorted_by_hp,x='stats.armor',ax=axes[1],bins=bincount,
             kde=True,line_kws={'color':'#FF0000',
                                 'linewidth':2})
axes[1].set_title('KERNEL DISTRIBUTION ESTIMATION(ARMOR)')
axes[1].set_xlabel('ARMOR')
axes[1].set_ylabel('NUMBER OF CHAMPIONS')

sns.histplot(data=df_Sorted_by_hp,x='move_speed',ax=axes[2],bins=7,
             kde=True,line_kws={'color':'#FF0000',
                                 'linewidth':2})

axes[2].set_title('KERNEL DISTRIBUTION ESTIMATION(SPEED)')
axes[2].set_xlabel('SPEED')
axes[2].set_ylabel('NUMBER OF CHAMPIONS')

plt.tight_layout()
if __name__ == "__main__":
  plt.show()