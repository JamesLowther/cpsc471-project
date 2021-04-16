from flask import make_response, jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import create_access_token

from database import db

parser = reqparse.RequestParser()
parser.add_argument("user_type", type=str, required=True, choices=("patient", "doctor", "clerk"),
                    help="Bad choice: {error_msg}")
parser.add_argument("ssn", type=str, required=True,
                    help="SSN for user logging in.")
parser.add_argument("password", type=str, required=True,
                    help="Password for user logging in.")


class Login(Resource):
    def post(self):
        """Handle post request to the login endpoint.
        """

        args = parser.parse_args()

        if args["ssn"] == "" or args["password"] == "":
            return {"logged_in": 0}

        status = False

        # Handle login for specfic user type.
        if args["user_type"] == "patient":
            status = login_patient(args)
        elif args["user_type"] == "doctor":
            status = login_doctor(args)
        elif args["user_type"] == "clerk":
            status = login_clerk(args)

        # User did not successfully log in.
        if not status:
            return {"logged_in": 0}

        access = create_access_token(
            identity={"user_type": args["user_type"], "ssn": args["ssn"]})
        data = {
            "logged_in": 1,
            "access_token": access,
            "user_type": args["user_type"],
            "ssn": args["ssn"]
        }
        response = make_response(jsonify(data), 200)

        return response


def login_patient(args):
    """Handle the login logic for patients.
    Return True if login successful and False otherwise.
    """

    con, cursor = db.connect_db()

    cursor.execute("SELECT * FROM Patient WHERE P_SSN = ? AND Password = ?;",
                   (args["ssn"], args["password"]))

    # No user in database with those credentials.
    res = cursor.fetchone()
    if not res:
        con.close()
        return False

    # User has correct credentials.
    con.close()
    return True


def login_doctor(args):
    """Handle the login logic for doctors.
    Return True if login successful and False otherwise.
    """
    con, cursor = db.connect_db()

    cursor.execute("SELECT * FROM Doctor WHERE SSN = ? AND Password = ?;",
                   (args["ssn"], args["password"]))

    # No user in database with those credentials.
    res = cursor.fetchone()
    if not res:
        con.close()
        return False

    # User has correct credentials.
    con.close()
    return True


def login_clerk(args):
    """Handle the login logic for clerks.
    Return True if login successful and False otherwise.
    """
    con, cursor = db.connect_db()

    cursor.execute("SELECT * FROM Clerk WHERE SSN = ? AND Password = ?;",
                   (args["ssn"], args["password"]))

    # No user in database with those credentials.
    res = cursor.fetchone()
    if not res:
        con.close()
        return False

    # User has correct credentials.
    con.close()
    return True
