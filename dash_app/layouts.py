'''
Name: layouts.py
Description: The layout of the dash app is located in this file. Any HTML or Markdown that is designing the layout of the app 
is located in the main function layout and returned to app.py
Functions:
    layout()
author: @Katelyn98
'''
import dash_core_components as dcc
import dash_html_components as html
import config_with_yaml as config
import styles_file as sf

#load in config file
cfg = config.load("config/config.yml")

def layout():
    '''
    Returns the layout of the dash app
        Returns:
            HTML and Markdown Dash layout
    '''
    return html.Div(children=[
    html.H2(children=cfg.getProperty("dash_app.title"), style=sf.styles['title']),
    html.P(children = [cfg.getProperty("dash_app.dash_text.intro_P1"), 
        html.A('Supplementary Guide', href='https://iqtlabs.github.io/Infodemic-Mapping/'), cfg.getProperty("dash_app.dash_text.intro_P2")], 
        style=sf.styles['text']),
    html.Div(children=[

        #figures on the left side
        html.Div(children=[
            html.H3(cfg.getProperty("dash_app.dash_text.leftSide.headingLeft")),
            dcc.Tabs(id='tabs-narratives', value=cfg.getProperty("dash_app.dash_text.leftSide.valueDefault"), children=[
                dcc.Tab(label=cfg.getProperty("dash_app.dash_text.leftSide.tabLeft"), value=cfg.getProperty("dash_app.dash_text.leftSide.valueLeft"), style=sf.tab_style, selected_style=sf.tab_selected_style),
                dcc.Tab(label=cfg.getProperty("dash_app.dash_text.leftSide.tabRight"), value=cfg.getProperty("dash_app.dash_text.leftSide.valueRight"), style=sf.tab_style, selected_style=sf.tab_selected_style),
            ]),
            html.Div(id='tabs-narratives-content')
        ], className ="six columns"),
        
        #figures on the right side
        html.Div(children=[
            html.H3(cfg.getProperty("dash_app.dash_text.rightSide.headingRight")),
            dcc.Tabs(id='tabs-claims-range', value='tab-1', children=[
                dcc.Tab(label=cfg.getProperty("dash_app.dash_text.rightSide.tab1"), value=cfg.getProperty("dash_app.dash_text.rightSide.valueTab1"), style=sf.tab_style, selected_style=sf.tab_selected_style),
                dcc.Tab(label=cfg.getProperty("dash_app.dash_text.rightSide.tab2"), value=cfg.getProperty("dash_app.dash_text.rightSide.valueTab2"), style=sf.tab_style, selected_style=sf.tab_selected_style),
                dcc.Tab(label=cfg.getProperty("dash_app.dash_text.rightSide.tab3"), value=cfg.getProperty("dash_app.dash_text.rightSide.valueTab3"), style=sf.tab_style, selected_style=sf.tab_selected_style),
            ]),
        ], className="six columns"),
        html.Div(id='tabs-claims-range-content', className ="six columns")
    ], className="row"),
    
], style=sf.styles['text']) 