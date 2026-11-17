import seaborn as sns
import matplotlib.pyplot as plt

from Pandas.Rol_Analysis_Pandas import FirstBar,SecondBar,ThirdBar

fig,axes=plt.subplots(1,3,figsize=(20,6))

fig.suptitle('CHAMPION STATS COMPARISON(FIRST 7)',
             fontsize=20,fontweight='bold')

# sns.barplot(data)

sns.barplot(data=FirstBar,ax=axes[0],
            x='hp',y='name',
                    hue='Group',palette={
                        'Highest 7':'#008F00',
                        'Lowest 7':'#10FF81'
                        }
                                          )
axes[0].set_title("CHAMPION HP")
axes[0].set_xlabel('HP')
axes[0].set_ylabel('NAME')

sns.barplot(data=SecondBar,  ax=axes[1],
            x='stats.armor',  y='name',
                    hue='Group', palette={
                            'Highest 7':'#FF0000',
                            'Lowest 7':'#FF7F7F'
                        }
                                            )

axes[1].set_title("CHAMPION ARMOR")
axes[1].set_xlabel('ARMOR')
axes[1].set_ylabel('NAME')

sns.barplot(data=ThirdBar,ax=axes[2],
            x='move_speed',y='name',
                      hue='Group',palette={
                          'Highest 7':'#00007F',
                          'Lowest 7':'#10F0FF'
                      }
                                      )

axes[2].set_title("CHAMPION SPEED")
axes[2].set_xlabel('SPEED')
axes[2].set_ylabel('NAME')

plt.show()