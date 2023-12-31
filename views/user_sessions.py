from dash import html
import dash_bootstrap_components as dbc
import functions

id_gen = functions.id_factory('TableauSessions')

######################## Create Filter Controls ########################

layout =  dbc.Container([ 
   
    dbc.Row([
        dbc.Col([
                html.Div([
                    # html.Br(),
                      html.H3("Tableau Snip: User Sessions Over Time by Contact Source", style={"text-align": "center"}),
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
                 html.Img(src='/assets/userSessions.PNG')
                  ######
                ], 
                    style={
                    'textAlign': 'center',
                    # "height": "100%",
                    # "width": '100%',
                    # "border":"2px black solid",
                    'margin': 'auto'
                    }
                ),
            ], width=6, align='center', 
                    xs=12, sm=12, md=12, lg=12, xl=12,
                # style={"height": "100%",
            # "background-color": "purple" 
            # }
            ),
        ],align='center',
                justify='center',
                style={"height": "80%%"},
                class_name='mt-2 d-flex'
            ),                    
####################
         
####################

], fluid=True, 
style={"height": "88vh",
# "background-color": "green"
}
)
         
