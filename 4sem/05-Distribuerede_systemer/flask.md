# Flask demo


## Install Flask
You have to install Flask with

    pip3 install flask

*Consider using a virtual environment*

## Code
A minimal Flask application could be something like this:

```python
# Importing flask module in the project is mandatory
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
```

