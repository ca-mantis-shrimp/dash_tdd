import app

import pandas as dataframes
import plotly.express as graphs

def create_test_dataframe():
    return dataframes.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
        }
    )


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

