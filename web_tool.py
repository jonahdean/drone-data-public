import dash
from dash.dependencies import Input, Output, State
import pandas as pd
from dash import dash_table, dcc, html
from flask import Flask
import dash_bootstrap_components as dbc

from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

# import dash_bootstrap_components as dbc

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


url_base = '/assembly_tree/'
server = Flask(__name__, static_url_path='/static')
app = dash.Dash(__name__, server=server, url_base_pathname=url_base)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.title = 'DSS Apps'

# static file locations
# path_pre = '/Users/jonahbuckingham-cain/PycharmProjects/pythonProject/venv/static/'
path_pre = 'venv/static/'
pilot_count = path_pre +'pilot_count.csv'
df_pilot=pd.read_csv(pilot_count)
# app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
            dcc.Input(id='zip code', placeholder='Enter Zip Code'),
            dcc.Input(id='radius', placeholder='Enter Radius'),
            html.Button('Look-Up', id='search', n_clicks=0),
            html.H1(id='result'),
    ])
])

@app.callback(
    Output('result', 'children'),
    Input('search', 'n_clicks'),
    [State('zip code', 'value'),
     State('radius', 'value')]
)
def update_result(k, x, y):
    print(k)
    print(x)
    print(y)
    if k==0:
        print('None ', k)
        return None

    in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(x, float(y))]  # ('ZIP', radius in miles)
    radius_utf = [t.encode('UTF-8') for t in in_radius]  # unicode list to utf list
    # print(in_radius)
    # print(radius_utf)
    pilot_sum = df_pilot['count'].loc[df_pilot['zip'].isin(in_radius)].sum()
    return pilot_sum


if __name__ == '__main__':
    # app_port = 5001
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0", port=app_port)