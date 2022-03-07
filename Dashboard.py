import dash
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Center([ html.Div([
    html.H1('IoT Dashboard'),
    html.Div([
        html.P('Very early version'),
    ])]),
    html.Br(),
    daq.Gauge(
        id='my-gauge-1',
        label="Humidity",
        value=4
    ),
    dcc.Slider(
        id='my-gauge-slider-1',
        min=0,
        max=4,
        step=1,
        value=5
    ),
    daq.Gauge(
    showCurrentValue=True,
    units="MPH",
    value=5,
    label='Speed',
    max=10,
    min=0
)
])

@app.callback(Output('my-gauge-1', 'value'), Input('my-gauge-slider-1', 'value'))
def update_output(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)