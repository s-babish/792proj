#!/usr/bin/env python3
# 

import sys, re, glob
import numpy as np 
import pandas as pd


df = pd.read_csv("Costa_Rica_Database_2022.csv", 
                 usecols=['ID','Date Collected', 'plant family', 'plant species', 'plant common name',
                          'order','family','sub family','lep species','lep name'], 
                parse_dates=['Date Collected'],infer_datetime_format=True)

print(df)
print(df.dtypes)
diet_dic = {}

diet_breadth = df.groupby('lep species')['plant species'].unique()
diet_number = df.groupby('lep species')['plant species'].nunique()

#diet_breadth['breadth'] = df['plant species'].value_counts()
diet_breadth.to_csv("Earthwatch_Diet_Breadth.csv")

data_by_date = df.sort_values(by = 'Date Collected')

df['Date Collected'].dt.year


print(data_by_date)


