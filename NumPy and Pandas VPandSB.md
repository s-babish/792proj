---
output:
  html_document: default
  pdf_document: default
---
# Sage Babish and Victoria Peechatt Final Project
## NumPy, pandas, data cleaning and visualization  

<br>

### We used Pandas and NumPy to clean and extract data from our datasets. 

#### Peechatt has three 20+ year datasets with caterpillar, host plant, and other data. 
- First, I imported the datasets. 
- I cleaned the data, and extracted the columns I wanted to look at further. 
- I've used the data before to calculte the host breadth of the species that were collected. Previously, I manually went through the excel, sorted by lep species name, and counted the unique number of host plants. But with pandas and numpy, it took 4 lines of code! 
- I used matplotlib to make figures of species richness, rank abundance, etc. for the sites. 


**import packages & check required datasets**

```python
import os
import numpy as np
import pandas as pd
```
