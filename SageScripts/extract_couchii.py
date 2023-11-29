#!/usr/bin/env python3

import sys
import pandas as pd
IN=pd.read_csv(sys.argv[1])
shape=IN.shape
print("Shape of file:" + str(shape))
print(IN.head())

if ("Sp" in list(IN.columns)):
    Couchii=IN.loc[IN["Sp"].str.strip() == "couchii"]
    Couchii.to_csv("couchii_mamu.csv",index = False,mode='a')
elif ("Species" in list(IN.columns)):
    Couchii2=IN.loc[IN["Species"].str.strip() == "couchii"]
    Couchii2.to_csv("couchii_mamu.csv",index=False, mode='a')
elif ("Spp" in list(IN.columns)):
    Couchii3=IN.loc[IN["Spp"].str.strip() == "couchii"]
    Couchii3.to_csv("couchii_mamu.csv",index=False, mode='a')
