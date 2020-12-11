
import os
import sys
import pandas as pd

def pd_reader(filename=''):
    ext = os.path.splitext(filename)[1]
    if 'csv' in ext:
        return pd.read_csv(filename)
    elif 'json' in ext:
        return pd.read_json(filename, lines=True)
    raise Exception('File extension {} not recognized as option.'.format(ext)) 
