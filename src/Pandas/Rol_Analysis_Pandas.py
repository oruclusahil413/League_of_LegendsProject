from General_Cleaning import ROLS_ANALYSIS_CSV
import pandas as pd

df=ROLS_ANALYSIS_CSV

df_Sorted_by_hp=df.sort_values(by='hp',ascending=True)

"""FIRST"""
FirstBar_highest=df.nlargest(7,'hp')[['name','hp']]
# print(FirstBar_highest)
FirstBar_highest['Group']='Highest 7'

FirstBar_smallest=df.nsmallest(7,'hp')[['name','hp']]
FirstBar_smallest=FirstBar_smallest.sort_values(by='hp',ascending=False)
# print(FirstBar_smallest)
FirstBar_smallest['Group']='Lowest 7'

FirstBar=pd.concat([FirstBar_highest,FirstBar_smallest])
# print(FirstBar[['name','hp']])

"""SECOND"""
SecondBar_highest=df.nlargest(7,'stats.armor')[['name','stats.armor']]
# print(SecondBar_highest)
SecondBar_lowest=df.nsmallest(7,'stats.armor')[['name','stats.armor']]
# print(SecondBar_lowest)

SecondBar_highest['Group']='Highest 7'
SecondBar_lowest['Group']='Lowest 7'

SecondBar_lowest=SecondBar_lowest.sort_values(by='stats.armor',ascending=False)

SecondBar=pd.concat([SecondBar_highest,SecondBar_lowest])

# print(SecondBar_highest)
#print(SecondBar_lowest)

"""THIRD"""
ThirdBar_highest=df.nlargest(7,'move_speed')[['name','move_speed']]
ThirdBar_lowest=df.nsmallest(7,'move_speed')[['name','move_speed']]

ThirdBar_lowest=ThirdBar_lowest.sort_values(by='move_speed',ascending=False)

ThirdBar_highest['Group']='Highest 7'
ThirdBar_lowest['Group']='Lowest 7'

ThirdBar=pd.concat([ThirdBar_highest,ThirdBar_lowest])