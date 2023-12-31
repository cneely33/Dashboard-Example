from dash.dependencies import Output, Input
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
# from datetime import datetime as dt
# import plotly.express as px
from plotly import graph_objects as go

from app import app, no_data_fig
from data.pull_flex_time_results import  load_funnel
import functions


####################################################################################################
## Graph properties ##

## create callback id prefex generator
id_gen = functions.id_factory('calls_overview')

df_funnel = load_funnel()

# initial_visible_month = dt(current_year, max_dt_start.month, 1)
margins=dict(t=20, l=0, r=0, b=10)
# axis_font=dict(family='Arial', color='black', size=20)

group_list = sorted(df_funnel['funnel_group'].unique())
group_list_output = [{'label': l, 'value': l} for l in group_list]

######################## Create Filter Controls ########################

layout =  dbc.Container([ 
    dbc.Row([
        dbc.Col([
                html.Div([
                    html.Br(),
                      html.H3("Select Funnel Type:", style={"text-align": "center"}),
          
                     dcc.RadioItems(
                     id=id_gen('funnel_radio'),
                     options=group_list_output,
                      value='Non-Cohortal Funnel',
                     # style={'display': 'inline-block'},
                     inputStyle={"margin-left": "10px", "margin-right": "5px", }
                                 ),
                      ], style={'textAlign': 'center',}),
              ], align='center',
            # xs=12, sm=12, md=6, lg=6, xl=6
            xs=12, sm=12, md=12, lg=12, xl=12
            ),
        # dbc.Col([
        #         html.Div([
        #                 html.P(''),
        #               ], style={'textAlign': 'center',}),
        #       ], align='center',
        #     xs=12, sm=12, md=6, lg=6, xl=6
        #     ),
    
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
                    # html.H2("Sales Funnel", style={"text-align": "center"}),
                  ######
                  dcc.Graph(id=id_gen('sales_funnel'),
                            figure={},
                            style={"height": "98%"},
                            config = {'displayModeBar': False}
                            ),
                  ######
                ], 
                    style={
                    'textAlign': 'center',
                    "height": "100%",
                    "width": '100%',
                    "border":"2px black solid",
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
                style={"height": "90%"},
                class_name='mt-2 d-flex'
            ),                    
####################           
####################

], fluid=True, 
style={"height": "88vh",
# "background-color": "green"
}
)
         
@app.callback(Output(id_gen('sales_funnel'), 'figure'),
          [Input(id_gen('funnel_radio'), 'value'),
          ])
def call_summary_datatable(funnel_radio_value):
    try:
        ## Load data from state
        df_funnel_copy = df_funnel.copy()
        
        if funnel_radio_value == 'Non-Cohortal Funnel':
            df_funnel_copy = df_funnel_copy[df_funnel_copy['funnel_group'] == funnel_radio_value]
            
            # fig = px.funnel(df_funnel_copy, x='QA Leads Count', y='Stage')
            # 
            fig = go.Figure(go.Funnel(
                        y = df_funnel_copy['Stage'],
                        x =  df_funnel_copy['QA Leads Count'],
                        textposition = "inside",
                        textinfo = "value+percent initial",
                       
                        )
                    )
            
        else:
            df_funnel_copy = df_funnel_copy[df_funnel_copy['funnel_group'] == funnel_radio_value]
            
            # fig = px.funnel(df_funnel_copy, x='QA Leads Count', y='Stage', color='YYYYMM')
            
            fig = go.Figure()
            
            for i in df_funnel_copy['YYYYMM'].unique():
                df_fun_sub = df_funnel_copy[df_funnel_copy['YYYYMM'] == i]
                
                fig.add_trace(go.Funnel(
                            name=i,
                            orientation = "h",
                            y = df_fun_sub['Stage'],
                            x =  df_fun_sub['QA Leads Count'],
                            textposition = "inside",
                            textinfo = "value+percent initial",
                           
                            )
                        )
            
        fig.update_layout(
                        modebar_add=['drawline', 'eraseshape'], 
                        margin=dict(t=0, r=0, l=45, b=10),   
            )
       
        fig = functions.remove_figure_background(fig)
        
    except Exception as e:
        print(e)
        fig = no_data_fig
        
    return fig
    