#!/usr/bin/env python3
import pandas as pd
import sys

df=pd.read_csv(sys.argv[1])
dup_check=str(sys.argv[2])
df=df.astype({dup_check:str})

df[dup_check]=df[dup_check].str.replace(" ","")
uniq_df=df.drop_duplicates(subset=[dup_check],keep='first')
uniq_df.to_csv("noduplicates_"+sys.argv[1],index=False)
