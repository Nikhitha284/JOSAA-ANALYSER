import matplotlib.pylab as plt 
import pandas as pd 
import numpy as np
import seaborn as sns

df=pd.read_csv('semif.csv',index_col=[0]) #semif.csv is input data which we scrapped from website
df=df[~df['Closing Rank'].str.contains('P')]
df['Opening Rank']=df['Opening Rank'].astype(float).apply(np.ceil).astype(int)
df['Closing Rank']=df['Closing Rank'].astype(float).apply(np.ceil).astype(int)
df.Gender=df.Gender.fillna('Gender-Neutral')
df.drop(df.columns[[0,3]], axis=1, inplace=True)
df.index+=1
df.to_csv('semif1.csv') # semif1.csv is output file name