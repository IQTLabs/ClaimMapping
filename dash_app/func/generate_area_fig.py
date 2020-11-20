'''
Name: generate_area_fig.py

Description: Generates a filled area plotly express chart

Functions:
    generateAreaFigure(clean_res_df, color, title)

author: @Katelyn98
'''
import plotly.express as px
import pandas as pd
import config_with_yaml as config
import func.prep_plotly as pfp
import styles_file as sf

#load in config file
cfg = config.load("config/config.yml")

def generateAreaFigure(clean_res_df, color, title):
    '''
    Returns one plotly express filled area chart to show on dash app.

        Parameters: 
            clean_res_df: pandas DataFrame
            cfg: config object reference

        Returns:
            fig: A plotly express filled area chart with range slider
    '''

    #get filtered, narrowed df
    df = pfp.prepDataFrame(clean_res_df, True)

    #make filled area chart with range slider - create legend by category
    fig = px.area(df, x="date", y="count", color=color)
    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=cfg.getProperty("plotly_figures.figures.area.rangeslider")
            ),
            type="date"
        )
    )
    fig.update_layout(
        paper_bgcolor=sf.styles['text']['background-color'],
        font_color=sf.styles['title']['color']
    )
    #show the hover lines
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    #create title
    fig.update_layout(title = title)

    return fig