'''
Name: main.py

Description: Loads in a folder with several data files. Can do a variety of tasks depending on the arg function

author: @Katelyn98, @zhampel
'''
import func.filter_data as fdf
import func.ensemble as esla
import func.analyze_filtered_tweets as azft
import os
import glob
import argparse
import config_with_yaml as config
from pathlib import Path

# CMD line option to feed in YAML configuration file
global args
parser = argparse.ArgumentParser(description="Preprocessing script")
parser.add_argument("-c", "--config_file", dest="config_file",
                    default='config/config.yml', help="Path to YAML configuration file")
args = parser.parse_args()

# Path to configuration file
cfg_file = args.config_file

#load in config file
cfg = config.load(cfg_file)

# Grab path to requested files of requested file extension
data_dir = cfg.getPropertyWithDefault("data_file_path", "data")
file_ext = cfg.getProperty("file_type")

# Grab list of files 
data_files = glob.glob(os.path.join(data_dir, "*." + file_ext))
num_files = len(list(data_files))

# Grab output filtered file name
filtered_fname = cfg.getPropertyWithDefault("filtered_fname", "filtered_example.csv")

if __name__ == "__main__":
    #language detection experiments
    esla.ensembleMethod(data_files)
    
    #filtering is not required for analyzing, but is recommended.
    #filtering gets rid of tweets that do not have a place or URL and tweets that are not in English
    print("start filter")
    final_df = fdf.mainFilter(data_files, filtered_fname)
    print("completed filter")

    print("start analyzing")
    azft.mainFunc(final_df)
    print("completed analyzing")
