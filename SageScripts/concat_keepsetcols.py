#!/usr/bin/env python3
import sys
import pandas as pd

concat_df = pd.DataFrame()

numfiles=int(sys.argv[1])
fileend=numfiles+2
for file in sys.argv[2:fileend]:
    df=pd.read_csv(file,dtype=str)
    concat_df = pd.concat([concat_df,df],ignore_index=True)

out_df=pd.DataFrame()
for col in sys.argv[fileend:]:
    out_df = pd.concat([out_df,concat_df[col]],axis=1)

out_df.dropna(subset=[sys.argv[fileend]], inplace=True)
out_df.to_csv("concatenatedcols.csv",index=False)