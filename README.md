# Claim Mapping Visualization & Analysis
All examples, documentation, and scripts related to claim mapping can be found in this folder. 
To run scripts and customize the scripts in this folder, please follow the steps below:
1) Clone or download the ClaimMapping repository to your local machine: ```git clone https://github.com/IQTLabs/ClaimMapping```
2) Navigate to the ClaimMapping folder via terminal: ```cd ClaimMapping```
3) Execute this command in terminal: ```pip3 install -r req.txt```

A demo of the narrative and claim-mapping dash app core functionalities can be seen below. 
<p align="center">
  <img src="https://github.com/IQTLabs/ClaimMapping/tree/master/analysis/results/final-demo.gif" /> 
</p>

All the code for the dash app can be found in the [dash app](https://github.com/IQTLabs/ClaimMapping/tree/master/dash_app) folder of this repo.

## Folder Structure
The structure of the ClaimMapping directory and the specifics of each folder are listed below.
For more in depth detail on each folder, navigate to that folder to view its specific README.md.
```bash 
├── README.md
├── dash_app
├── jupyter_notebooks
├── analysis
    ├── results
├── req.txt
└── tests
``` 
The **dash_app** folder is home to all scripts for the Claim Mapping Dash App. This folder is self contained and can be run on its own.
The **jupyter_noteooks** folder has several notebooks that provide examples of prototypes. 
It also breaks down steps used to create the hand-curated labeled dataset of tweets for prototyping a claim mapping visualization.
The **analysis** folder is composed of code from the **jupyter_notebooks** folder.
The code in **analysis** converted the code from the jupyter notebooks into scripts to be used on data via the terminal instead of via Jupyter. 
The *README.md* in this directory provides an in depth discussion of analyses explored and prototyped throughout the process of developing the claim mapping visualization. 
This *README.md* is updated on a biweekly basis. 
The **analysis/results** directory has several images from prototyping and performing experiments throughout the development of the Claim Mapping visualization.
In some cases the Jupyter Notebook file may not show the resulting figure - those images can be found in **analysis/results**.
This generally only happens for the plotly figures.
Any side experiments with Dash and Plotly can be found in the **tests** folder - currently has one test on the Dash slider functionality to prepare for cross-filtering.

## Claim Mapping Dash App
The **dash_app** folder has more specifics on how to get the dash app deployed. View the *README.md* in the **dash_app** folder for more information. 
