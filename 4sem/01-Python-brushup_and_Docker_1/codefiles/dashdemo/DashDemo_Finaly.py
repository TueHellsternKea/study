 
import dash
from dash import dcc
from dash import html
#from dash import Label
from pandas.io.formats import style
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("./life_expectancy.csv")

colors = {"background": "#011833", "text": "#7FDBFF"}

app.layout = html.Div(
    [   
        # Dropdown to filter developing/developed country.
        html.Div(
            [
                dcc.Dropdown(
                    id="status-dropdown",
                    options=[{"label": s, "value": s} for s in df.Status.unique()], # Create available options from the dataset
                ),
            ]
        ),
        # Dropdown to filter countries with average schooling years.
        html.Div(
            [
                dcc.Dropdown(
                    id="schooling-dropdown",
                    options=[
                        {"label": y, "value": y}
                        for y in range(
                            int(df.Schooling.min()), int(df.Schooling.max()) + 1
                        )
                    ], # add options from the dataset.
                ),
            ]
        ),
        # Placeholder to render teh chart.
        html.Div(dcc.Graph(id="life-exp-vs-gdp"), className="chart"),

        # Slider to select year.
        dcc.Slider(
            "year-slider",
            min=df.Year.min(),
            max=df.Year.max(),
            step=None,
            marks={year: str(year) for year in range(df.Year.min(), df.Year.max() + 1)}, # set markers at one year interval.
            value=df.Year.min(),
        ),
    ],
)


@app.callback(
    Output("life-exp-vs-gdp", "figure"),
    Input("year-slider", "value"),
    Input("status-dropdown", "value"),
    Input("schooling-dropdown", "value"),
)
def update_figure(selected_year, country_status, schooling):
    filtered_dataset = df[(df.Year == selected_year)]

    if schooling:
        filtered_dataset = filtered_dataset[filtered_dataset.Schooling <= schooling]

    if country_status:
        filtered_dataset = filtered_dataset[filtered_dataset.Status == country_status]

    fig = px.scatter(
        filtered_dataset,
        x="GDP",
        y="Life expectancy",
        size="Population",
        color="continent",
        hover_name="Country",
        log_x=True,
        size_max=60,
    )

    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)