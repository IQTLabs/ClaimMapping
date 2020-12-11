'''
Name: ensemblePrint.py

Description: prints out all the counts for english language counted using each detection method

Functions:
    printCount(df)
'''
import config_with_yaml as config

cfg = config.load("config/config.yml")

def printCount(df):
    #ensemble method
    enCt = 0
    otrCt = 0

    #twitter lang 
    twCt = 0
    twotrCt = 0

    #lang detect lang
    ldCt = 0
    ldotrCt = 0

    #filter for this lang
    lang = cfg.getProperty("language")
    
    for i in range(len(df)):
        #ensemble method
        if df.iloc[i]['twitterLang'] == lang and df.iloc[i]['langDetect'] == lang:
            enCt += 1
        else:
            otrCt += 1

        #only twitter count
        if df.iloc[i]['twitterLang'] == lang:
            twCt += 1
        else:
            twotrCt += 1

        #only langDetect count
        if df.iloc[i]['langDetect'] == lang:
            ldCt += 1
        else:
            ldotrCt += 1

    print("en: {}".format(enCt))
    print("other: {}".format(otrCt))

    print("twitter_en: {}".format(twCt))
    print("twitter_otr: {}".format(twotrCt))

    print("langDetect_en: {}".format(ldCt))
    print("langDetect_otr: {}".format(ldotrCt))
