import pandas as dataframes

import plotly.express as graphs
import plotly

from dash import html


def create_example_dataframe():
    return dataframes.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
        }
    )

def create_example_barchart(dataframe):
    return graphs.bar(dataframe, x="Fruit", y="Amount", color="City", barmode="group")

def create_example_header():
    return html.H1("Hello Dash")

def create_example_div():
    return html.Div("Dash: A web application framework for Python.")
