'''
Name: slider.py

Description: This file serves as an example of a dash app with one figure that has a slider instead of 
using the animation_frame parameter for a plotly express figure. This file runs and exists without any of the
other files in this folder. To run it, type 'python3 slider.py' in the terminal. 
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import func.process_data as prod
import config_with_yaml as config
import styles_file as sf
import plotly.express as px

#load in config file
cfg = config.load("config/config.yml")

#process dataframe
file_path = 'data/testDates.csv'
data_type = cfg.getProperty("data.data_type")
df = prod.processDF(file_path, data_type)

#setting up styles for dash up
external_stylesheets = [cfg.getProperty("dash_app.external_stylesheets")]

#initalizing dash app to variable named 'app'
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions = cfg.getProperty("dash_app.callback_exceptions"))

#line needed to deploy to heroku
server = app.server

#main layout of the dash app
app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='date-slider',
        min=min(df['number']),
        max=max(df['number']),
        value=min(df['number']),
        marks={str(number): str(number) for number in df['number'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('date-slider', 'value')])
def update_figure(selected_date):
    filtered_df = df[df.number == selected_date]

    fig = px.scatter_geo(filtered_df, lat="long", lon="lat", color="category")
    fig.update_layout(title = cfg.getProperty("plotly_figures.figures.scatterGeo.title"), geo_scope = 'usa')
    fig["layout"].pop("updatemenus")

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)