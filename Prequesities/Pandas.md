# Pandas
- Loading data from dataset should be an automatic reflex

## Manual Data loading
![Streched](/home/iliass/Pictures/Pthon/Preq/S3L13.png)
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
## Selecting Rows and columns
### Column
```python
M = X.as_matrix()
type(M) # numpy.ndarray

X[0] # returns the column 0
type(X[0]) # pandas.core.series.Series
```
 - Pandas data frames are for **2D objets**
 - Panadas series for **1D objects**
 ### Rows
 ```python
X.iloc[0] # row 0
X.ix[0] # row 0

X[X[0]<5] # rows where X[0] < 5 with same nbr of rows as datafram
X[0] < 5 # serie with true , true , false ....
type(X[0] < 5) # pandas.core.series.Series
```
### Columns name
```python
df = pd.read_csv("file_name",engine="python" , skipfooter=3) # skip footer is number of lines at bottom to skip  (unspported with engine = 'c')

df.columns = ["months" ,"passengers"] #to change columns names
df.columns # to see new columns name 
df['ones'] =1 # add new column names 'ones' with 1s

df.ones # to see the new serie of ones
```

## The apply() function
![Streched](/home/iliass/Pictures/Pthon/Preq/S3L17.png)
![Streched](/home/iliass/Pictures/Pthon/Preq/S3L17-2.png)
![Streched](/home/iliass/Pictures/Pthon/Preq/S3L17-3.png)

```python
from datetime import datetime
datetime.strptime("1949-05","%Y-%m") 
df['dt'] = df.apply(lambda row: datetime.strptime(row['month'],"%Y-%m"), axis=1)

df.info() # df.dt contain datetime objects

```
## Joins
![Streched](/home/iliass/Pictures/Pthon/Preq/S3L18.png)
```python
t1 = read_csv("table1.csv")
t2 = read_csv("table2.csv")
m = pd.merge(t1,t2,on = "user_id")

```