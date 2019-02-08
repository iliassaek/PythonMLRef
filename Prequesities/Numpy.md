# Numpy

## List vs Array

### Declaring an Array
```python
ipython
import numpy as np
A = np.array([1,2,3])
```

### Declaring a list
```python
L = [1,2,3]
```
Addidtion in numpy does addition
```python
A+A #array([2,4,6])
```
Addition in lists does concatenation
```python
L+L #[1,2,3,1,2,3]
```
- We can consider np.array as a vector
- We can consider list as a table
- we can use loop in list . but we should always avoid loops because they are too slow !!

```python
np.log(A) #array([0,0.69,1.09])
```

## Dot Product1
![Streched](/home/iliass/Pictures/Pthon/Preq/S2l5-1.png)
```python
a =  np.array([1,2])
(a*a).sum()
np.sum(a*a)
np.dot(a,a)
a.dot(b)
b.dot(a)
```

### amg
```python
amag = np.sqrt((a*a).sum())
amag = np.linalg.norm(a) 
```
![Streched](/home/iliass/Pictures/Pthon/Preq/s2l5-2.png)
```python
a = np.array([1,2])
b = np.array([2,1])
cosangle = a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b))
angle = np.arccos(cosangle) #in radiant
```
-----------------
## Matrix

It is recommended to work with arrays than matrix

There are 1D arrays and 2D arrays .

```python
M = np.array([[1,2],[3,4]])
```

## Generating arrays of data
O = np.ones((10,10))
Z = np.zeros((10,10))
U = np.random.random((10,10)) # Uniform distribution
G = np.random.randn(10,10) #gaussian distribtuion
G.mean() # mean
G.var() # variance

## Matrix product 
![Streched](/home/iliass/Pictures/Pthon/Preq/S2L9-1.png)

## Matrix operations
for diag if input : 2D then output : 1D
if input : 1D then output 2D
### inter & outer product
```python
a = np.array([1,2])
b = np.array([1,4])

a.dot(b) # 9
np.outer(a,b) #array([[1,4],
              #       [2,8]])
np.inner(a,b) # 9
```
### Trace
```python
A = np.array([a,b])
np.trace(A)
```

### covariance of sample in multidimentional space
```python
X = np.random.randn(100,3) #100 samples and 3 features

covX = np.cov(X.T) ## don't forget transpose please
covX.shape # 3
```

### Eigenvalues and Eigenvectors
![Streched](/home/iliass/Pictures/Pthon/Preq/S2L10-2.png)
```python
np.linalg.eigh(covX) ## eig values with the same eig vectore in columns
np.linalg.eig(covX) ## order may be not the same
```

![Streched](/home/iliass/Pictures/Pthon/Preq/S2L10-3.png)

## Solving Linear Systems

![Streched](/home/iliass/Pictures/Pthon/Preq/S2L11-1.png)

![Streched](/home/iliass/Pictures/Pthon/Preq/S2L11-2.png)

you should alwayse solve rather tha inv .

## Example of solving linear problem
![Streched](/home/iliass/Pictures/Pthon/Preq/S2L12-1.png)
![Streched](/home/iliass/Pictures/Pthon/Preq/S2L12-2.png)