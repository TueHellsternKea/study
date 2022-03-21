# Deploying Docker containers on Azure
We are going to deploy a Dash application on Azure using Docker and Azure Web App services.

# Content

# Create a Dash application running on Docker
First we need to create a docker image that we can use to develop and deploy our Dash application.

Create the Python file **dash_app.py**

```python
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Hello Dash")
])
if __name__ == "__main__":
    # Get port and debug mode from environment variables    
    port = os.environ.get('dash_port')
    debug = os.environ.get('dash_debug')=="True"
    app.run_server(debug=debug, host="0.0.0.0", port=port)
```

Create the requirements.txt

```txt
dash
pandas
numpy
requests
```


# Link
- [Deploying Docker containers on Azure](https://docs.docker.com/cloud/aci-integration/)