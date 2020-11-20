'''
Name: callbacks.py
Description: All callbacks for dash app are located in this file. All calbacks are located in the function
performCallbacks. Once all callbacks are completed, the app is returned to app.py
Functions:
	performCallbacks(app, clean_res_df)
	update_figure(value, clickData)
	render_world(value)
	render_content(tab)
	render_scatter(value)
author: @Katelyn98
'''
import dash
import json
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import func.generate_geo_fig as ggf
import func.generate_area_fig as gaf
import func.generate_scatter_fig as gsf
import func.process_data as prod
import config_with_yaml as config
import layouts
import styles_file as sf

#load in config file
cfg = config.load("config/config.yml")
default_geo = 'usa'

def performCallbacks(app, clean_res_df):
	'''
	Returns all callbacks made to app.py

	Parameters:
		app: dash app iniation
		clean_res_df: pandas dataframe

	Returns:
		app: modififed dash app
	'''

	## LEFT SIDE CONTENT
	#Callback for tweet metadata - referenced by callback below
	@app.callback(
	    Output('click-data', 'children'),
	    [Input('radio_meta', 'value'), Input('claim-map-figure', 'clickData')])
	def update_figure(value, clickData):
	    tweetData = json.dumps(clickData, indent=2)
	    dictData = json.loads(tweetData)
	    #Print dictData if the indices of full_text or source_url or bias ever get messed up
	    # print(dictData)
	    try:
	        full_text = dictData['points'][0]['customdata'][cfg.getProperty("dash_app.dash_text.tweetMeta.full_text_id")]
	        source_url = dictData['points'][0]['customdata'][cfg.getProperty("dash_app.dash_text.tweetMeta.source_url_id")]
	        bias = dictData['points'][0]['customdata'][cfg.getProperty("dash_app.dash_text.tweetMeta.bias_id")]
	    except:
	        full_text = "Not available"
	        source_url = "Not available"
	        bias = "Not available"

	    if value == 'showMeta':

	        return html.Div(children=[
	                html.Meta(charSet='UTF-8'),
	                html.H4(cfg.getProperty("dash_app.dash_text.tweetMeta.title")),
	                html.P(cfg.getProperty("dash_app.dash_text.tweetMeta.intro_P")),
	                #Show Full_text
	                dcc.Markdown('''**Text:**'''),
	                html.P(full_text),
	                #Show URL Link (aka source)
	                dcc.Markdown('''**Source:**'''),
	                dcc.Markdown(source_url),
	                #Show political bias
	                dcc.Markdown('''**Political Bias**'''),
	                html.P(bias)])

	#Callback to change scope of Topics map referenced by callback below
	@app.callback(
	    Output('claim-map-figure', 'figure'),
	    [Input('radio_world', 'value')])
	def render_world(value):
		return ggf.generateWorld(clean_res_df, value, '')

	#Callback to create options for adjusting map scope and options to show metadata. References two callbacks above
	@app.callback(Output('tabs-narratives-content', 'children'),
		              [Input('tabs-narratives', 'value')])
	def render_claim_content(tab):
	    available_claims = clean_res_df['topics'].unique()
	    if tab == 'topics':
	        return html.Div([
	            dcc.Graph(id='claim-map-figure'),
	            dcc.RadioItems(id='radio_meta',options=[
	            	{'label': cfg.getProperty("dash_app.radio_items.twitter.label1"), 'value': cfg.getProperty("dash_app.radio_items.twitter.value1")},
	            	{'label': cfg.getProperty("dash_app.radio_items.twitter.label2"), 'value': cfg.getProperty("dash_app.radio_items.twitter.value2")}],
	            	value=cfg.getProperty("dash_app.radio_items.twitter.defaultValue"),
	            	labelStyle={'display': cfg.getProperty("dash_app.radio_items.display")}),
	            dcc.RadioItems(id='radio_world',
	            	options=[{'label': cfg.getProperty("dash_app.radio_items.world.label1"), 'value': cfg.getProperty("dash_app.radio_items.world.value1")},
	            	{'label': cfg.getProperty("dash_app.radio_items.world.label2"), 'value': cfg.getProperty("dash_app.radio_items.world.value2")},
	            	{'label': cfg.getProperty("dash_app.radio_items.world.label3"), 'value': cfg.getProperty("dash_app.radio_items.world.value3")},
	            	{'label': cfg.getProperty("dash_app.radio_items.world.label4"), 'value': cfg.getProperty("dash_app.radio_items.world.value4")},
	            	{'label': cfg.getProperty("dash_app.radio_items.world.label5"), 'value': cfg.getProperty("dash_app.radio_items.world.value5")},
	            	{'label': cfg.getProperty("dash_app.radio_items.world.label6"), 'value': cfg.getProperty("dash_app.radio_items.world.value6")}],
	            	value=cfg.getProperty("dash_app.radio_items.world.defaultValue"),labelStyle={'display': cfg.getProperty("dash_app.radio_items.display")}), 
	            html.Pre(id='click-data', style=sf.styles['pre'])
	        ])
	    elif tab == 'narratives':
	        return html.Div([
	        	html.P(cfg.getProperty("dash_app.dash_text.leftSide.tabRight_subtxt")),
	        	dcc.Dropdown(
	                id='narratives-category',
	                options=[{'label': i, 'value': i} for i in available_claims],
	                value='category-narrative'
	            ),
	            html.Pre(id='claim-map-figure2'),  
	        ])

	#Callback to adjust the map view to show narratives based on topics - referenced in the callback above
	@app.callback(Output('claim-map-figure2', 'children'),
	                [Input('narratives-category', 'value')])
	def render_scatter(value):
	    try:
	        iggeo = ggf.generateWorld(clean_res_df, default_geo, value)
	        return html.Div([
	                dcc.Graph(id='claim-map-figure', figure=iggeo),
	                dcc.RadioItems(id='radio_meta',options=[
	            	{'label': cfg.getProperty("dash_app.radio_items.twitter.label1"), 'value': cfg.getProperty("dash_app.radio_items.twitter.value1")},
	            	{'label': cfg.getProperty("dash_app.radio_items.twitter.label2"), 'value': cfg.getProperty("dash_app.radio_items.twitter.value2")}],
	            	value=cfg.getProperty("dash_app.radio_items.twitter.defaultValue"),
	            	labelStyle={'display': cfg.getProperty("dash_app.radio_items.display")}),
	            	html.Pre(id='click-data', style=sf.styles['pre'])
	            ], style=sf.styles['pre'])
	    except:
	        pass


	## RIGHT SIDE CONTENT
	#Callback for which tab is clicked on 
	@app.callback(Output('tabs-claims-range-content', 'children'),
	              [Input('tabs-claims-range', 'value')])
	def render_content(tab):

		if tab == 'tab-1':
	    	#generate the area figure
			area_fig = gaf.generateAreaFigure(clean_res_df, cfg.getProperty("dash_app.dash_text.rightSide.figures.tab1.area_legend"), cfg.getProperty("dash_app.dash_text.rightSide.figures.tab1.area_title"))
			available_claims = clean_res_df[cfg.getProperty("dash_app.dash_text.rightSide.figures.tab1.area_legend")].unique()
			return html.Div([
				html.P(cfg.getProperty("dash_app.dash_text.rightSide.figures.tab1.area_subtxt")),
				dcc.Graph(id='g2', figure=area_fig)
			])
		elif tab == 'tab-2':
			#generate the area figure
			area_fig = gaf.generateAreaFigure(clean_res_df, cfg.getProperty("dash_app.dash_text.rightSide.figures.tab2.area_legend"), cfg.getProperty("dash_app.dash_text.rightSide.figures.tab2.area_title"))
			available_claims = clean_res_df[cfg.getProperty("dash_app.dash_text.rightSide.figures.tab2.area_legend")].unique()

			return html.Div([
				html.P(cfg.getProperty("dash_app.dash_text.rightSide.figures.tab2.area_subtxt")),
				dcc.Graph(id='g2', figure=area_fig)
			])
		elif tab == 'tab-3':
			available_claims = clean_res_df[cfg.getProperty("dash_app.dash_text.rightSide.figures.tab3.area_legend")].unique()
			return html.Div([
				html.P(children =[cfg.getProperty("dash_app.dash_text.rightSide.figures.tab3.area_subtxt1"), html.A(cfg.getProperty("dash_app.dash_text.rightSide.figures.tab3.area_linkTxt"), href=cfg.getProperty("dash_app.dash_text.rightSide.figures.tab3.area_link"))]),
				html.P(cfg.getProperty("dash_app.dash_text.rightSide.figures.tab3.area_subtxt2")),
				dcc.Dropdown(
					id='claims_category',
					options=[{'label': i, 'value': i} for i in available_claims],
					value='category-political-claim'
				),
				html.Pre(id='political-claims'),
			])

	#Callback to change the political affiliation map - referenced in callback above. 
	@app.callback(Output('political-claims', 'children'),
	                [Input('claims_category', 'value')])
	def render_scatter(value):
	    try:
	        fig3 = gsf.generatePoliticalScatter(clean_res_df, value)
	        return html.Div([
	                dcc.Graph(id='g3', figure=fig3)
	            ])
	    except:
	        pass

	return app