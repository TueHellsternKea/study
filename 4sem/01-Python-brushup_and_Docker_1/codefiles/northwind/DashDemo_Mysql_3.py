
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

from mysql_conn import conn_open

app = Dash(__name__)


app.layout = html.Div([
    html.H5('Northwind'),

    html.Label('Select year'),
    dcc.Dropdown(
        id = 'selectedeyear',
        options=['1996', '1997', '1998'],
    ),

    dcc.Graph(
        style={'height': 300},
        id='my-graph'
    )
])



def getCategorySale():
    conn = conn_open()
    EmployeesSale = pd.read_sql('SELECT * FROM CategorySaleTest;', conn)
    return EmployeesSale

@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)

def update_graph():
    CategorySale = getCategorySale()
    fig = px.bar(CategorySale, x='CategoryName', y='Total', title='Category Sales')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)