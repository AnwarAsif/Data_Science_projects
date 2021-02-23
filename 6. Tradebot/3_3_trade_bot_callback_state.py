import dash
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from datetime import datetime
import plotly.graph_objs as go
import requests
import json
import os

style = ['/assets/stylesheet.css']
app = dash.Dash(__name__, external_stylesheets= style)

app.layout = html.Div([

    html.Div([
        html.H2("Trade Bot"),
        html.Img(src='/assets/Robot.png')
    ], className="banner"),
    
    html.Div([
        dcc.Input(id='symbol-input', value='ETHUSDT', type='text'),
        html.Button(id="sumbit-button", n_clicks=0, children='Submit')
    ]),



    html.Div([
        html.Div([

            dcc.Graph(
                id='graph_close',
            ),
        ], className="six columns"),
    ], className="row"),
])

app.css.append_css({
    'external_url':'/assets/bWLwgP.css'
})

@app.callback(Output('graph_close', 'figure'),
              [Input("sumbit-button", "n_clicks")],
              [State('symbol-input', 'value')])

def update_fig(n_clicks, input_value):

    symbol = input_value
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

    data =[]
    trace_close = go.Scatter(x=list(df.index),
                             y=list(df.close),
                             name="Close",
                             line=dict(color='#f44242'))

    data.append(trace_close)
    layout = {'title': symbol}

    fig = {"data": data,"layout":layout}

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
