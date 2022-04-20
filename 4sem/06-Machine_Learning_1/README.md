[Home](modul-4-2.md)
# Machine Learning 1
    - 25-04-2021 - Mandag - DK
    - 26-04-2021 - Tirsdag - INT

# Machine Learning
Machine learning is all around us. From antilock braking systems, to autopilot systems in airplanes and cars, smart speakers, which serve as personal digital assistants, to systems that learn our movie preferences and recommend what to watch next in Netflix.

    Machine Learning is the process of creating models that can perform a certain task without the need for a human explicitly programming it to do something



# Agenda

- Machine Learning in Python
- Scikit-learn
- TensorFlow
- Pandas
- Numpy
- Matplotlib
- Docker

- [Linear Regression](./Linear_Regression.md)

# Definitions
**Artificial Intelligence** (*AI*) refers to the simulation of human intelligence processes by machines, including learning, reasoning and self-correction

**Machine learning** (*ML*) is an application of AI generating systems that can learn and improve without being programmed

**Deep Learning** (*DL*) is a subset of Machine Learning and Artificial Intelligence. The term refers to a particular approach used for creating and training neural networks that are considered highly promising decision-making nodes

![](https://github.com/officegeek/image/raw/main/ai_ml_dl.png)

# Machine Learning algorithms
- [Supervised Learning](#supervised-learning)
- [Unsupervised Learning](#unsupervised-learning)
- [Reinforcement Learning](#reinforcement-learning)

![bg 67%](https://github.com/officegeek/image/raw/main/Types_of_ML.png)

# Supervised Learning
The area of Machine Learning where you have a set of independent variables which helps you to analyse the dependent variable and the relation between them

Whatever you want to predict is called as Dependent Variable, while variables that you use to predict are called as Independent Variables

    You want to predict the **age** of the person 
    based on the person’s **height** and **weight**, 
    then **height** and **weight** will be the **independent** variables, while **age** will be the **dependent** variable

Supervised learning is the most popular paradigm for machine learning. It is the easiest to understand and the simplest to implement.

## Regression
Regression is the kind of Supervised Learning that learns from the Labelled Datasets and is then able to predict a continuous-valued output for the new data given to the algorithm.

It is used whenever the output required is a number such as money or height etc. 

- Linear Regression 
- Logistic Regression


![bg right:30% 90%](https://github.com/officegeek/image/raw/main/Linear-Regression.png)
## Linear Regression
This algorithm assumes that there is a linear relationship between the 2 variables, Input (X) and Output (Y), of the data it has learnt from.

The Input variable is called the Independent Variable and the Output variable is called the Dependent Variable. 

When unseen data is passed to the algorithm, it uses the function, calculates and maps the input to a continuous value for the output.

![bg right:60% 100%](https://github.com/officegeek/image/raw/main/Linear-Regression-Example.png)


## Logistic Regression
This algorithm predicts discrete values for the set of Independent variables that have been passed to it.

It does the prediction by mapping the unseen data to the logit function that has been programmed into it. 

The algorithm predicts the probability of the new data and so it’s output lies between the range of 0 and 1.

![bg right:30% 90%](https://github.com/officegeek/image/raw/main/Logistic-Regression.png)


# Unsupervised Learning
You **don’t have any dependent variable**. You just have collection of variables and try to find out similarity between them and classify them into clusters

## Unsupervised Learning - Examples
- **Customer segmentation**, or understanding different customer groups around which to build marketing or other business strategies
- **Recommender systems**, which involve grouping together users with similar viewing patterns in order to recommend similar content.
- **Anomaly detection**, including fraud detection or detecting defective mechanical parts - predictive maintenance

# Reinforcement Learning
It is the training of machine learning models to make a sequence of decisions.

The *machine* learns to achieve a goal in an uncertain, potentially complex environment. The *machine* employs trial and error to come up with a solution to the problem.

## Reinforcement Learning - Example
Facebook has developed an open-source reinforcement learning **platform — Horizon**. The platform uses reinforcement learning to optimize large-scale production systems.

**Facebook has used Horizon internally**

- To personalize suggestions
- Deliver more meaningful notifications to users
- Optimize video streaming quality

Read more about Horizon
- [engineering.fb.com/ml-applications/horizon](https://engineering.fb.com/ml-applications/horizon)
- [research.fb.com/publications/horizon-facebooks-open-source-applied-reinforcement-learning-platform](https://research.fb.com/publications/horizon-facebooks-open-source-applied-reinforcement-learning-platform)


# Links
- [www.tensorflow.org](https://www.tensorflow.org)