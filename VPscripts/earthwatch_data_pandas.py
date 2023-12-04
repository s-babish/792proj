#!/usr/bin/env python3
# 

import sys, re, glob
import numpy as np 
import pandas as pd

import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv("Costa_Rica_Database_2022.csv", 
                 usecols=['ID','Date Collected', 'locale', 
                          'plant family', 'plant species', 'plant common name',
                          'order','family','sub family','lep species','lep name'], 
                parse_dates=['Date Collected'],infer_datetime_format=True)


#Diet breadth, all instances of host plants recorded for each species 
diet_breadth = df.groupby('lep species')['plant species'].unique()
diet_number = df.groupby('lep species')['plant species'].nunique()
diet_breadth.to_csv("Earthwatch_Diet_Breadth.csv")

#Cleaning up locale names so that they are the first three characters only 
df['plot_s']=df['locale'].str[:3]

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
plt.savefig('Species Vs Abundance.pdf')

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
plt.savefig('Rank Abundance.pdf')
