from flask_restful import Resource, reqparse

from database import db

parser = reqparse.RequestParser()
parser.add_argument("user_type", type=str, required=True, choices=("patient", "doctor", "clerk"),
                    help="Bad choice: {error_msg}")
parser.add_argument("username", type=str, required=True,
                    help="Username for new account.")
parser.add_argument("password", type=str, required=True,
                    help="Password for new account.")


class NewAccount(Resource):
    def post(self):
        args = parser.parse_args()

        print(args)

        return {"Hello": "world"}
