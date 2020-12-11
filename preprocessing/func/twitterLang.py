'''
name: twitterLang.py

Description: Detects the language of a tweet using the lang from Twitter

functions: 
    twitterLangDetect(data_files, tweetLangDict)
'''
import pandas as pd
from func.utils import pd_reader

def twitterLangDetect(data_files, tweetLangDict):
    '''
    Detects language by Lang column

    Parameters:
        data_files: string file path that can be changed in config.yml
        tweetLangDict: can be an empty dictionary or one that is being continued from a previous month
    '''

    for file in data_files:
        df = pd_reader(filename=file)
        for i in range(len(df)):
            strkey = df.loc[i]['lang']
            if strkey in tweetLangDict:
                tweetLangDict[strkey] += 1
            else:
                tweetLangDict[strkey] = 1

    return tweetLangDict
