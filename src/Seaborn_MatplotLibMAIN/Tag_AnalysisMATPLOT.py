import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from Pandas.Tag_analysis_Pandas import df_flat

"PLOT"

fig,axes=plt.subplots(1,3,figsize=(20,7))

sns.countplot(data=df_flat,y='tags',ax=axes[0])
axes[0].set_title("ROLES")
axes[0].set_ylabel("ROLE_DISTRIBUTION")
axes[0].set_xlabel("COUNT")

# plt.pie(data=count,labels=)

plt.show()