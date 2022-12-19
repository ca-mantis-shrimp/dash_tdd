import app

import pandas as dataframes
import plotly.express as graphs
from dash import dcc, html

def create_test_dataframe():
    return dataframes.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
        }
    )

def create_test_plotly_barchart():
    graphs.bar(create_test_dataframe(), x="Fruit", y="Amount", color="City", barmode="group")

def create_test_dash_barchart():
    return dcc.Graph(id="example-graph", figure=create_test_plotly_barchart())


def test_example_dataframe_creation():
    test_dataframe = app.create_example_dataframe()

    app.dataframes.testing.assert_frame_equal(
        test_dataframe,
        dataframes.DataFrame(
            {
                "Fruit": [
                    "Apples",
                    "Oranges",
                    "Bananas",
                    "Apples",
                    "Oranges",
                    "Bananas",
                ],
                "Amount": [4, 1, 2, 2, 4, 5],
                "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
            }
        ),
    )

def test_example_bar_chart():
    test_dataframe = create_test_dataframe()

    test_bar_chart = app.create_example_barchart(test_dataframe)

    assert test_bar_chart.layout.barmode == "group"
    assert test_bar_chart.layout.xaxis.title.text == "Fruit"
    assert test_bar_chart.layout.yaxis.title.text == "Amount"
    assert test_bar_chart.layout.legend.title.text == "City"

def test_example_header():
    test_header = app.create_example_header()

    assert test_header.children == "Hello Dash"

def test_example_div():
    test_div = app.create_example_div()

    assert test_div.children == "Dash: A web application framework for Python."

def test_example_dash_graph():
    test_ploty_barchart = create_test_plotly_barchart()

    test_dash_graph = app.create_example_dash_graph(test_ploty_barchart)

    assert test_dash_graph.figure == test_ploty_barchart

def test_dash_graph_id():
    test_ploty_barchart = create_test_plotly_barchart()

    test_dash_graph = app.create_example_dash_graph(test_ploty_barchart)

    assert test_dash_graph.id == "example-graph"

def test_dash_app():
    test_app = app.create_example_layout()

    assert test_app.children[0].children == "Hello Dash"
    assert test_app.children[1].children == "Dash: A web application framework for Python."
#    assert test_app.children[2] == create_test_dash_barchart()

