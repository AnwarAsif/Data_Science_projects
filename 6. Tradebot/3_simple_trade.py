import dash
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div(
  html.H1(children='Hello World')
)

if __name__ == '--__main__':
    app.run_server(debug=True)
