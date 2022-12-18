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

    assert test_bar_chart is not None
