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

from sqlalchemy import create_engine, exc
import configparser

############### Data import - MySQL connection #################
def connect():
    db_conn = None
    try:
        # Read config.ini file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Connect to MySQL
        db_connection_str = config['mysqlini']['conn_string']
        db_conn = create_engine(db_connection_str)
        
        return db_conn

    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        db_conn.dispose() # Close connection

# EmployeesSale
def getEmployeesSale():
    conn = connect()
    EmployeesSale = pd.read_sql('SELECT * FROM EmployeesSale;', conn)
    return EmployeesSale

# CategorySale
def getCategorySale():
    conn = connect()
    CategorySale = pd.read_sql('SELECT * FROM CategorySale;', conn)
    return CategorySale

# Top5Products
def getTop5Products():
    conn = connect()
    Top5Product = pd.read_sql('SELECT * FROM Top5Products;', conn)
    return Top5Product

# Top5Customers
def getTop5Customers():
    conn = connect()
    Top5Customers = pd.read_sql('SELECT * FROM Top5Customers;', conn)
    return Top5Customers

EmployeesSale = getEmployeesSale()
CategorySale = getCategorySale()
Top5Products = getTop5Products()
Top5Customers = getTop5Customers()
########################## End data import #####################

############################# Create charts ####################
def top5_products():
    fig = px.pie(Top5Products, values='Total', names='ProductName', title='Top 5 Products')
    return fig

def top5_customers():
    fig = px.pie(Top5Customers, values='Total', names='CompanyName', title='Top 5 Customers')
    return fig

def employesssale():
    fig = px.bar(EmployeesSale, x='EmployeeName', y='Total', title='Sales by Employees')
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