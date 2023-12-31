from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

#main app
from app import app
### connect to pages
from views import calls_overview, user_sessions, funnel_heatmap
import functions

content_div = html.Div(id='page-content', children=[])


## Diplay currentDashboard in NavBar
brand_text = "Dash"
dropdown_menu = ''

logo_navbar = functions.standard_nav_bar(brand_text, dropdown_menu)

url_holder = dcc.Location(id='url', refresh=False)

### place layout in function to reload data on page refresh
# def serve_layout():
#     return html.Div(children=[url_holder, logo_navbar, content_div])

# app.layout = serve_layout
app.layout = html.Div(children=[url_holder, logo_navbar, content_div])
app.title = 'Dash Multipage'

# Optional new in dash 1.12 to avoid call back exceptions associated with multipage apps dash.plotly.com/urls
# "complete" layout
app.validation_layout = html.Div([
    url_holder,
    logo_navbar,
    content_div,
    user_sessions.layout,
    funnel_heatmap.layout,
    calls_overview.layout,
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    
    if pathname == '/':
        return calls_overview.layout
       
    elif pathname == '/views/pc2':
        return user_sessions.layout
    
    elif pathname == '/views/pc3':
        return funnel_heatmap.layout
          
    elif pathname == '/views/pc':
        return calls_overview.layout
          
    else:
        return "404 Page Error! Page Not Found!"

#callback to toggle the collapse on small screens
@app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# for hamburger
@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


## needed for docker startup
server = app.server
    
## local run options only
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080, dev_tools_hot_reload=False)