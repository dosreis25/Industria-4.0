# frontend.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Energy Management Dashboard"),
    dcc.Graph(id='energy-graph'),
    dcc.Interval(
        id='interval-component',
        interval=5*1000,  # Atualiza a cada 5 segundos
        n_intervals=0
    )
])

@app.callback(
    Output('energy-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    response = requests.get('http://127.0.0.1:5000/api/energy_data')
    data = response.json()
    df = pd.DataFrame(data)

    fig = {
        'data': [{
            'x': df['timestamp'],
            'y': df['energy_consumption'],
            'type': 'line',
            'name': 'Energy Consumption'
        }],
        'layout': {
            'title': 'Energy Consumption Over Time',
            'xaxis': {'title': 'Time'},
            'yaxis': {'title': 'Energy Consumption (kWh)'},
        }
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
