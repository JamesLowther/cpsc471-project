from flask_restful import Resource, reqparse

from database import db

parser = reqparse.RequestParser()
parser.add_argument("user_type", type=str, required=True, choices=("patient", "doctor", "clerk"),
                    help="Bad choice: {error_msg}")
parser.add_argument("ssn", type=str, required=True,
                    help="SSN for new account.")
parser.add_argument("password", type=str, required=True,
                    help="Password for new account.")
parser.add_argument("Fname", type=str, required=False,
                    help="Doctor/Clerk first name.")
parser.add_argument("Lname", type=str, required=False,
                    help="Doctor/Clerk last name.")
parser.add_argument("Initial", type=str, required=False,
                    help="Doctor/Clerk initial.")
parser.add_argument("DoB", type=str, required=False,
                    help="Doctor/Clerk date of birth.")
parser.add_argument("Specialization", type=str, required=False,
                    help="Doctor specialization.")


class NewAccount(Resource):
    def post(self):
        """Handle post request to new-account endpoint.
        """

        args = parser.parse_args()

        status = False

        # Check user type.
        if args["user_type"] == "patient":
            status = create_patient(args)
        elif args["user_type"] == "doctor":
            status = create_doctor(args)
        else:
            status = create_clerk(args)

        if not status:
            return {"successful": 0}

        return {"successful": 1}


def create_patient(args):
    """Handle the account logic for patients.
    """
    con, cursor = db.connect_db()

    cursor.execute("SELECT * FROM Patient WHERE P_SSN = ?;", (args["ssn"],))

    # User already exists in database
    if cursor.fetchone():
        return False

    # Add the patient to the database.
    cursor.execute("INSERT INTO Patient VALUES (?, ?);",
                   (args["ssn"], args["password"]))
    con.commit()
    con.close()

    return True


def create_doctor(args):
    """Handle the account logic for doctors.
    """
    con, cursor = db.connect_db()

    cursor.execute("SELECT * FROM Doctor WHERE SSN = ?;", (args["ssn"],))

    # User already exists in database
    if cursor.fetchone():
        return False

    # Add the doctor to the database.
    cursor.execute("INSERT INTO Doctor VALUES (?, ?, ?, ?, ?, ?, ?);",
                   (args["ssn"], args["Specialization"], args["Fname"], args["Lname"], args["Initial"], args["DoB"], args["password"]))

    con.commit()
    con.close()

    return True


def create_clerk(args):
    """Handle the account logic for clerks.
    """
    con, cursor = db.connect_db()

    cursor.execute("SELECT * FROM Clerk WHERE SSN = ?;", (args["ssn"],))

    # User already exists in database
    if cursor.fetchone():
        return False

    # Add the clerk to the database.
    cursor.execute("INSERT INTO Clerk VALUES (?, ?, ?, ?, ?, ?);",
                   (args["ssn"], args["Fname"], args["Lname"], args["Initial"], args["DoB"], args["password"]))

    con.commit()
    con.close()

    return True
