'''
name: analyze_filtered_tweets.py

description: Functions to create a hand-curated data set of twitter data from a dataframe. Associated with jupyter notebook 'FilteredTweets.ipynb'

functions: 
	hasURL(tweet)
	fix_csv(df)
	topURLs(df)
	read_top_URL_tweets(url_to_tweet_map, fixed_df)
	hand_curated_dataset(urls_list, df, topic, narrative)
	mainFunc(df)
'''
import ast
import pandas as pd
import config_with_yaml as config

cfg = config.load("config/config.yml")

def hasURL(tweet):
	'''
	Checks to see if a tweet has a URL

	Parameter:
		tweet: a single tweet (a row) from the data

	Returns:
		boolean: True if the tweet has a URL; False if the tweet does not have a URL
	'''
	URL_location = tweet[cfg.getProperty("tweet.url_path.entities")][cfg.getProperty("tweet.url_path.url")]
	if len(URL_location) == 0:
		return False
	else: 
		return True

def fix_csv(df):
	'''
	Fixes cells that are a dictionary but of type string and converts them back to a dictionary

	Parameters: 
		df: pandas dataframe that was created from a CSV or excel file

	Returns:
		df: a modified pandas dataframe where the dictionaries of type string are now of type dictionary
	'''
	for i in range(len(df)):
		try: 
			strplace = df.loc[i]['place']
			dictplace = ast.literal_eval(strplace)
			df.at[i, 'place'] = dictplace

			quote_str = df.loc[i]['quoted_status']
			quote = ast.literal_eval(quote_str)
			df.at[i, 'quoted_status'] = quote

			strentity = df.loc[i]['entities']
			dictentity = ast.literal_eval(strentity)
			df.at[i, 'entities'] = dictentity

			struser = df.loc[i]['user']
			dictuser = ast.literal_eval(struser)
			df.at[i, 'user'] = dictuser

		except:
		    pass

	return df

def topURLs(df):
	'''
	Create a dictionary of unique URLs and how many times they were referenced and a dictionary mapping tweets to a URL

	Parameters:
		df: a pandas dataframe consisting of all the twitter data

	Returns:
		tweet_URLs: a dictionary that consists of a URL and the number of times that URL was referenced throughout the data
		url_to_tweet_map: a dictionary that consists of a URL and all the indices of the tweet in the dataframe

	'''

    #create lang dictionary to get a count of the number of times a url is tweeted
	tweet_URLs = {}
	url_to_tweet_map = {}

	for i in range(len(df)):
		if hasURL(df.loc[i]):
			#get the URL that was referenced in the tweet (in some cases URL is a twitter link to another tweet (this is a retweet))
			expURL = df.loc[i][cfg.getProperty("tweet.url_path.entities")][cfg.getProperty("tweet.url_path.url")][cfg.getProperty("tweet.url_path.exp_url_id")][cfg.getProperty("tweet.url_path.exp_url")]
			if expURL.startswith('https://twitter.com/'):
				continue
			else: 
				#collecting all unique URLs
				if expURL in tweet_URLs:
					tweet_URLs[expURL] += 1
				else:
					tweet_URLs[expURL] = 1

				#adding every tweet index that references that URL
				if expURL in url_to_tweet_map:
					url_to_tweet_map[expURL].append(i)
				else:
					url_to_tweet_map[expURL] = []
					url_to_tweet_map[expURL].append(i)
		else:
			continue;
            
	return tweet_URLs, url_to_tweet_map

def read_top_URL_tweets(url_to_tweet_map, df):
	'''
	Prints out all of the URLs with their tweets' full text. The threshold can be changed. Currently any URL that was referenced by 
	more than 0 tweets will be printed out. For a larger dataset, it is good to change this value to 10 or more. 

	Parameters:
		url_to_tweet_map: dictinoary that consists of the URL and the indices of the tweets that reference that URL
		df: original dataframe with all the twitter data

	Returns: 
		Print statements of URLs and full text of tweets
	'''
	#create a df for the URLs with tweet ids
	columns = ['url', 'tweets']
	urltweets_df = pd.DataFrame(url_to_tweet_map.items(), columns=columns)
	for i in range(len(urltweets_df)):
		#print out any URL and the tweets associated with it if it has more than 0 tweets referencing it.
		if len(urltweets_df.loc[i]['tweets']) > cfg.getProperty("tweet.url_path.threshold"):
			print("URL: " + urltweets_df.loc[i]['url'])
			for tweet in urltweets_df.loc[i]['tweets']:
				print("Tweet number: {}".format(tweet))
				print(df.loc[tweet]['full_text'])
				print("\n")

	return urltweets_df

def hand_curated_dataset(urltweets_df, df, urlList, topic, narrative):
	'''
	Method used to create a hand_curated dataframe

	Parameters: 
		urltweets_df: dictionary of URLs mapped to tweet indices
		df: original dataframe with all the twitter data
		urlList: list of URLs that you want to have labeled
		topic: string name of topic you want to label the URL (this could be Cure, Origin, Prevention, etc.)
		narrative: string name of specific narrative within the topic you want to label the URL

	Returns:
		df: a modified dataframe of the original dataframe with labels for two columns (topics and narratives)
			*note* these two columns are added if they are not previously there.

	'''

	for i in range(len(df)):
		if urltweets_df.loc[i]['url'] in urlList:
			df.at[i, 'topics'] = topic
			df.at[i, 'narratives'] = narrative

	return df

def mainFunc(df): 
	'''
	Main function that performs all tasks required for analyzing the dataframe.

	Parameter:
		df: dataframe passed in after filtering happens

	Returns: 
		Print statements from methods called
	'''
	# fixed_df = fix_csv(df) #only use if passing in a dataframe that was created from a CSV file
	tweet_URLs, url_to_tweet_map = topURLs(df)
	urltweets_df = read_top_URL_tweets(url_to_tweet_map, df)

