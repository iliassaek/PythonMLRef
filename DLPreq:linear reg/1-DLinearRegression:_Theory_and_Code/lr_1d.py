import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#load the data
X = []
Y = []

M = pd.read_csv("data_1d.csv", header = None).as_matrix()

X = M[:,0]
Y = M[:,1]

# try to plot the data

plt.scatter(X,Y)

denominator = X.dot(X) - X.sum()*X.mean()

a = (X.dot(Y) - X.sum()*Y.mean())/denominator

print(a)
b = (X.dot(X)*Y.mean() -X.mean()*X.dot(Y))/denominator 

yhat = a*X + b

plt.plot(X,yhat)

plt.show()

# tesCalculating R2
d1 = Y - yhat
d2 = Y - Y.mean()

r2 = 1 - d1.dot(d1)/d2.dot(d2)

print ("the r2 squared is ", r2)

