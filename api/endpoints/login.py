from flask_restful import Resource, reqparse

from database import db

parser = reqparse.RequestParser()
parser.add_argument("user_type", type=str, required=True, choices=("patient", "doctor", "clerk"),
                    help="Bad choice: {error_msg}")
parser.add_argument("username", type=str, required=True,
                    help="Username for user logging in.")
parser.add_argument("password", type=int, required=True,
                    help="Password for user logging in.")


class Login(Resource):
    def post(self):
        args = parser.parse_args()

        print(args)

        return {"Hello": "world"}
