import dash
from dash import dcc
from dash import html
#from dash import Label
from pandas.io.formats import style
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output



df = pd.read_csv("./life_expectancy.csv")

min=df.Year.min()


print(min)