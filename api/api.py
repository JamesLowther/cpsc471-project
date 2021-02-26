from flask import Flask
from flask_restful import Api, Resource

from endpoints.login import Login
from database import db

app = Flask(__name__)
api = Api(app)


def init_api():
    """ Call functions which initialize the API.
    """
    db.init_db()
    add_api_endpoints()


def add_api_endpoints():
    """ Adds all of the endpoints to our API.
    Endpoints need to be imported from the endpoints module.
    """
    api.add_resource(Login, '/login')


if __name__ == '__main__':
    init_api()
    app.run(debug=True)
