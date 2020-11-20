'''
Name: generate_geo_fig.py

Description: Generates a scatter_geo plotly express figure mapping the tweets to a location and date. 

Functions:
    generateWorld(clean_res_df, scope, claim_category)

author: @Katelyn98
'''
import plotly.express as px
import pandas as pd
import config_with_yaml as config
import styles_file as sf

#load in config file
cfg = config.load("config/config.yml")

def generateWorld(clean_res_df, scope, claim_category):
    '''
    Returns a plotly express scatter geo figure based on the scope
        Parameters:
            clean_res_df: pandas DataFrame
            cfg: config object
            scope: string value to use to create map - scope is limited to plotly express scatter_geo options
        Returns:
            fig: plotly express scatter_geo figure
    '''
 
    #set the legend to be either the topics or the narratives depending on which tab is clicked on
    #change the title accordingly
    claim_df = clean_res_df
    color = "topics"
    title = "COVID-19 Topic-Mapping"
    if claim_category != '':
         claim_df = clean_res_df[clean_res_df['topics'] == claim_category]
         color = "narratives"
         title = "COVID-19 Claim-Mapping"

     #Create scatter_geo figure - set animation frame to be by date, create custom hover data (changing the order of this hover data wilk
     # also affect how the tweet metadata is shown)
    fig = px.scatter_geo(claim_df, lat="long", lon="lat", animation_frame=cfg.getProperty("plotly_figures.figures.scatterGeo.animation_frame"), 
        color=color, hover_name=cfg.getProperty("plotly_figures.figures.scatterGeo.hover_name"),
        hover_data={"long": cfg.getProperty("plotly_figures.figures.scatterGeo.hover_data.lat"),
        "lat": cfg.getProperty("plotly_figures.figures.scatterGeo.hover_data.long"),
        "topics": False,
        "narratives": True,
        "full_text": cfg.getProperty("plotly_figures.figures.scatterGeo.hover_data.full_text"),
        "username": cfg.getProperty("plotly_figures.figures.scatterGeo.hover_data.tweet_user"),
        "retweet_count": True,
        "favorite_count": True,
        "source_tweeter": cfg.getProperty("plotly_figures.figures.scatterGeo.hover_data.source_tweeter"),
        "quote_retweet_count": True,
        "quote_favorite_count": True,
        "source": cfg.getProperty("plotly_figures.figures.scatterGeo.hover_data.source"),
        "source_bias": cfg.getProperty("plotly_figures.figures.scatterGeo.hover_data.source_bias"), 
        "date": False})
    fig.update_layout(paper_bgcolor=sf.styles['text']['background-color'],font_color=sf.styles['title']['color'], geo_scope = scope)
    fig.update_layout(title = title)

    return fig