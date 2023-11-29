#!/usr/bin/env python3
import pandas as pd
import sys, numpy

df=pd.read_csv(sys.argv[1],header=0)
PreNo=str(sys.argv[2])
df2=pd.read_csv("old_MAMUs.csv",header=0)
df3=pd.read_csv("KER_MAMU_101923.csv",header=0)

df[PreNo]=df[PreNo].str.replace(" ","")
df2['ID']=df2['ID'].str.replace(" ","")
df3['ID']=df3['ID'].str.replace(" ","")

df=df.assign(ChkOld=df[PreNo].isin(df2['ID']).astype(int))
df=df.assign(ChkNew=df[PreNo].isin(df3['ID']).astype(int))

df['MAMU'] = df['ChkOld']
df.loc[df['ChkOld'] == 1, 'MAMU'] = "y"
df.loc[df['ChkNew'] == 1, 'MAMU'] = "y"

df.to_csv(sys.argv[1]+"_mamudat.csv",index=False,mode='w')