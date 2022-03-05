# Dash demo 
# Tue Hellstern
# Version 2

# Import
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc # https://dash-bootstrap-components.opensource.faculty.ai/
import plotly.express as px
import pandas as pd

# Dash app
app = dash.Dash()

# Data import til Pandas dataframes
EmployessSale = pd.read_excel("test_2.xlsx", "EmployessSale")
CategoryeSale = pd.read_excel("test_2.xlsx", "CategoryeSale")
Top5Products = pd.read_excel("test_2.xlsx", "Top5Products")
Top5Customers = pd.read_excel("test_2.xlsx", "Top5Customers")

def top5_products():
    fig = px.bar(Top5Products, x='Products', y='Total')
    return fig

def top5_customers():
    fig = px.bar(Top5Customers, x='Customers', y='Total')
    return fig

def employesssale():
    fig = px.bar(EmployessSale, x='Employess', y='Total')
    return fig    

def categorysale():
    fig = px.bar(CategoryeSale, x='Category', y='Total')
    return fig


## initialize the app and set the theme to Flatly. 
## Theme sets the color combinations and style of the elements such as data cards. 
app = dash.Dash(external_stylesheets = [ dbc.themes.FLATLY],)

body_app = dbc.Container([
    
    dbc.Row([
        # 1 column, 1 row, covering 6 columms
        dbc.Col(
            dcc.Graph(id = 'top5products', figure = top5_products()), # end of graph component
            style = {'height':'450px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
         
        # 2 column, 1 row, coving 6 columns 
        dbc.Col(
            dcc.Graph(id = 'top5customers', figure = top5_customers()),
            style = {'height':'450px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),         
    ]), 

    dbc.Row([
        # 1 column, 2 row, coving 6 columns 
        dbc.Col(
            dcc.Graph(id = 'employessales', figure=employesssale()),
            style = {'height':'450px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),

        # 2 column, 2 row, coving 6 columns 
        dbc.Col(
            dcc.Graph(id = 'categorysale', figure=categorysale()),
            style = {'height':'450px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
    ]),

],fluid = True)  # Using Fluid = True, components occupy the empty space   

# Dash layout
app.layout = html.Div(id = 'parent', children = [body_app])

# Run app
if __name__ == "__main__":
    app.run_server()