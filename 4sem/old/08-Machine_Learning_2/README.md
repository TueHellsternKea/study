[Home](modul-4-2.md)
# Machine Learning 2
- 11-10-2022 - Fredag

# Agenda
- Bernoulli
- Curvex data

# Bernoulli
Bernoulli Naive Bayes is one of the variants of the Naive Bayes algorithm in machine learning. It is very useful to be used when the dataset is in a binary distribution where the output label is either present or absent (*0 or 1*).

- Is it possible to detect stress from text string on the internet - *In a chat for example* - with machine Learning?
- It it possible to detect hatefully language on Twitter?
- Can you use ML to detect spam?

## Example Stress
Stress detection with machine learning from text strings. The dataset for this task contains data posted on subreddit's related to mental health. 

This dataset contains various mental health problems shared by people about their life. This dataset is labelled as 0 and 1, where 0 indicates no stress and 1 indicates stress.

The data is: [stress_csv.csv](./code/stress_csv.csv)

I have used Jupyter Lab for this - [DetectStress.ipynb](./code/DetectStress.ipynb)

## Example Twitter
Use the Bernoulli algorithm for detection of the language on Twitter.

Data is in [twitter.csv](../07-Machine_Learning_2/code/twitter.csv)

## Example Spam
This example look's at the text in the csv file: [spam.csv](./spam.csv)

The text is labeled in the colum class with:

- ham = Not spam
- spam = Spam

### Test of the algorithm 

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("spam.csv", encoding= 'latin-1')
data = data[["class", "message"]]

x = np.array(data["message"])
y = np.array(data["class"])

cv = CountVectorizer()
x = cv.fit_transform(x)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.33, random_state=42)

model = BernoulliNB(binarize=0.0)
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))
```

# Curvex
The Curvex case.

## Test device
I have the device if you would like to test it

## Data
You can get the Curvex data on Fronter as a zip file.


## Use Python for data import
The Curvex data is located in different csv files in different folders.

Create Python code there can combine the different csv files.