import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.P(f"this is special"),

    html.Div('Trade Bot:')

])

if __name__ == '__main__':
    app.run_server(debug=True)
