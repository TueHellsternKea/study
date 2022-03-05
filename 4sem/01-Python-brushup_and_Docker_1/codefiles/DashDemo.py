# Dash demo 
# Tue Hellstern
# Version 2

# Import
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Dash app
app = dash.Dash()

# Hent data fra GithHub - Pandas
df = pd.read_csv(
    "https://raw.githubusercontent.com/TueHellsternKea/study/main/4sem/01-Python-brushup_and_Docker_1/codefiles/life_expectancy.csv"
)

# Opret Scatter Plot - Plotly
fig = px.scatter(
    df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

# Dash layout
app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])

# Run Dash server - Local - http://127.0.0.1:8050/
if __name__ == "__main__":
    app.run_server(debug=True)