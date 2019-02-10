# Introduction

* If you can't implement something in code , It means that you didn't understand it at all .

## Classification
2-1
### Types of Data
* There are two common types of Daata
    1. Images
    1. Text
* The entire Internet is mostly made up of these 2 things 

### Example of Classification
#### Text Example : Spam Detection 
* **Input :** Email **Output:** Spam or not Spam  
#### Buisness Example : Online Ads
* **Inputs:** Age , Gender ,  Location , you searched "best sunglasses for running" 
* **Output :** will you click this add yes/ no
* *Binary* Classification 

### Learning
* We're given a dataset on which to train 
* It consists of **input** data and **targets** ( aka labels)
* Given many examples we figure out the pattern 

### Useful abstraction 
* 2 useful things a blackbox can do 
1. Learn
    * Figure out the patern between input and output
1. Predict
    * Label new things it has never seen before(e.g tomorrow's emails !!!)

### Evaluation
* How do we know the the model has learned something useful ?
* Measure it *accuracy* (classification rate)
        Accuracy = # correct/#total
* In code
```python
model.score(x,y)
```
