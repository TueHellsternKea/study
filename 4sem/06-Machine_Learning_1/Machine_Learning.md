---
title: Machine Learning
theme: gaia
_class: lead
paginate: true
marp: true
backgroundColor: #fff
size: 4K
@auto-scaling true
markdown.marp.enableHtml
---

![bg 125%](https://github.com/officegeek/image/raw/main/ml.jpg)

---

# NEW
- https://github.com/ryantcullen/stock-bot
---

<!-- _class: invert -->
# Machine Learning is the process of creating models that can perform a certain task without the need for a human explicitly programming it to do something

---

![bg right:20% 110%](https://github.com/officegeek/image/raw/main/Artificial_Intelligence_2.jpg)
Your smartphone, your house, your car, and your bank all use **artificial intelligence** on a daily basis.

Sometimes it’s **easy to understand**, when you ask Siri, Cortana or OK Google to get you directions. 

Sometimes it’s **less obvious**, like when you make an abnormal purchase on your credit card and don’t get a fraud alert from your bank. 

**AI**, **ML** and **DL** are everywhere and Data Science is the interdisciplinary field of methods to extract the knowledge needed. 

## These technologies are making a huge difference in our lives every day and evolving fast by a magnitude of people working to improve them consistently.

---

![bg right:30% 90%](https://github.com/officegeek/image/raw/main/ai_ml_dl_2.png)
# Definitions

**Artificial Intelligence** (*AI*) refers to the **simulation of human intelligence** processes by machines, including learning, reasoning and self-correction

**Machine learning** (*ML*) is an application of *AI* generating systems that can learn and **improve without being programmed**

**Deep Learning** (DL) is a subset of Machine Learning and Artificial Intelligence. The term refers to a **particular approach** used for creating and training neural networks that are considered highly promising decision-making nodes

---

![bg 100%](https://github.com/officegeek/image/raw/main/ai_ml_dl.png)

<!-- _footer: medium.com -->

---

# Machine Learning algorithms 

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

---

![bg 95%](https://github.com/officegeek/image/raw/main/Learning.jpg)

---

![bg 98%](https://github.com/officegeek/image/raw/main/Use-Case-Machine-Learning.png)

---

<!-- _class: invert -->
# Supervised Learning <!--fit-->

---

# Supervised Learning
The area of Machine Learning where you have a **set of independent variables** which helps you to analyse the **dependent variable** and the **relation between them**

Whatever you want to predict is called as **Dependent Variable**, while variables that you use to predict are called as **Independent Variables**

    You want to predict the age of the person 
    based on the person’s height and weight, 
    then height and weight will be the independent 
    variables, while age will be the dependent variable

Supervised learning is the most popular paradigm for machine learning.
It is the easiest to understand and the simplest to implement

---

# Types of Supervised Learning
Supervised Learning can be classified into 2 types

- Regression
- Classification

---

# Regression
Regression is the kind of Supervised Learning that learns from the Labelled Datasets and is then able to predict a continuous-valued output for the new data given to the algorithm.

It is used whenever the output required is a number such as money or height etc. 

- Linear Regression 
- Logistic Regression
 
---

![bg right:30% 90%](https://github.com/officegeek/image/raw/main/Linear-Regression.png)
# Linear Regression
This algorithm assumes that there is a linear relationship between the 2 variables, Input (X) and Output (Y), of the data it has learnt from. The Input variable is called the Independent Variable and the Output variable is called the Dependent Variable. 

When unseen data is passed to the algorithm, it uses the function, calculates and maps the input to a continuous value for the output.

---

![bg right:60% 100%](https://github.com/officegeek/image/raw/main/Linear-Regression-Example.png)
# Linear Regression Python

<!-- _footer:   Linear_Regression_Good.ipynb and  Linear_Regression_Bad.ipynb-->

---

![bg right:30% 90%](https://github.com/officegeek/image/raw/main/Logistic-Regression.png)
# Logistic Regression
This algorithm predicts discrete values for the set of Independent variables that have been passed to it.

It does the prediction by mapping the unseen data to the logit function that has been programmed into it. 

The algorithm predicts the probability of the new data and so it’s output lies between the range of 0 and 1.

---

# Classification
Classification is the kind of machine learning where the algorithm needs to **map the new data** that is obtained to any one of the **2 classes that you have in the dataset**. 

The classes need to be **mapped to either 1 or 0 **which in real-life translated to *Yes* or *No*, *Rains* or *Does Not Rain*

The output will be **either one of the classes and not a number** as it was in Regression.

- Decision Tree
- Naive Bayes Classifier
- Support Vector Machines

---

![bg right:30% 100%](https://github.com/officegeek/image/raw/main/Decision_Tree.png)
# Decision Tree
Decision Trees classify based on the feature values. They use the method of Information Gain and find out which feature of the dataset gives the best of information, make that as the root node and so on till they are able to classify each instance of the dataset.

Every branch in the Decision Tree represents a feature of the dataset. They are one of the most widely used algorithms for classification.

---

# Naive Bayes Classifier
Naive Bayes algorithms assume that the features of the dataset are all independent of each other.

Works great on large datasets.

---

![bg right:40% 100%](https://github.com/officegeek/image/raw/main/Support-Vector-Machine.png)
# Support Vector Machines
Support Vector Machines algorithms are based on the statistical learning theory of *Vapnik.*

They use Kernal functions which are a central concept for most of the learning tasks. 
These algorithms create a hyper-plane that is used to classify the two classes from each other.

<!-- _footer: Vapnik–Chervonenkis theory - https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory -->

---

![bg right:25% 120%](https://github.com/officegeek/image/raw/main/house.jpg)
# Supervised Learning - Example

## Predicting house prices
First, we need data about the houses: *square footage, number of rooms, features, whether a house has a garden or not, and so on*. 

We then need to know the prices of these houses, i.e. the corresponding labels.

By leveraging data coming from thousands of houses, their features and prices, **we can now train a supervised machine learning model to predict a new house’s price** based on the examples observed by the model. 

---




![bg right:60% 80%](https://github.com/officegeek/image/raw/main/Logistic_Regression.png)
# Logistic Regression Python

<!-- _footer:   Logistic_Regression_Application.ipynb and  Logistic_Regression_Diabetes.ipynb -->

---

<!-- _class: invert -->
# Unsupervised Learning <!--fit-->

---

# Unsupervised Learning
You **don’t have any dependent variable**. You just have collection of variables and try to find out similarity between them and classify them into clusters

---

# Unsupervised Learning - Examples
- Customer segmentation, or understanding different customer groups around which to build marketing or other business strategies
- Recommender systems, which involve grouping together users with similar viewing patterns in order to recommend similar content.
- Anomaly detection, including fraud detection or detecting defective mechanical parts - *predictive maintenance*

---

<!-- _class: invert -->
# Reinforcement Learning <!--fit-->

---

# Reinforcement Learning
It is the training of machine learning models to make a sequence of decisions.

The *machine* learns to achieve a goal in an uncertain, potentially complex environment. The *machine* employs trial and error to come up with a solution to the problem.

---

# Reinforcement Learning - Example
Facebook has developed an open-source reinforcement learning platform — Horizon. 
The platform uses reinforcement learning to optimize large-scale production systems.

**Facebook has used Horizon internally**

- To personalize suggestions
- Deliver more meaningful notifications to users
- Optimize video streaming quality

**Read more**
- https://engineering.fb.com/ml-applications/horizon
- https://research.fb.com/publications/horizon-facebooks-open-source-applied-reinforcement-learning-platform

---

![bg 67%](https://github.com/officegeek/image/raw/main/Types_of_ML.png)

---

# Link
- https://www.ibm.com/cloud/learn/unsupervised-learning

