'''
Name: styles_file.py

Description: Home to all the styles needed for any compoonent in the Dash App.

author: @Katelyn98
'''
import config_with_yaml as config
#load in config file
cfg = config.load("config/config.yml")

#Style used for the Twitter Metadata
styles = {
    'pre': {
        'font-family': cfg.getProperty("dash_app.styles.font-family"),
        'overflowX': cfg.getProperty("dash_app.styles.overflowX"),
        'font-size': cfg.getProperty("dash_app.styles.font-size")
    },
    'text': {
        'font-family': cfg.getProperty("dash_app.styles.font-family"),
        'background-color': 'rgb(255,255,255)',
        'color': 'rgb(0,0,31)',
    },
    'title': {'textAlign': 'center',
        'font-family': cfg.getProperty("dash_app.styles.font-family"),
        'background-color': 'rgb(255,255,255)',
        'color': 'rgb(0,0,31)',
    }


}

colors = {
    'background': 'gb(255,255,255)',
    'text': 'rrgb(0,0,31)'
}

#Styles specifically for the tabs used in the Dash App
tabs_styles = {
    'height': cfg.getProperty("dash_app.styles.tab.height"),
    'font-family': cfg.getProperty("dash_app.styles.tab.font-family")
}
tab_style = {
    'borderBottom': cfg.getProperty("dash_app.styles.tab.borderBottom"),
    'padding': cfg.getProperty("dash_app.styles.tab.padding"),
    'fontWeight': cfg.getProperty("dash_app.styles.tab.fontWeight")
}

tab_selected_style = {
    'borderTop': cfg.getProperty("dash_app.styles.tab.borderTop"),
    'borderBottom': cfg.getProperty("dash_app.styles.tab.borderBottom"),
    'backgroundColor': 'rgb(0,0,31)',
    'color': 'rgb(255,255,255)',
    'font-family': 'tahoma',
    'padding': cfg.getProperty("dash_app.styles.tab.padding")
}