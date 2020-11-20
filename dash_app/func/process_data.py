'''
Name: process_data.py

Description: Parent method to house several methods for cleaning the dataframe

Functions:
	processDF(file_path, data_type)

author: @Katelyn98
'''
import pandas as pd
import ast
import func.read_data as rd
import func.clean_csv as ccs
import func.append_cols as acl

def processDF(file_path, data_type):
    '''
    Calls several methods to clean and modify the original testDates.csv

    Parameters:
    	file_path: file path from config.yml
    	data_type: file type (either csv or json or potentially for SQL database)
    '''
    
    #turn input file into a pandas DataFrame and fix column values
    res_df = rd.readData(file_path, data_type)
    clean_res_df = ccs.cleanCSV(res_df)
    return acl.append(clean_res_df)