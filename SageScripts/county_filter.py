#!/usr/bin/env python3

import sys
import pandas as pd
import re
df=pd.read_csv(sys.argv[1])

counties = ['Placer','Sierra','Nevada']
df=df[df['County'].str.contains("|".join(counties), flags=re.IGNORECASE,na=False)]
df.to_csv("counties_"+sys.argv[1],mode='w')