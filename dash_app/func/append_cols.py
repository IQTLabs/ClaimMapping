'''
Name: append_cols.py

Description: Fills in columns of the dataframe to make it easier to access specific information to plot the figures

Functions:
	append(clean_res_df)

author: @Katelyn98
'''
import config_with_yaml as config
#load in config file
cfg = config.load("config/config.yml")

def append(clean_res_df):
	'''
	Loops through every row of the passed in dataframe; grabs certain information and adds it to separate columns. Returns 
	the new dataframe. 

		Parameters:
			clean_res_df: pandas dataframe

		Returns:
			clean_Res_df: pandas dataframe
	'''
	for i in range(len(clean_res_df)):

		#Set the latitude and longitude values - else set the size to 0 because it is a filler row
		try:
			lat = clean_res_df.loc[i]['place']['bounding_box']['coordinates'][0][0][0]
			longg = clean_res_df.loc[i]['place']['bounding_box']['coordinates'][0][0][1]
			clean_res_df.at[i, 'lat'] = lat
			clean_res_df.at[i, 'long'] = longg
		except:
			clean_res_df.at[i, 'size'] = 0
		
		#set the quoted retweet and favorite count for easy access
		try:
			quote_rt_ct = clean_res_df.loc[i]['quoted_status']['retweet_count']
			quote_fv_ct = clean_res_df.loc[i]['quoted_status']['favorite_count']
			clean_res_df.at[i, 'quote_retweet_count'] = quote_rt_ct
			clean_res_df.at[i, 'quote_favorite_count'] = quote_fv_ct
		except:
			pass

		#Change a column name
		if clean_res_df.loc[i]['narratives'] == 'Prevention: Social Distancing' or clean_res_df.loc[i]['narratives'] == 'Prevention: Distancing/Masks':
			clean_res_df.at[i, 'narratives'] = 'Distancing/Masks'
		
		#Set tweet_user and source_tweeter for easy access  
		try:
			screen_name = clean_res_df.loc[i]['user']['screen_name']
			clean_res_df.at[i, 'username'] = "@" + screen_name
			if clean_res_df.loc[i]['URL_link'].startswith('https://twitter.com/'):
				username = ((clean_res_df.loc[i]['URL_link'].split('https://twitter.com/'))[1].split('/'))[0]
				clean_res_df.at[i, 'source_tweeter'] = "@" + str(username)
			else:
				clean_res_df.at[i, 'source_tweeter'] = "not_available"
		except:
			pass

		#set source link for easy access
		clean_res_df.at[i, 'source'] = clean_res_df.loc[i]['URL_link']

	return clean_res_df