# Matplotlib

## Linechart

```python
import matplotlib.pyplot as plt

x = np.linspace(0,10,10) # the start the end how many points
y = np.sin(x)
plt.plot(x,y)
plt.show()

plt.xlabel("Time")
plt.ylabel("Some functione of time")
plt.title("my cool chart")

plt.show()
```


## Scatterplot
- we'll try to fit some raw data
- "cd ./linear_regression_class"
- scatter vs plot : 
  1. scatter draws points without lines connecting them whereas plot may or may not plot the lines , depending on the arguments
  2. scatter allows you to specify a different colour and a different size for each point individually. It is not possible to do that with plot.
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


A = pd.read_csv("data_1d.csv", header=None).as_matrix() # np.darray

x = A[:,0]
y = A[:,1]

plt.scatter(x,y)
plt.show()
```
![Streched](/home/iliass/Pictures/Pthon/Preq/S4L20-1.png)
```python
x_line = np.linspace(0,100,100)
y_line = 2*x_line + 1
plt.scatter(x,y)
plt.scatter(x_line,y_line)

```

![Streched](/home/iliass/Pictures/Pthon/Preq/S4L20-2.png)


## Histogram

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.hist(x)
plt.show()

R = np.random.rand(100000)
plt.hist(R , bins=20)
plt.show()

y_actual = 2*x-1
residuals = y - y_actual
plt.hist(residuals) # should be guassian distributed (AD)
```

## Plotting images
![Streched](/home/iliass/Pictures/Pthon/Preq/S4L22-1.png)
```python
import pandas as pd 
df = pd.read_csv("train.csv")
df.shape # (42000,785)
M = df.as_matrix()
im = M[0 , 1:]
im.shape # (784,)
im = im.reshape(28,28)
im.shape # (28,28)

import matplotlib.pyplot s plt
plt.imshow(im)
plt.show()

# if you wanna gray
plt.imshow(im , cmap='gray')
plt.show()

# black ->white-> black
plt.readimg(255-im , cmap='gray')
plt.show()
```