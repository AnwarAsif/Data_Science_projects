import dash
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from datetime import datetime
import plotly.graph_objs as go
import requests
import json
import os

symbol ='ETHUSDT'
base = 'https://api.binance.com'
endpoint = '/api/v3/klines'
params = '?&symbol='+symbol+'&interval=1h'
url = base + endpoint + params
data = requests.get(url).text
dictionary = json.loads(data)
df = pd.DataFrame.from_dict(dictionary)
df = df.drop(range(6,12), axis=1)
col_names = ['time','open','high','low','close','volume']
df.columns = col_names
for col in col_names:
  df[col] = df[col].astype(float)

trace_close = go.Scatter(x=list(df.index),
                         y=list(df.close),
                         name="Close",
                         line=dict(color='#f44242'))

trace_high = go.Scatter(x=list(df.index),
                         y=list(df.high),
                         name="Close",
                         line=dict(color='#f44242'))
style = ['/assets/stylesheet.css']
app = dash.Dash(__name__, external_stylesheets= style)

app.layout = html.Div([
    html.Div([
        #dcc.Input(id='symbol-input', value='ETHUSDT', type='text')
    ]),

    html.Div([
        html.H2("Trade Bot"),
        html.Img(src='/assets/Robot.png')
    ], className="banner"),

    html.Div([
        html.Div([
            html.H3('Column 1'),

            dcc.Graph(
                id='graph_close',
                figure={
                    "data":[trace_close],
                    "layout":{
                        "title":"Close Graph"
                    }
                }
            ),
        ], className="six columns"),
        html.Div([
            html.H3('Column 2'),
            dcc.Graph(
                id='graph_high',
                figure={
                    "data":[trace_high],
                    "layout":{
                        "title":"High Graph"
                    }
                }
            ),
        ], className="six columns"),
    ], className="row"),
])

app.css.append_css({
    'external_url':'/assets/bWLwgP.css',
})

#@app.callback(Output('graph_close', 'figure'), Input('symbol-input', 'value'))

if __name__ == "__main__":
    app.run_server(debug=True)
