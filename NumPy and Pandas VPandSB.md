---
output:
  html_document: default
  pdf_document: default
---

# Sage Babish and Victoria Peechatt Final Project

## NumPy, pandas, data cleaning and visualization

### We used Pandas and NumPy to clean and extract data from our datasets.

#### Sage has multiple people's specimen catalogs, data on snake TTX resistance in multiple formats, and a host of other unorganized files to extract data from.

I needed two different sets of information from these data sets. First, which specimens collected by our lab and our collaborators were from my study area, and did we have tissue samples, sequencing data, or phenotypes for them? Second, which specimens had phenotypes, base speeds, and at least one out of SVL, mass, and tail length? The first information was used to figure out how many tissue/genetic samples we already had and how many new ones would need to be requested from museums or captured in the field and phenotyped. The second set will be used to model the effects of mass, size, body condition, and TTX resistance on base speed in an attempt to observe a trade-off between resistance and muscle function.

##### Part 1: Catalog Searches

My first steps for this project were parsing through several specimen collection catalogs and extracting specimens based on increasingly specific qualifications. The first qualification was pulling out all the specimens that were *Th. couchii*, which I did with this script:

###### extract_couchii.py

``` python
#!/usr/bin/env python3
import sys
import pandas as pd

for file in sys.argv[1:]:
  IN=pd.read_csv(file)
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
  
  IN.close()
```

extractbycol.py

``` python
#!/usr/bin/env python3
# only works on 1 file at a time
import sys, re
import pandas as pd

df=pd.read_csv(sys.argv[1]) #import input file
out=sys.argv[2] #save name of output file
col=sys.argv[3] #save column we're filtering by

for value in sys.argv[4:]: #loop through all inputted search terms
    fileout=df[df[col].str.contains(value, flags=re.IGNORECASE,na=False)] #pull rows with the values passed as   
                                                                            #inputs in the column we specified
    fileout.to_csv(out,mode='a') #set to append bc we loop through
```

dropduplicates.py

``` python
#!/usr/bin/env python3
import pandas as pd
import sys

df=pd.read_csv(sys.argv[1])
dup_check=str(sys.argv[2])
df=df.astype({dup_check:str})

df[dup_check]=df[dup_check].str.replace(" ","")
uniq_df=df.drop_duplicates(subset=[dup_check],keep='first')
uniq_df.to_csv("noduplicates_"+sys.argv[1],index=False)
```

checkmamu.py (making sure there wasn't new data in new mamu files)

``` python
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
```

mamuchk.py (coding if specimen had mamu in old or new mamu file, once i was on el dorado and knew we wanted both)

``` python
#!/usr/bin/env python3
import pandas as pd
import sys

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
```

##### Part 2: Compiling Old Data

Intro blah blah blah

concat_keepsetcols.py

``` python
#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

concat_df = pd.DataFrame()

numfiles=int(sys.argv[1])
fileend=numfiles+2
for file in sys.argv[2:fileend]:
    df=pd.read_csv(file,dtype=str)
    concat_df = pd.concat([concat_df,df],ignore_index=True)

out_df=pd.DataFrame()
for col in sys.argv[fileend:]:
    out_df = pd.concat([out_df,concat_df[col]],axis=1)
    
out_df[sys.argv[fileend]]=out_df[sys.argv[fileend]].replace('[^\d\.]',np.nan,regex=True)

out_df.dropna(subset=[sys.argv[fileend],sys.argv[fileend+1]], inplace = True)

out_df.to_csv("concatenatedcols.csv",index=False)
```

#### Peechatt has three 20+ year datasets with caterpillar, host plant, and other data.

-   First, I imported the datasets.
-   I cleaned the data, and extracted the columns I wanted to look at further.
-   I've used the data before to calculte the host breadth of the species that were collected. Previously, I manually went through the excel, sorted by lep species name, and counted the unique number of host plants. But with pandas and numpy, it took 4 lines of code!
-   I used matplotlib to make figures of species richness, rank abundance, etc. for the sites.

**import packages & check required datasets**

``` python
import os
import numpy as np
import pandas as pd
```
