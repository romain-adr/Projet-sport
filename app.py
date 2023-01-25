from dash import Dash, html, dcc
import plotly.graph_objs as go
import pandas as pd

app = Dash(__name__)

stats = pd.read_excel('stats.xlsx')

fig = go.Figure(data=[go.Scatter(x=stats['date'], y=stats['Poids'])])

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dashboard push.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)