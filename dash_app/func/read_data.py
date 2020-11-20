'''
Name: read_data.py

Description: Read in the data from given file path based on data type. Return data frame after adding 6 new twitter metadata columns

Functions:
	readData(file_path, data_type)

author: @Katelyn98
'''
import pandas as pd
from pathlib import Path
import config_with_yaml as config

#load in config file
cfg = config.load("config/config.yml")

def readData(file_path, data_type): 
	'''
		Reads in data based on file path and data type. Returns data as pandas dataframe.

		Parameters:
			file_path: string path to data in the format of 'folder/folder/file.csv'
			data_type: string of data type - example: 'read_csv'

		Returns:
			res_df: pandas dataframe consisting of data from passed in file
	'''
	#file path to access data - change '.' if data is outside of dash_app folder.
	fpath = Path('.') / file_path
	if data_type == 'read_csv':
	    res_df = pd.read_csv(str(fpath))
	elif 'read_json':
	    res_df = pd.read_json(file_path, lines=True)
	# elif data_type = 'read_sql':
	#     read from postgres sql database 

	#prep dataframe for plotting - add several columns for easy access
	res_df['username'] = ''
	res_df['lat'] = -90.0
	res_df['long'] = -180.0
	res_df['size'] = 1
	res_df['source'] = ''
	res_df['source_tweeter'] = ''
	res_df['quote_retweet_count'] = 0
	res_df['quote_favorite_count'] = 0

	return res_df