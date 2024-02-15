#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

concat_df = pd.DataFrame() #initialize an empty df to combine everything into

numfiles=int(sys.argv[1]) #first argument if number of files
fileend=numfiles+2 #and that is used to figure out how to index through sys.argv
for file in sys.argv[2:fileend]: #loop through every file
    df=pd.read_csv(file,dtype=str) #read in file as data frame
    concat_df = pd.concat([concat_df,df],ignore_index=True) #concatenate by column, adding new columns every time a new one is introduced, and putting NA for any entries that don't have a vzlue for that column