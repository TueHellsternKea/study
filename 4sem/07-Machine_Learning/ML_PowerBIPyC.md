# Machine Learning in Power BI using PyCaret

## Setting up the Environment
Before we start using PyCaret’s machine learning capabilities in Power BI we have to create a virtual environment and install PyCaret.

Create a virtuel environment see this guide: [/Using Jupyter Lab in Virtual Environment](./Using_Jupyter_Lab_in_Virtual_Environme.md)

## Set Python Directory in Power BI
The virtual environment created must be linked with Power BI. This can be done using Global Settings in Power BI Desktop:

    File → Options → Global → Python scripting

Use the path from the Virtuel Environment you just created.

![](./image/power_bi_path.jpg)

# Clustering in Power BI
Clustering is a machine learning technique that groups data points with similar characteristics. These groupings are useful for exploring data, identifying patterns and analyzing a subset of data. Some common business use cases for clustering are:

- Customer segmentation for the purpose of marketing.
- Customer purchasing behavior analysis for promotions and discounts.
- Identifying geo-clusters in an epidemic outbreak such as COVID-19.

In this tutorial we will use **jewellery.csv** file that is available on PyCaret’s github repository. 

You can load the data using a web connector. 

    Power BI Desktop → Get Data → From Web

Link to csv File: https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/jewellery.csv

![](./image/filelink.jpg)

## K-Means Clustering
To train a clustering model we will execute Python script in Power Query Editor

    Power Query Editor → Transform → Run python script

![](./image/powerquery_python.jpg)

Run the following code as a Python script:

```python
from pycaret.clustering import *
dataset = get_clusters(data = dataset)
```

![](./image/python_script.jpg)

# Anomaly Detection in Power BI
Anomaly Detection is a machine learning technique used for identifying rare items, events, or observations by checking for rows in the table that differ significantly from the majority of the rows. Typically, the anomalous items will translate to some kind of problem such as bank fraud, a structural defect, medical problem or error. Some common business use cases for anomaly detection are:

- Fraud detection (credit cards, insurance, etc.) using financial data.
- Intrusion detection (system security, malware) or monitoring for network traffic surges and drops.
- Identifying multivariate outliers in the dataset.

In this tutorial we will use **anomaly.csv** file available on PyCaret’s github repository. 

You can load the data using a web connector

    Power BI Desktop → Get Data → From Web

Link to csv file: https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/anomaly.csv