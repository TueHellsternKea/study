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

## initialize the app and set the theme to Flatly. 
## Theme sets the color combinations and style of the elements such as data cards. 
app = dash.Dash(external_stylesheets = [ dbc.themes.FLATLY],)

body_app = dbc.Container([
    
     dbc.Row([
         
         # 1st column covering 6 columms for big size screens
         dbc.Col(
              dcc.Graph(id = 'trend', figure = top5_products()), # end of graph component
             style = {'height':'450px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6
                ),
         
         # 2nd column coving 6 columns for big size screens
          dbc.Col(
              dcc.Graph(id = 'regions', figure = top5_customers()),
              style = {'height':'450px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6
              ),         
         ]), 
    
],fluid = True)  # Using Fluid = True, components occupy the empty space   

# Dash layout
app.layout = html.Div(id = 'parent', children = [body_app])

if __name__ == "__main__":
    app.run_server()