'''
Name: main.py

Description: Loads in a folder with several data files. Can do a variety of tasks depending on the arg function

author: @Katelyn98
'''
import func.filter_data as fdf
import func.ensemble as esla
import func.analyze_filtered_tweets as azft
import os
import config_with_yaml as config
from pathlib import Path

#load in config file
cfg = config.load("config/config.yml")
data_dir = Path('../..') / cfg.getProperty("data_file_path")
data_files = data_dir.glob(cfg.getProperty("file_type"))

if __name__ == "__main__":
	#language detection experiments
	esla.ensembleMethod(data_files)
	
	#filtering is not required for analyzing, but is recommended.
	#filtering gets rid of tweets that do not have a place or URL and tweets that are not in English
	# print("start filter")
	# final_df = fdf.mainFilter(data_files, 3)
	# print("completed filter")

	# print("start analyzing")
	# azft.mainFunc(final_df)
	# print("completed analyzing")
