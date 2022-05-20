from flask import jsonify, current_app
from pyms.flask.app import Microservice

ms = Microservice()
app = ms.create_app()


@app.route("/")
def example():
    return jsonify({"main": "hello world {}".format(current_app.config["APP_NAME"])})


if __name__ == '__main__':
    app.run()