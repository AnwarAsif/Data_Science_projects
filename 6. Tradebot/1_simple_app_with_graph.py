import dash
import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__) # why __name__ is required


def get_figure_info():

    N = 1000
    X = np.linspace(0, 10, 100)
    y = 3*X + 5 + np.linspace(0, 10, 100)


    data = [go.Scatter(x=X,
                    y=y,
                    name = 'data',
                    mode='markers')]

    layout = {'title':"Gradien Descent"}

    return data, layout

data , layout = get_figure_info()


app.layout = html.Div(children=[
    html.H1('Gradien Descent'),

    html.Div('Gradien Desent is an optimization Algorithm to find optimized loss by reducing cost by doing iterations. To find the lowest cost algorithm use calculas to calculate the direction and pace toward the target cost'),

    dcc.Graph(figure={
        'data':data,
        'layout': layout
    }),



])



if __name__ == '__main__':


    app.run_server(debug=True)
