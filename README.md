# Dashboard-Example
Multi-page dashboard app using Docker, Dash, Plotly, and Tableau

TODO: dashboard can be found at:

Steps to start local instance
1.  Create secrets file at .\mods
      a. need "SECRET_KEY" ENV variable for dash app server
2.  docker build -t dash_example:v1 -f Dashboard-Example/Dockerfile .
3.  docker run -d -p 8080:8080 --name dash_ex dash_example:v1
