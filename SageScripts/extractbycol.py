#!/usr/bin/env python3
# only works on 1 file at a time
import sys, re
import pandas as pd

df=pd.read_csv(sys.argv[1]) #import input file
out=sys.argv[2] #save name of output file
col=sys.argv[3] #save column we're filtering by

for value in sys.argv[4:]: #loop through all inputted search terms
    fileout=df[df[col].str.contains(value, flags=re.IGNORECASE,na=False)]
    fileout.to_csv(out,mode='a') #set to append bc we loop through