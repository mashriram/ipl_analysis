import pandas as pd
import plotly.express as px


def gapminder(
    df: pd.DataFrame,
    x_col: str | pd.Series,
    y_col: str | pd.Series,
    size_col: str | pd.Series | None = None,
    color_col: str | pd.Series | None = None,
    hover_name: str | None = None,
    title: str = "Gapminder Plot",
    labels: dict | None = None,
) -> None:

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        size=size_col,
        color=color_col,
        hover_name=hover_name,
        title=title,
        labels=labels,
    )
    fig.show()


def parallelplot(
    df: pd.DataFrame,
    columns: list[str | pd.Series],
    color_col: str | pd.Series | None = None,
    title: str = "Parallel Coordinates Plot",
    labels: pd.Series | str | None | dict[str, str] = None,
) -> None:

    fig = px.parallel_coordinates(
        df, dimensions=columns, color=color_col, title=title, labels=labels
    )
    fig.show()
