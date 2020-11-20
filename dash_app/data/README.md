# Data used for Dash App
You can download the _example_data.csv_ file and use this to merge with your own data. This file contains two rows of data - the first row is a filled in tweet example and the second row is a filler row that is used for plotly figures animations. The dash app is currently running on _testDates.csv_ which includes 563 tweets from March, April and May 2020 and 450 filler rows. You can find a data dictionary and data format guidelines below. You can process your data through the [filter_data python analysis script](https://github.com/IQTLabs/Infodemic/blob/4b8f67c5b33566316b2d1b70002087e0b471cb01/Claim_Mapping/python_analysis/func/filter_data.py) which takes in a folder of json files full of Twitter API data. 

## Data Dictionary
| column name | type | definition |
| --- | --- | --- |
| created_at | <class 'str'> | Twitter API created_at
| date	| <class 'str'> | split created_at string to only have _yyyy-mm-dd_
| id	| <class 'numpy.float64'> | Twitter API tweet id
| tweet_on_twitter | <class 'str'> | [tweetOnTwitter function](https://github.com/IQTLabs/Infodemic/blob/4b8f67c5b33566316b2d1b70002087e0b471cb01/Claim_Mapping/python_analysis/func/filter_data.py#L34)
| full_text | <class 'str'> | Twitter API tweet full_text
| entities	| <class 'str'> or <class 'dict'> | Twitter API tweet entities
| source	| <class 'str'> | Twitter API source
| in_reply_to_status_id	| <class 'numpy.float64'> | Twitter API in_reply_to_status_id	
| in_reply_to_status_id_str |	<class 'str'> | Twitter API in_reply_to_status_id_str
| in_reply_to_user_id	| <class 'numpy.float64'> | Twitter API in_reply_to_user_id
| in_reply_to_user_id_str |	<class 'str'> | Twitter API in_reply_to_user_id_str
| in_reply_to_screen_name |	<class 'str'> | Twitter API in_reply_to_screen_name
| quoted_status	| <class 'str'> of a dictionary or <class 'dict'> | Twitter API quoted_status
| user | <class 'str'> of a dictionary or <class 'dict'> | Twitter API user
| place | <class 'str'> of a dictionary or <class 'dict'> | Twitter API place
| contributors | <class 'str'> | Twitter API contributors
| retweeted_status | <class 'str'> | Twitter API retweeted_status
| is_quote_status | <class 'str'> |Twitter API is_quote_status
| quoted_status_id	| <class 'str'> |Twitter API quoted_status_id
| quoted_status_id_str | <class 'str'> | Twitter API quoted_status_id_str
| quoted_status_permalink	| <class 'str'> | Twitter API quoted_status_permalink
| retweet_count |	<class 'str'> | Twitter API retweet_count
| favorite_count	| <class 'str'> |Twitter API favorite_count
| lang	| <class 'str'> | Twitter API lang or [langdetect language function](https://github.com/IQTLabs/Infodemic/blob/4b8f67c5b33566316b2d1b70002087e0b471cb01/Claim_Mapping/python_analysis/func/filter_data.py#L12)
| URL_link	| <class 'str'> | URL link to URL shared in tweet - [modifyColumns functions](https://github.com/IQTLabs/Infodemic/blob/4b8f67c5b33566316b2d1b70002087e0b471cb01/Claim_Mapping/python_analysis/func/filter_data.py#L46)
| topics |	<class 'str'> | hand-labeled topic that URL fits within (i.e. Cure, Prevention, Origin, etc.)
| narratives |	<class 'str'> | hand-labeled narrative that URL fits within under specific topic
| source_bias | <class 'str'> | URL_link political affiliation from [NELA-GT-2019 Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/O7FWPO)

## Data Format
Follow the format below to be able to use your own twitter data with this dash app. The order does not need to be the same order as below. 
Note that a majority of the columns came from the Twitter API and some were removed just to make the dataset smaller, but it would not matter if they were not removed.

created_at | date	| id	| tweet_on_twitter | full_text | entities	 | source	| in_reply_to_status_id	| in_reply_to_status_id_str |	in_reply_to_user_id	| in_reply_to_user_id_str |	in_reply_to_screen_name |	quoted_status	| user | place | contributors |	retweeted_status | is_quote_status | quoted_status_id	| quoted_status_id_str | quoted_status_permalink	| retweet_count |	favorite_count	| lang	| URL_link	| topics |	narratives |	source_bias
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2020-03-01 05:18:22+00:00	| 2020-03-01 | 1.23E+18	| https://twitter.com/CoryBMorgan/status/1233984905702281216 | "i knew that a vaccine was pending. i should be safe now. little uncomfortable thohttps://t.co/gky3wthb2m"	| {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/GkY3WtHB2M', 'expanded_url': 'https://www.alaraby.co.uk/english/news/2020/2/25/applying-essential-oil-to-anus-cures-coronavirus-iranian-cleric', 'display_url': 'alaraby.co.uk/english/news/2‚Äö√Ñ¬∂', 'indices': [87, 110]}]} | <a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>	| not available |	not available |	not available |	not available |	not available |	not available |	{'id': 253147396, 'id_str': '253147396', 'name': 'Cory Morgan', 'screen_name': 'CoryBMorgan', 'location': 'Calgary', 'description': 'So woke it hurts. On permanently ceded territory. Shamelessly embracing my apparent privilege.  Prone to bouts of tastelessness.', 'url': 'http://t.co/NaQ1iEcny8', 'entities': {'url': {'urls': [{'url': 'http://t.co/NaQ1iEcny8', 'expanded_url': 'http://www.corymorgan.com', 'display_url': 'corymorgan.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 13578, 'friends_count': 682, 'listed_count': 141, 'created_at': 'Wed Feb 16 17:10:17 +0000 2011', 'favourites_count': 7509, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': True, 'statuses_count': 51217, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1277299990742753281/wTqP2Dn3_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1277299990742753281/wTqP2Dn3_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/253147396/1497992308', 'profile_image_extensions_alt_text': None, 'profile_banner_extensions_alt_text': None, 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'} | {'id': '2de55725306af67b', 'url': 'https://api.twitter.com/1.1/geo/id/2de55725306af67b.json', 'place_type': 'city', 'name': 'Foothills No. 31', 'full_name': 'Foothills No. 31, Alberta', 'country_code': 'CA', 'country': 'Canada', 'contained_within': [], 'bounding_box': {'type': 'Polygon', 'coordinates': [[[-114.636486, 50.309675], [-113.490136, 50.309675], [-113.490136, 50.9222386], [-114.636486, 50.9222386]]]}, 'attributes': {}}	|	FALSE	| not available |	not available	| not available	|	not available	| not available	| 17 | 56 |	en | https://www.alaraby.co.uk/english/news/2020/2/25/applying-essential-oil-to-anus-cures-coronavirus-iranian-cleric |	Cure | Natural Oils/Herbs |	not available

**The columns that are absolutely needed** for the dash app to run on your data are ***date***, ***full_text***, ***quoted_status***, ***user***, ***place***, ***retweet_count***, ***favorite_count***, ***URL_link***, ***topics***, ***narratives***, ***source_bias***. 

### Plotly Express scatter_geo figure data
This figure uses the ***date*** column for its animation frame. In order for this to work properly, you will need your data to follow the following guidelines. These guidelines will require you to add filler rows if you don't have enough data. We had to do this while creating a prototype. 

**Example of data without filler rows** (*Note: this will not work with the animation frame option*)
| category |	date	| tweet_id |
| --- | --- | --- |
| A	| 3/1	| 1000 |
| B |	3/1	| 1001 |
| B	| 3/1	| 1002 |
| D	| 3/5	| 1003 |
| C |	3/6 |	1004 |
| C |	3/6	| 1005 |

**Example of data with filler rows** (*Note: this will work with the animation frame option*)
The tweet_id for the filler rows is 0 as a way to flag in the program that it is a filler row. 
| category |	date	| tweet_id |
| --- | --- | --- |
| A	| 3/1	| 1000 |
| B |	3/1	| 1001 |
| B	| 3/1	| 1002 |
| C |	3/1 |	0 |
| D	| 3/1	| 0 |
| D	| 3/5	| 1003 | 
| A	| 3/5	| 0 |
| B	| 3/5	| 0 |
| C	| 3/5	| 0 |
| C	| 3/6	| 1004 |
| C	| 3/6	| 1005 |
| A	| 3/6	| 0 |
| B	| 3/6 |	0 |
| D	| 3/6 |	0 |

