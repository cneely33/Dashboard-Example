import dash
import dash_bootstrap_components as dbc
# import pathlib
# User management initialization
from os import getenv, path, getcwd
from flask import abort, request
# from flask_caching import Cache
from mods import secrets
# from werkzeug.security import generate_password_hash

## local imports
from exceptions import no_data_graphs
from mods.DBA import ProdTestEnvFunc as pt

try:
    secrets.load_env_vars()
except:
    print('unable to load env vars')
    pass   

no_data_fig = no_data_graphs.figure_none_line()

### Set color template for high cardinality cats
# high_card_color_template = px.colors.qualitative.Dark24 + px.colors.qualitative.Light24 + px.colors.qualitative.Prism
# remove_colors = ['#FB00D1', '#FF0092', '#00FE35', '#22FFA7', '#0DF9FF']
# for i in remove_colors:
#     high_card_color_template.remove(i)


# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash('Dash', 
                external_stylesheets=[dbc.themes.LUX],
                # suppress_callback_exceptions=True,
                # meta_tags=[{'name': 'viewport',
                #             'content': 'width=device-width, initial-scale=1.0'}]
                )


server = app.server
### optional cacheing of results pulled from long running process
# cache = Cache(server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory',
#     'CACHE_THRESHOLD': 100
# })

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# config
server.config.update(
    SECRET_KEY=getenv("SECRET_KEY"),
    SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URI"),
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    #### echo out queries 
    # SQLALCHEMY_ECHO = True,
    # SQLALCHEMY_RECORD_QUERIES = True
)

### optional add ip address in .env to whitelist
# IP_EXTERNAL will be the only element available in prod
# ip_addy_list = []
# ip_env = ['IP_LOOP', 'IP_EXTERNAL', 'IP_DOCKER_DEV']

# for i in ip_env:
#     ip_addy = getenv(i)
#     ip_addy_list.append(ip_addy)
    
# @server.before_request
# def limit_remote_addr():
#     value = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)   
#     if value not in ip_addy_list:
#         abort(403)  # Forbidden

