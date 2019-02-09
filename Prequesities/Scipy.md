# Scipy
 
## Gaussian PDF and CDF
![Streched](/home/iliass/Pictures/Pthon/Preq/S5L23-1.png)

>Given a sample of a random variable what is its probability density ??

     PDF = Probability density function
     you should always use scipy because it's too fast

![Streched](/home/iliass/Pictures/Pthon/Preq/S5L23-2.png)

```python
from scipy.stats import norm

norm.pdf(0) #0.39 which is f(0)

norm.pdf(0 , loc = 5 , scale=10) # mean and sigma it's not variance
#0.0352
```
> We can calculate pdf pf multiple values at the same time 


```python
import numpy as np 

r = np.random.randn(10)
norm.pdf(r) # array

```

![Streched](/home/iliass/Pictures/Pthon/Preq/S5L23-3.png)
```python
norm.logpdf(r)
norm.cdf(r) # integral from -00 to x
norm.logcdf(r) # log of integral 
```

## Sampling form a gaussian distribution (1-D)

>form this
![Streched](/home/iliass/Pictures/Pthon/Preq/S5L24-1.png) 
  to this
>  ![Streched](/home/iliass/Pictures/Pthon/Preq/S5L24-2.png)
>  
```python
r = 10*np.random.randn(10000) + 5 #standard deviation = 10 and mean=5

plt.hist(r, bins=100)
plt.show()
```
## Sampling from a Gaussian Distribution (Spherical and Axis-aligned Elliptical)

```python
import numpy as np
r =np.random.randn(10000,2)
plt.scatter(r[:,0],r[:,1])
plt.axis("equal")
plt.show()
```
![Streched](/home/iliass/Pictures/Pthon/Preq/S5L25-1.png)

```python
import numpy as np
r = np.random.randn(10000,2)
plt.scatter(r[:,0],r[:,1])
plt.axis("equal")
plt.show()
```
![Streched](/home/iliass/Pictures/Pthon/Preq/S5L25-2.png)