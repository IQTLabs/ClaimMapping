'''
name: langDetect.py

Description: performs language detection on a tweet's text by using langdetect method

functions:
	langDetectMethod(data_files, langDetectDict, nFiles)
'''
from langdetect import detect, lang_detect_exception, DetectorFactory

def langDetectMethod(data_files, langDetectDict, nFiles):
	'''
	Detects language using langdetect

	Parameters:
		data_files: file path from config.yml
		langDetectDict: you can pass in an empty dictionary or a dictionary to continue frmo a previous month.
		nFiles: number of files that you have to pass through for progress print statements
	'''

	numFiles = nFiles
	count = 0.0

	for file in data_files:
		df = pd.read_json(str(file), lines=True)
		for i in range(len(df)):
			DetectorFactory.seed = 0
			detected_lang = None
			try: 
				strkey = detect(df.loc[i]['full_text'])             
			except:
				strkey = 'und'
	        
			if strkey in langDetectDict:
				langDetectDict[strkey] += 1
			else:
				langDetectDict[strkey] = 1
		count += 1
        
		if count%5 == 0:
			print("completed: {:.2}%".format(count/numFiles))

	return langDetectDict