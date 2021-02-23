import dash
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from iexfinance.stocks import Stock
from iexfinance.refdata import get_symbols
from iexfinance.stocks import get_historical_data
from dateutil.relativedelta import relativedelta
from datetime import datetime
import plotly.graph_objs as go
import requests
import json


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


candle = go.Candlestick(
			x = list(df.index),
			open = list(df.open),
			close = list(df.close),
			high = list(df.high),
			low = list(df.low),
			name = "Candlesticks")

trace_close = go.Scatter(x=list(df.index),
                         y=list(df.close),
                         name="Close",
                         line=dict(color='#f44242'))

data =[trace_close]
layout = dict(title=symbol, showledgend=False)

fig=dict(data=data,layout=layout)
#print(fig)

app = dash.Dash(__name__)

print(fig)
app.layout= html.Div([
    html.Div(html.H1(children="Trade Bot V1")),
    html.Label('Dash Chart'),

    html.Div(
        dcc.Input(
            id="stock-input",
            placeholder="Enter a Coin to be charted",
            type='text',
            value=''
        ),
    ),

    html.Div(
        dcc.Dropdown(
            options=[
                {'label': 'Candlestick', 'value':'Candlestick'},
                {'label': 'Line', 'value':'Line'},
            ]
        ),
    ),
    html.Div(
        dcc.Graph(id='Stock Chart', figure=fig)
    )



])
if __name__ == '__main__':
    app.run_server(debug=True)

'''#start = datetime.today() - relativedelta(years=5)
#end = datetime.today()

#df = get_historical_data("AAPL", start, end, output_format='pandas', token="pk_1a8d78cea473429fa72cbcefdcf2c486")

aapl = Stock("AAPL",token="pk_1a8d78cea473429fa72cbcefdcf2c486")
aapl.get_balance_sheet()
print(aapl.head(-5))'''
