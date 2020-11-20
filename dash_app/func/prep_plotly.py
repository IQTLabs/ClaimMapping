'''
Name: prep_plotly.py

Description: Prepares the dataframe being passed in to be used for the scatter plot or filled area chart. Returns modified
dataframe.

Functions:
    prepDataFrame(clean_res_df)

author: @Katelyn98
'''
import pandas as pd
import config_with_yaml as config

#load in config file
cfg = config.load("config/config.yml")

def prepDataFrame(clean_res_df, zeros):
    '''
    Returns a modififed dataframe set up to create a filled area chart

    Parameters:
        clean_res_df: pandas dataframe

    Returns:
        agg_sum_category: modififed pandas dataframe of clean_res_df with the columns: 'date', 'topics', 'narratives', 'source_bias', and 'size'
    '''
    #Getting rid of any columns that don't have any tweets recorded (columns with size of 0)
    df_area_chart = clean_res_df
    if zeros:
        dff_clean = df_area_chart[df_area_chart['size'] != 0]
        dff_clean = dff_clean.reset_index()
    else: 
        dff_clean = df_area_chart
    # df_area_chart = dff_clean.drop(columns=['index'])

    #filter DataFrame by date, then topic/narrative, then source_bias and aggregate size to get a final count
    agg_sum_category = pd.DataFrame(dff_clean.groupby(['date','topics', 'narratives', 'source_bias']).agg('size'))
    agg_sum_category.columns = ['count']

    agg_sum_category = agg_sum_category.reset_index()

    return agg_sum_category