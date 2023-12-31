# from dash.dependencies import Output, Input
from dash import dash_table, dcc, html
from dash.dash_table.Format import Format, Align
import dash_bootstrap_components as dbc
# import plotly.express as px
import functions

from app import app, no_data_fig
from data.pull_flex_time_results import load_medium_funnel


## create callback id prefex generator
id_gen = functions.id_factory('FunnelHeatMap')

######################## Create Filter Controls ########################
layout =  dbc.Container([ 
   
    dbc.Row([
        dbc.Col([
                html.Div([
                    # html.Br(),
                      html.H3("Tableau Snip: Heatmap of Sales Funnel", style={"text-align": "center"}),
                     
                      ], style={'textAlign': 'center',}),
              ], align='center',
            # xs=12, sm=12, md=6, lg=6, xl=6
            xs=12, sm=12, md=12, lg=12, xl=12
            ),
    
    ],align='center',
        justify='center',
      style={'margin': 'auto'
          # "height": "10%",
            # 'width': '50%',
            # "background-color": "green"
            }), 
# ############################################################################     
    dbc.Row([       
            dbc.Col([
                html.Div([
                  ######
                 html.Img(src='/assets/SalesFunnelHeatMap.PNG')
                  ######
                ], 
                    style={
                    'textAlign': 'center',
                    "height": "100%",
                    "width": '100%',
                    # "border":"2px black solid",
                    'margin': 'auto'
                    }
                ),
            ], width=6, align='center', 
                    xs=12, sm=12, md=12, lg=12, xl=12,
                style={"height": "100%",
            # "background-color": "purple" 
            }
            ),
        ],align='center',
                justify='center',
                style={"height": "60%"},
                class_name='mt-2 d-flex'
            ),                 
####################
####################

], fluid=True, 
style={"height": "88vh",
# "background-color": "green"
}
)
         

    