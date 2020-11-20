'''
Name: generate_scatter_fig.py

Description: Generates a plotly express scatter plot for politcial affiliation

Functions:
    generatePoliticalScatter(clean_res_df, value)

author: @Katelyn98
'''
import plotly.express as px
import pandas as pd
import config_with_yaml as config
import func.prep_plotly as pfp
import styles_file as sf

#load in config file
cfg = config.load("config/config.yml")

def generatePoliticalScatter(clean_res_df, value):
    '''
    Returns one plotly express scatter ploty figure to show on dash app

        Parameters: 
            clean_res_df: pandas DataFrame
            cfg: config object reference
            value: string value to filter DataFrame

        Return:
            fig: a plotly express scatter plot with range slider
    '''
    #get filtered, narrowed df
    df = pfp.prepDataFrame(clean_res_df, True)

    dff = df
    if value != '':
        #filter scatter plot by value chosen from dropdown
        dff = df[df['narratives'] == value]


    #create scatter plot, set legend based on source_bias and choose specific colors based on political party themes
    fig = px.scatter(dff, x="date", y="count", color="source_bias",hover_name="narratives",
                    hover_data={
                        "source_bias": True
                    }, 
                    color_discrete_map={cfg.getProperty("plotly_figures.figures.scatter.colors.label"): cfg.getProperty("plotly_figures.figures.scatter.colors.color"), 
                    cfg.getProperty("plotly_figures.figures.scatter.colors.label2"): 'rgb(153,153,153)', 
                    cfg.getProperty("plotly_figures.figures.scatter.colors.label3"): 'rgb(55,126,184)', 
                    cfg.getProperty("plotly_figures.figures.scatter.colors.label4"): 'rgb(228,26,28)'})
    #create a range slider
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="date"
        ),
        paper_bgcolor=sf.styles['text']['background-color'],
        font_color=sf.styles['title']['color']
    )
    #create title
    fig.update_layout(title = cfg.getProperty("plotly_figures.figures.scatter.title"))

    return fig