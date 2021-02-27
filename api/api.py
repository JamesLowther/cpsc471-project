from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

from flask_jwt_extended import JWTManager

from endpoints.login import Login
from endpoints.new_account import NewAccount
from endpoints.patient import Patient

from database import db

app = Flask(__name__)
CORS(app=app, supports_credentials=True)
app.config["JWT_SECRET_KEY"] = "GRu7cjtC5YwbKBS*#jmHz"

api = Api(app)
jwt = JWTManager(app)

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
    api.add_resource(Patient, '/patient')


init_api()

if __name__ == '__main__':
    app.run(debug=True)
