#!/usr/bin/env python3
# 

import sys, re, glob
import numpy as np 
import pandas as pd
from PCOA import pcoa

import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv("Costa_Rica_Database_2022.csv", 
                usecols=['ID','Date Collected', 'locale', 
                          'plant family', 'plant species', 'plant common name',
                          'order','family','sub family','lep species','lep name'], 
                parse_dates=['Date Collected'],infer_datetime_format=True)


#Cleaning up locale names so that they are the first three characters only 

df['plot_s']=df['locale'].str[:3]



#Extracting one species info: 

for file in sys.argv[1:]:  #loop through all files passed to the script
  IN=pd.read_csv(file, 
                usecols=['ID','Date Collected', 'locale', 
                          'plant family', 'plant species', 'plant common name',
                          'order','family','sub family','lep species','lep name'], 
                parse_dates=['Date Collected'],infer_datetime_format=True)
       
  if ("lep species" in list(IN.columns)): #most common column heading
      Couchii=IN.loc[IN["lep species"].str.strip() == "quadrus cerialis"]
      Couchii.to_csv("quadceri.csv",index = False,mode='a')
  
  elif ("Lep Species" in list(IN.columns)):
      Couchii2=IN.loc[IN["Species"].str.strip() == "quadrus cerialis"]
      Couchii2.to_csv("quadceri.csv",index=False, mode='a')
  
  elif ("Lep species" in list(IN.columns)):
      Couchii3=IN.loc[IN["Spp"].str.strip() == "quadrus cerialis"]
      Couchii3.to_csv("quadceri.csv",index=False, mode='a')



#Diet breadth, all instances of host plants recorded for each species 

diet_names = df.groupby('lep species')['plant species'].unique()
diet_names.to_csv("names_diet.csv")
diet_number = df.groupby('lep species')['plant species'].nunique()
diet_number.to_csv("numbers_diet.csv")
df_names = pd.read_csv("names_diet.csv")
df_num = pd.read_csv("numbers_diet.csv")
diet_full = pd.merge(df_num, df_names, on='lep species')
diet_full.to_csv("Diet Breadth Summary.csv")

plt.figure()
breadth = df_num.groupby('plant species')['lep species'].count().plot()
plt.xlabel("Diet - # of host plant species")
plt.ylabel("Number of Lepidopteran Species")
plt.title("Diet Breadth Plot")
plt.savefig("Diet Breadth Plot.png")


#Species Richness: number of species observed 
richness = df['lep species'].nunique()
print("\nNumber of species: ", richness,"\n")

#Species Abundance: Number of indiividuals per species per plot
plt.figure()
sp_abundance = df.groupby(['plot_s','lep species'])['lep species'].count().unstack().plot(legend=None)
plt.savefig('species_abundance.pdf')

#Number of species vs. #of individuals observed 
plt.figure()
spec_abun = df.groupby('lep species')['lep species'].count().rename('abundance')
spec_abun.to_csv("Abundance.csv")
df2 = pd.read_csv("Abundance.csv")
spec_numabun = df2.groupby('abundance').count().plot()
plt.xlim(0,60)
plt.ylabel("Number of species")
plt.title("Species Abundance Plot")
plt.savefig('Species_vs_Abundance.png')

# Rank abundance plot : Relative abundancy vs. Rank (low rank is most abundant)
plt.figure()
spec_rank = df2.sort_values('abundance', ascending=False)
print("\nNumber of individuals: ", spec_rank['abundance'].sum(), "\n")
spec_rank['abunprop'] = spec_rank['abundance']/(spec_rank['abundance'].sum())
spec_rank['rank'] = spec_rank.reset_index().index 
spec_rank = spec_rank.astype({'abunprop': float, 'rank':int})
spec_rank['rank'] +=1
spec_rank['logabun'] = np.log(spec_rank['abunprop'])
print(spec_rank)
plt.scatter(spec_rank['rank'], spec_rank['logabun'], s = 0.5)
plt.xlabel("Rank")
plt.ylabel("Log Relative Abundance")
plt.title("Rank Abundance Plot")
plt.savefig('Rank Abundance.png')
