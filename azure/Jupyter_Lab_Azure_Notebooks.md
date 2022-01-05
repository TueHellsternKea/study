[Home](./README.md)

# Jupyter Lab
JupyterLab is a web-based interactive development environment for notebooks, code, data and diagrams - [jupyter.org](https://jupyter.org)

Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning.

You can install Jupyter Lab on your local computer [jupyter.org/install](https://jupyter.org/install) or Azure in the cloud.

There are also the possibility of running Jupyter Lab in your browser - [jupyter.org/try](https://jupyter.org/try)

## Jupyter Lab on Azure Notebooks
There are some advantages of running your Jupyter Notebook on Azure as opposed to your local system.

- **Global access** - You can access your notebooks/repositories anywhere in the world as opposed to your local system
- **Elasticity** - You can use a *lower* compute to run data pre-processing and move to a *higher* compute when you are training a more complex model or using more data
- **Older Hardware** - Whether you are using the *latest* laptop, or an *old thing* from a couple of decades ago, as long as you have a browser you can deploy machine learning models on the Azure cloud
- **Easy to share and collaborate** - With the advantage of pulling and deploying straight from your Github, you can also collaborate and share Jupyter Notebooks
- **The familiarity of Jupyter Notebook** - Jupyter Notebook has been the de facto options for data scientists for some years

## Azure setup
Have a look at this video
<iframe width="560" height="315" src="./video/createjupyterlab.mp4" 
frameborder="0" allow="accelerometer; autoplay=false; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


- Login - [portal.azure.com](https://portal.azure.com)
- Click - **Create a resource**
- Select - **AI + Machine Learning**
- Click - **Create** under Machine Learning
- Project details
    - Subscription
    - Resource group
    - Workspace name
- Click - **Review + create**
- Click - **Create**
- When deployment is *complete* - **Go to resource**
- Click - **Launch studio**
- Select - **Notebooks - Start now**
- In the top select select - **Create compute**
- Create compute instance
    - Configure required setting
    - Compute name
    - Select - **Select from all options**
    - Sort by **Cost**
    - Select the lowest cost - *$0.07/hr - Standard_DS1_v2 1 cores, 3.5GB RAM, 7GB storage*
    - Click - **Create**
- In the section *Quick actions* - Select - **Start with an empty notebook**
- Filename
- File type - **Notebook(*ipynb)**

Your Jupyter Lab server and your fist notebook is created and running

![](https://github.com/TueHellsternKea/study/raw/main/azure/image/azure_jupyter_lab_running.jpg)

