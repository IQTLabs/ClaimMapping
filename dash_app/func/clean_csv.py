'''
Name: clean_csv.py

Description: Modifies all of the columns necessary that are type string but actually a dictionary

Functions: 
    cleanCSV(df)

author: @Katelyn98
'''
import ast
import config_with_yaml as config

#load in config file
cfg = config.load("config/config.yml")
def cleanCSV(df):
    ''''
    Returns a modified pandas dataframe that changes all strings necessary to the dictionary type

    Parameters:
        df: pandas dataframe

    Returns:
        df: modified pandas dataframe
    '''
    for i in range(len(df)):
        try: 
            strplace = df.loc[i]['place']
            dictplace = ast.literal_eval(strplace)
            df.at[i, 'place'] = dictplace
        except:
            pass

        try:
            quote_str = df.loc[i]['quoted_status']
            quote = ast.literal_eval(quote_str)
            df.at[i, 'quoted_status'] = quote
        except:
            pass  

        try:
            strentity = df.loc[i]['entities']
            dictentity = ast.literal_eval(strentity)
            df.at[i, 'entities'] = dictentity
        except:
            pass

        try:
            struser = df.loc[i]['user']
            dictuser = ast.literal_eval(struser)
            df.at[i, 'user'] = dictuser
        except:
            pass
        
    return df