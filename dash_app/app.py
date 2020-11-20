''' 
Name: app.py
Description: Creates Claim Mapping dash app. Generates three figures from hand-curated
dataset of tweets from March - April 2020. Tweet ids hydrated from https://github.com/echen102/COVID-19-TweetIDs.
Functions:
    update_figure(value, clickData)
    render_content(tab)
    render_scatter(value)
@author: katelyn98
'''
import dash
import func.process_data as prod
import config_with_yaml as config
import styles_file as sf
import layouts as appview
import callbacks as cb

#load in config file
cfg = config.load("config/config.yml")

#process dataframe
file_path = cfg.getProperty("data.data_file_path")
data_type = cfg.getProperty("data.data_type")
clean_res_df = prod.processDF(file_path, data_type)

#setting up styles for dash up
external_stylesheets = [cfg.getProperty("dash_app.external_stylesheets")]

#initalizing dash app to variable named 'app'
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions = cfg.getProperty("dash_app.callback_exceptions"))

#uncomment line below to deploy to heroku
server = app.server

#main layout of the dash app
app.layout = appview.layout

#handle all callbacks for the dash app
cb.performCallbacks(app, clean_res_df)


if __name__ == '__main__':
    app.run_server(debug=True)