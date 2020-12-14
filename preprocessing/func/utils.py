
import os
import sys
import pandas as pd

def pd_reader(filename=''):
    ext = os.path.splitext(filename)[1]
    if 'csv' in ext:
        df = pd.read_csv(filename)
        return df
    elif 'json' in ext:
        df = pd.read_json(filename, lines=True)
        return df
    raise Exception('File extension {} not recognized as option.'.format(ext)) 
