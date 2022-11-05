import dash
from dash.dependencies import Input, Output, State
import pandas as pd
from dash import dash_table, dcc, html
from flask import Flask
import dash_bootstrap_components as dbc


url_base = '/assembly_tree/'
server = Flask(__name__, static_url_path='/static')
app = dash.Dash(__name__, server=server, url_base_pathname=url_base)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.title = 'DSS Apps'

app.layout = html.Div([
    html.Div([

            html.H1("Hello World", id='result'),
    ])
])


if __name__ == '__main__':
    # app_port = 5001
    app.run(debug=True)