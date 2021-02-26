from flask import Flask
from flask_restful import Api, Resource

from endpoints.login import Login
from endpoints.new_account import NewAccount
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
    api.add_resource(NewAccount, '/new-account')


@app.after_request
def after_request(response):
    """Required for CORS workaround.
    """
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


init_api()

if __name__ == '__main__':
    app.run(debug=True)
