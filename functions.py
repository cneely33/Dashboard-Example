def id_factory(page: str):
    def func(_id: str):
        """
        Dash pages require each component in the app to have a totally
        unique id for callbacks. This is easy for small apps, but harder for larger 
        apps where there is overlapping functionality on each page. 
        For example, each page might have a div that acts as a trigger for reloading;
        instead of typing "page1-trigger" every time, this function allows you to 
        just use id('trigger') on every page.
        https://community.plotly.com/t/how-do-we-repeat-element-id-in-multi-page-apps/41339
        How:
            prepends the page to every id passed to it
        Why:
            saves some typing and lowers mental effort
        **Example**
        # SETUP
        from system.utils.utils import id_factory
        id = id_factory('page1') # create the id function for that page
        
        # LAYOUT
        layout = html.Div(
            id=id('main-div')
        )
        # CALLBACKS
        @app.callback(
            Output(id('main-div'),'children'),
            Input(id('main-div'),'style')
        )
        def funct(this):
            ...
        """
        return f"{page}-{_id}"
    return func


def remove_figure_background(fig):
    fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
    return fig



def standard_nav_bar(brand_text, dropdown_menu):
    from dash import html
    import dash_bootstrap_components as dbc
    import dash_mantine_components as dmc
    from dash_iconify import DashIconify
    from os import getenv, path
    
    # base_exec_overview_url = getenv("EXEC_OVERVIEW_URL")
    # base_flextime_url = getenv("FLEXTIME_URL")
    
    # flex_time_call_log_url = base_flextime_url + "views/viz/calls_overview"
    # base_url = 'pc-assignment.j7bv674aangfm.us-east-1.cs.amazonlightsail.com'
    
    # curr_path = path.abspath(path.dirname(__name__))
    # path_proc = curr_path + '\\assets\\proc.png'
    # print(path_proc)
    
    return dbc.Navbar(
        dbc.Container([
            dbc.Col([], width=1),
                dbc.Nav([
                        dbc.Container(children=[
                                dbc.NavItem([
                                    dmc.ActionIcon(
                                        DashIconify(icon="system-uicons:menu-hamburger", width=20),
                                                    size="lg",
                                                    variant="filled",
                                                    color="red",
                                                    id="open-offcanvas",
                                                    n_clicks=0,
                                                    mb=10,
                                                ),
                                    dbc.Offcanvas([
html.A("Simple Sales Funnel", id='page1', 
       # href='pc-assignment.j7bv674aangfm.us-east-1.cs.amazonlightsail.com/views/pc'
       href='/views/pc'
       ),
html.P(""),
html.A("User Sessions", id='page2', 
       # href='pc-assignment.j7bv674aangfm.us-east-1.cs.amazonlightsail.com/views/pc2',
       href='/views/pc2'
       ),
html.P(""),
html.A("Sales Funnel Heat Map", id='page3', 
       # href='pc-assignment.j7bv674aangfm.us-east-1.cs.amazonlightsail.com/views/pc3',
       href='/views/pc3'
       ),
],
id="offcanvas",
    title="Multipage Dash App",
is_open=False,
                                                )
                                            ]),
                                            ]),
                        ],),
                # external Links
                html.A(
                        # Use row and col to control vertical alignment of logo / brand
                        dbc.Row(children=[   
                                dbc.Col(html.Img(src='/assets/dash-logo-stripe.svg', height="42px")),
                                ],
                            align="center",
                            class_name="g-0",
                        ),href="https://dash.plotly.com/",style={"textDecoration": "none"},
                        ),
              dbc.Col(children=[dbc.NavbarBrand(
                                               ' Assessment',
                                              class_name="ms-2"),
                      html.Div(id='user-name', className='ms-2', children=[]),
                      html.Div(id='logout', className='ms-2', children=[])
                      ], 
                      class_name="text-white"),
          # nav Items
############################################################################################################################      

                # dbc.Nav([
                    # html.Div(id='current_week2', children=['pagename'])
                            # ],
                #         class_name="text-white ms-auto",
                #         navbar=True,
                # ),
############################################################################################################################
                dbc.Col([
                    dbc.Row([
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                                dbc.Nav(
                                        [dropdown_menu],
                                        class_name="text-white",
                                        navbar=True,
                                        ),
                                id="navbar-collapse",
                                navbar=True,
                                class_name="text-white"
                                ),
                        ], class_name="d-flex justify-content-end")
                    ],
                    class_name="d-flex justify-content-end"
                    ),
                #
            dbc.Nav(
               dbc.Container(children=[
                  dbc.NavItem(html.Div(id='current_page_link',
                                       children=[
                                           dbc.NavLink("Chris Neely",
                                                       href="https://www.linkedin.com/in/neelychristopher/",
                                                       class_name="text-white",
                                                       external_link=True)
                                           ])),
                   ])
              ),
          dbc.Nav(
                 [html.Div(id='current_week', children=[])
                     ],
                 class_name="text-white ms-auto",
                 navbar=True,
                 ),
                         
                dbc.Col([], width=1),
############################################################################################################################                            
            ],class_name="m-1", fluid=True
        ),
        color="dark",
        dark=True,
        class_name="mb-2, p-1",
        )

