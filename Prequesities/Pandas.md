# Pandas
- Loading data from dataset should be an automatic reflex

## Manual Data loading
![Streched](/assets/S3L13.png)
- Data can be semi-structured (data collected by a server)
- Data can be structured (kaggle)
```python
ipyhton
X = []
import numpy as np

for line in open("data2_2d.csv"):
  row = line.split(',')
  #cast row into float and load it in sample
  sample = map(float,row)
  X.append(sample)

#convert into numpy array
X = np.array(X)
X.shape # (100,3)
```  

## Data Frames
```python
import pandas as pd
X = pd.read_csv("data_2d.csv",header=None)
type(X) # pandas.core.frame.DataFrame
X.info() # it tells us if there is other row types , if you have only one String in cell it will return String
X.head() # print few first rows
X.head(10) # print 10 fst rows
```
