'''
Name: filter_Data.py

Description: Filters data to be in English (language can be changed in config.yml), have a URL, and a location.

Functions:
    detectLang(tweet)
    hasPlace(tweet)
    hasURL(tweet)
    tweetOnTwitter(df)
    filterDF(df)
    mainFilter(data_files, filtered_filename)
'''
import os
from langdetect import detect, lang_detect_exception, DetectorFactory
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import wordnet as wn
import pandas as pd
from func.utils import pd_reader
import config_with_yaml as config

cfg = config.load("config/config.yml")


#Between twitter identified lang and lang determined by langDetect, detect language. 
def detectLang(tweet):
    '''
    Detect language using an ensemble approach

    Parameter:
        tweet: one row (tweet) from dataframe

    Returns:
        detected_lang: string two letter code of language detected
    '''
    DetectorFactory.seed = 0
    detected_lang = None
    try: 
        detected_lang = detect(tweet['full_text'])             
    except:
        detected_lang = 'und'

    #filter for this lang for ensemble method
    lang = cfg.getProperty("language")

    if tweet['lang'] != lang and detected_lang == lang:
        #if twitter say the tweet isn't in English and langDetect says it is, don't include it
        detected_lang = tweet['lang']
    elif tweet['lang'] == lang and detected_lang == lang:
        detected_lang = lang

    return detected_lang

def hasPlace(tweet):
    '''
    Checks if the tweets is associated with a location

    Parameters:
        tweet: one row (tweet) from dataframe

    Returns:
        boolean: location - true, no location - false
    '''
    if tweet['place'] == None:
        return False
    else: 
        return True

def hasURL(tweet):
    '''
    Checks if the tweet has a URL

    Parameters:
        tweet: one row (tweet) from dataframe

    Returns:
        boolean: has URL - true; no URL; false
    '''
    if len(tweet['entities']['urls']) == 0:
        return False
    else: 
        return True

def tweetOnTwitter(df):
    '''
    Creates an easy link to view the tweet on twitter by concatenating twitter.com with username and twitter id

    Parameters:
        df: pandas dataframe of twitter data

    Returns:
        df: modified pandas dataframe with a new column called 'tweet_on_twitter'
    '''
    for i in range(len(df)):  
        begin = 'https://twitter.com/'
        username = df.loc[i]['user']['screen_name']
        breakin = '/'
        status = 'status' 
        tweetid = str(df.loc[i]['id'])
        urlstr = begin+username+breakin+status+breakin+tweetid
        df.at[i, 'tweet_on_twitter'] = urlstr
    
    return df

def modifyColumns(df):
    '''
    Modifies the dataframe to create a column with the source URL that was referenced in the tweet

    Parameters:
        df: Pandas dataframe of twitter data

    Returns:
        df: modified pandas dataframe with a new column called 'URL_link'
    '''
    #Create a quick an easy URL Link column to view the link that is being referenced.
    df.insert(3, 'url_link', '')
    for i in range(len(df)):
        if len(df.loc[i]['entities']['urls']) > 0:
            urlstr = df.loc[i]['entities']['urls'][0]['expanded_url']
            df.at[i, 'URL_link'] = urlstr
    #create a quick and easy column to view the tweet on twitter
    df.insert(4, 'tweet_on_twitter','')
    return tweetOnTwitter(df)


def filterDF(df):
    '''
    Filters the dataframe to make sure there is a place, a URL, and tweets are in English using ensemble approach

    Parameters:
        df: Pandas dataframe of twitter data

    Returns:
        df: modified pandas dataframe of twitter data that is filtered
    '''
    dropList = []
    for i in range(len(df)):
        #fix the language
        df.at[i, 'lang'] = detectLang(df.loc[i])

        #drop records that don't have a url or a place
        if not hasPlace(df.loc[i]):
            dropList.append(i)
        if not hasURL(df.loc[i]):
            dropList.append(i)

    #at the end remove all the records from the droplist
    df = df.drop(dropList)
    df = df[df['lang'] == 'en']
    df = df.reset_index()
    return df

#code in two methods below from Medium.com Blog Post on TF-IDF: https://medium.com/@bedigunjit/simple-guide-to-text-classification-nlp-using-svm-and-naive-bayes-with-python-421db3a72d34
# def lemmatization(df):
#     #Twitter specific stopwords
#     tweetWords = ['rt', 'co', 'https']
#     #Change all the text to lower case
#     df['full_text'] = [entry.lower() for entry in df['full_text']]
#     #Tokenize each entry
#     tokens = [word_tokenize(entry) for entry in df['full_text']]
#     #Remove Stop words, Non-Numeric and perfom Word Stemming/Lemmenting.
#     #WordNetLemmatizer requires Pos tags to understand if the word is noun or verb or adjective etc. By default it is set to Noun
#     tag_map = defaultdict(lambda : wn.NOUN)
#     tag_map['J'] = wn.ADJ
#     tag_map['V'] = wn.VERB
#     tag_map['R'] = wn.ADV
#     for index,entry in enumerate(tokens):
#         #Declaring Empty List to store the words that follow the rules for this step
#         Final_words = []
#         #Initializing WordNetLemmatizer()
#         word_Lemmatized = WordNetLemmatizer()
#         #pos_tag function below will provide the 'tag' i.e if the word is Noun(N) or Verb(V) or something else.
#         for word, tag in pos_tag(entry):
#             #Below condition is to check for Stop words and consider only alphabets
#             if word not in stopwords.words('english') and word not in tweetWords and word.isalpha():
#                 word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
#                 Final_words.append(word_Final)
#         #The final processed set of words for each iteration will be stored in 'text_final'
#         df.loc[index,'text_final'] = str(Final_words)
        
#     return df

# def topics(df):
#     keywords = ['cure', 'oil', 'remedy', 'medicine', 'tradition','traditional', 'natural', 'tea', 'whiskey', 'honey', 'mask', 'n95',
#                 'garlic', 'oregano','sesame','prevent','help', 'pee', 'poop', 'dung', 'cow', 'rare', 'drink', 'drugs',
#                 'urine', 'HIV', 'wear', 'try', 'eat', 'use', 'health']
#     df['topics'] = None
#     for i in range(len(df)):
#         topicWords = []
#         text_final = df.loc[i]['text_final']
#         for word in keywords:
#             if word in text_final:
#                 topicWords.append(word)
#         df.at[i, 'topics'] = topicWords
    
#     return df

def mainFilter(data_files=[], filtered_filename=''):
    '''
    Main filtering method that will call all helper methods above.

    Parameters:
        data_files: list of string paths to data files - can be changed in config.yml
        filtered_filename: string filename containing filtered data

    Returns:
        final_df: a filtered pandas dataframe
    '''
    count = 0.0
    result_dfs = []
    numb_files = len(data_files)

    for file in data_files:
        print("in file", file)
        fext = os.path.splitext(file)[1]
        df = pd_reader(filename=file)
        df = filterDF(df)
        df = modifyColumns(df)
        result_dfs.append(df)
        count += 1
        print("completed: {}".format(count/numb_files * 100))
   
    print(result_dfs)
    final_df = pd.concat(result_dfs)
    final_df = final_df.reset_index()
    final_df.to_csv(filtered_filename)
    return final_df
