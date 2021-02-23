import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

data = [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}]

data = [{'x':[1,2,3],
        'y':[4,5,4],
        'type': 'bar',
        'name':'Apple'},
        ]

layout = {'title':"Image Title"}

app.layout = html.Div(children=[
    dcc.Graph(
    figure = {
        'data': data,
        'layout': layout
    }
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)
