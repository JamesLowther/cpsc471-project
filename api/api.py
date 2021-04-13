from datetime import datetime
from datetime import timedelta
from datetime import timezone

from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

from endpoints.login import Login
from endpoints.new_account import NewAccount
from endpoints.keys import Keys
from endpoints.entities import EntitiesForms
from endpoints.patient import Patient, PatientForms
from endpoints.doctor import Doctor, DoctorForms

from endpoints.clerk import Clerk, ClerkForms

from database import db

app = Flask(__name__)
CORS(app=app, supports_credentials=True)
app.config["JWT_SECRET_KEY"] = "GRu7cjtC5YwbKBS*#jmHz"
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

api = Api(app)
jwt = JWTManager(app)

# Taken from https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/
@app.after_request
def refresh_expiring_jwts(response):
    """Refresh any JWT tokens that are set to expire in 30 minutes.
    """
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

def init_api():
    """ Call functions which initialize the API.
    """
    db.init_db()
    add_api_endpoints()


def add_api_endpoints():
    """ Adds all of the endpoints to our API.
    Endpoints need to be imported from the endpoints module.
    """

    # General endpoints.
    api.add_resource(Login, '/login')
    api.add_resource(NewAccount, '/new-account')
    api.add_resource(Keys, "/keys")

    # Patient endpoints.
    api.add_resource(Patient, '/patient')
    api.add_resource(PatientForms, '/patient/forms')

    # Clerk
    api.add_resource(Clerk, '/clerk')
    api.add_resource(ClerkForms, '/clerk/forms')

    # Doctor
    api.add_resource(Doctor, '/doctor')
    api.add_resource(DoctorForms, '/doctor/forms')

    # Entity
    api.add_resource(EntitiesForms, '/entities/forms')


init_api()

if __name__ == '__main__':
    app.run(debug=True)
