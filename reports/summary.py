import plotly.express as px
from dash import html, dcc

DATASETS = ["linelist"]


def generate_report(linelist):
    # Histogram of Age
    fig_age = px.histogram(linelist, x="Age", title="Age distribution")

    # Plot Days to Recovery vs Age
    fig_age_recovery = px.scatter(
        linelist, x="Age", y="Days to Recovery", title="Days to recovery vs Age"
    )

    # Return a dash div containing the summary of the dataset
    return html.Div(
        [
            html.H1("Summary"),
            html.H2("Table: 'linelist'"),
            html.Div(["Number of rows: ", html.B(f"{len(linelist)}")]),
            html.Div(["Number of columns: ", html.B(f"{len(linelist.columns)}")]),
            html.Div(["Columns: ", html.B(f"{', '.join(linelist.columns)}")]),
            html.Div(["Missing values: ", html.B(f"{linelist.isnull().sum().sum()}")]),
            # Plot histogram of age next to scatter plot of age vs days to recovery
            html.H3("Plots"),
            html.Div(
                [
                    dcc.Graph(figure=fig_age),
                    dcc.Graph(figure=fig_age_recovery),
                ],
                style={"display": "flex", "flexDirection": "row"},
            ),
            # Table preview
            html.Div(["Missing values by column:"]),
            html.Table(
                [
                    html.Thead(html.Tr([html.Th("Column"), html.Th("Missing values")])),
                    html.Tbody(
                        [
                            html.Tr(
                                [html.Td(col), html.Td(linelist[col].isnull().sum())]
                            )
                            for col in linelist.columns
                        ]
                    ),
                ]
            ),
            html.Br(),
            html.P("First 5 rows:"),
            html.Table(
                [
                    html.Thead(html.Tr([html.Th(col) for col in linelist.columns])),
                    html.Tbody(
                        [
                            html.Tr(
                                [
                                    html.Td(linelist[col].iloc[i])
                                    for col in linelist.columns
                                ]
                            )
                            for i in range(5)
                        ]
                    ),
                ]
            ),
        ]
    )
