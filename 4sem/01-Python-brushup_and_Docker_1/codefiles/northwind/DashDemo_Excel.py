# Dash demo 
# Tue Hellstern
# Version 3

# Import
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

############################## Data import #####################
Excel_file = 'data/northwind_data.xlsx'
EmployeesSale = pd.read_excel(Excel_file, "EmployeesSale")
CategorySale = pd.read_excel(Excel_file, "CategorySale")
Top5Products = pd.read_excel(Excel_file, "Top5Products")
Top5Customers = pd.read_excel(Excel_file, "Top5Customers")
########################## End data import #####################

############################# Create charts ####################
def top5_products():
    fig = px.pie(Top5Products, values='Total', names='ProductName', title='Top 5 Products')
    return fig

def top5_customers():
    fig = px.pie(Top5Customers, values='Total', names='CompanyName', title='Top 5 Customers')
    return fig

def employesssale():
    fig = px.bar(EmployeesSale, x='EmployeesName', y='Total', title='Sales by Employees')
    return fig    

def categorysale():
    fig = px.bar(CategorySale, x='CategoryName', y='Total', title='Category Sales')
    return fig
########################### End Create charts ##################

############################## Initialize the App ########################
# Dash app
app = dash.Dash()

# Flatly theme
app = dash.Dash(external_stylesheets = [ dbc.themes.FLATLY],)

body_app = dbc.Container([
    
    dbc.Row([
        # 1 column, 1 row, covering 6 columms
        dbc.Col(
            dcc.Graph(id = 'top5products', figure = top5_products()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
         
        # 2 column, 1 row, coving 6 columns 
        dbc.Col(
            dcc.Graph(id = 'top5customers', figure = top5_customers()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),         
    ]), 

    dbc.Row([
        # 1 column, 2 row, coving 6 columns 
        dbc.Col(
            dcc.Graph(id = 'employeessale', figure=employesssale()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),

        # 2 column, 2 row, coving 6 columns 
        dbc.Col(
            dcc.Graph(id = 'categorysale', figure=categorysale()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
    ]),

],fluid = True)  # Using Fluid   

############################## Diagram setup ########################

############################## Top bar ########################
logo = './assets/Northwind-Logo.gif'

topbar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(html.Img(src = logo, height = "70px"), ),
                dbc.Col(
                    dbc.NavbarBrand("Northwind sales", style = {'color':'black', 'fontSize':'25px','fontFamily':'Times New Roman'}
                    ),
                )
            ],
            align="center",
            className="g-10",
        ),
    ]
)
############################## end of navigation bar ########################

################################ Dash layout ##########################
# Inklusiv navnbar
app.layout = html.Div(id = 'parent', children = [topbar, body_app])
############################## End ash layout ########################

############################## Run App ########################
if __name__ == "__main__":
    app.run_server()