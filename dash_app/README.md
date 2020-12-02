# Dash App
This dash app is for the COVID-19 Claim Mapping Interactive Visualizations.
This visualization is only a prototype and should not be used for an end-to-end analysis of claims made on Twitter during the COVID-19 Pandemic.
Check out our [supplementary guide](https://iqtlabs.github.io/Infodemic-Mapping/) to view more about how you should use this visualizaton.
Check out the [data](https://github.com/IQTLabs/ClaimMapping/tree/master/dash_app/data) folder to view guidelines on how you can use this dash app with your own Twitter data!

## Folder Structure
The structure of this folder can be seen below.
The main dash app file is *app.py*. *app.py* relies on three files: *callbacks.py*, *styles_files.py*, and *layouts.py*.
The hand-curated labeled dataset for this dash app is located in the data folder called *combinedTEST.csv*.
The creation of this dataset can be viewed [here](https://iqtlabs.github.io/Infodemic-Mapping/).
The *Procfile* is used to deploy this dash app to Heroku and should not be changed.
To change text or variables used in *layouts.py*, *callbacks.py*, or any of the functions in the func folder, edit the *config.yml* file located in the config folder.
All requirements for this dash app folder are located in *requirements.txt*.
```bash
├── Procfile
├── README.md
├── __init__.py
├── app.py
├── callbacks.py
├── config
│   └── config.yml
├── data
│   └── combinedTEST.csv
├── func
│   ├── __init__.py
│   ├── append_cols.py
│   ├── clean_csv.py
│   ├── generate_area_fig.py
│   ├── generate_geo_fig.py
│   ├── generate_scatter_fig.py
│   ├── prep_plotly.py
│   ├── process_data.py
│   └── read_data.py
├── layouts.py
├── requirements.txt
└── styles_file.py
```

## Heroku Deployment Instructions
You can clone or download this folder without needing the folders or files from the rest of the Infodemic repo.
Once you clone or download this folder, navigate to this folder in your terminal and run ```pip3 install -r requirements.txt```.
This will install all packages required to get the dash app up an running. 

You can deploy your own version of this dash app to Heroku by following the [Dash Heroku Deployment instructions](https://dash.plotly.com/deployment) or by following the quick instructions here below. Make sure that you have your own Heroku account before you start - you can make one [here](https://id.heroku.com/login). If you don't have the [Heroku CLI installed](https://devcenter.heroku.com/articles/heroku-cli), download it (```brew install heroku```) before following the instructions below.

**Instructions to Deploy Dash App using Heroku CLI**
1. Navigate to the **dash_app** folder: ```cd ClaimMapping/dash_app``` 
2. Install the requirements for the dash app: ```pip3 install -r requirements.txt```
3. Initiate Heroku: ```heroku create my-dash-app``` (change 'my-dash-app' to what you want to name your Heroku app). 
4. Git push: ```git push heroku master```
5. ```heroku ps:scale web=1```

Anytime you make changes and want to update the deployed dash app, you will only need to type step 4 above in terminal to commit your changes.

### Troubleshooting 
**Deployment Errors**:
If you try to deploy your own version of this dash app to Heorku and it gives you an error about being unable to create a buildpack, please make sure you are in the folder (in terminal) when deploying. It will not work if you create a folder called _MyProject_ and then place the _dash_app_ folder within that folder and deploy _MyProject_ as a Heroku app. You will have to take all the files in the _dash_app_ folder and move them iindividually in _MyProject_ folder. 

**Heroku Deployment using GitHub Repo**: 
The dash files need to be isolated in their own repository or else Herokue will not be able to identify a program language.

**Plotly Figures showing year 2000**:
This will only happen if you end up using a CSV file. The date column in the CSV file will need to be reformatted to yyyy-mm-dd. It sometimes switches to mm/dd/yy and it thinks 03/01/20 is March 1st, 2000.
