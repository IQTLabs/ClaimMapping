'''
name: ensemble.py

description: Detects the language of a tweet using the ensemble method. Prints out counts of langdetect, twitterlang, and ensemble method

functions:
	ensembleMethod(data_files)
'''
import pandas as pd
from langdetect import detect, lang_detect_exception, DetectorFactory
import func.ensemblePrint as ep

def ensembleMethod(data_files):
	'''
	Ensemble method to determine the language of a tweet. Calls ensemblePrint.py to print out result

	Parameters:
		data_files: string path can be changed in config.yml

	Returns:
		print statement of result
	'''

	ensembleMethod = {}
	count = 0
	file = 0

	for file in data_files:
		print("file opened")
		try:
			df = pd.read_json(str(file), lines=True)
			for i in range(len(df)):
				count += 1
				#Twitter Language
				strkey = df.loc[i]['lang']

				#Langdetect
				DetectorFactory.seed = 0
				detected_lang = None
				try: 
					ld_strkey = detect(df.loc[i]['full_text'])             
				except:
					ld_strkey = 'und'

				#create nested dictionary
				ensembleMethod[count] = {}
				ensembleMethod[count]['twitterLang'] = strkey
				ensembleMethod[count]['langDetect'] = ld_strkey
		except:
			pass

	#turn dictionary into dataframe
	df = pd.DataFrame.from_dict(ensembleMethod, orient='index')

	#print out counts for given language
	ep.printCount(df)