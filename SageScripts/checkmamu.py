#!/usr/bin/env python3

import pandas as pd
import sys

df=pd.read_csv(sys.argv[1],header=0)
PreNo=str(sys.argv[2])
df2=pd.read_csv(sys.argv[3],header=0)
PreNo2=str(sys.argv[4])
df3=pd.read_csv("../specimens_to_find.csv",header=0)
PreNo3="Collector #"

df[PreNo]=df[PreNo].str.replace(" ","")
df2[PreNo2]=df2[PreNo2].str.replace(" ","")
ChkCounty=df[PreNo].isin(df2[PreNo2]).astype(int)
ChkNew=df[PreNo].isin(df3[PreNo3]).astype(int)
df=df.assign(ChkCounty=df[PreNo].isin(df2[PreNo2]).astype(int))
df=df.assign(ChkOld=df[PreNo].isin(df3[PreNo3]).astype(int))

OUT=open("new_mamus.txt",mode='a')

for _, row in df.iterrows():
    if row['ChkCounty'] == 1:
        if row['ChkOld']==0:
            OUT.write(str(row[PreNo])+"\n")

OUT.close()