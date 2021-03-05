from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json


class Patient(Resource):
    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        return jsonify({**current, "logged_in": 1})


forms_parser = reqparse.RequestParser()
forms_parser.add_argument("form_type", type=str, required=True, choices=("report", "new_applicant_form", "medical_history", "covid_screen"),
                          help="Bad choice: {error_msg}")
forms_parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form"),
                          help="Bad choice: {error_msg}")
forms_parser.add_argument("report_id", type=int, required=False)
forms_parser.add_argument("applicant_form", type=str, required=False)
forms_parser.add_argument("history_id", type=int, required=False)
forms_parser.add_argument("screen_date", type=str, required=False)
forms_parser.add_argument("form", type=dict)


class PatientForms(Resource):
    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

        # Get all reports.
        cursor.execute(
            "SELECT Report_ID FROM Report WHERE P_SSN = ?;", (current["ssn"],))
        reports = cursor.fetchall()

        # Get all new applicant forms.
        cursor.execute(
            "SELECT Email FROM New_Applicant_Form WHERE P_SSN = ?;", (current["ssn"],))
        new_applicant = cursor.fetchall()

        # Get all covid screens.
        cursor.execute(
            "SELECT Date FROM Covid_Screen WHERE P_SSN = ?;", (current["ssn"],))
        covid_screen = cursor.fetchall()

        # Get medical history forms.
        cursor.execute(
            "SELECT HID FROM Medical_History WHERE P_SSN = ?;", (current["ssn"],))
        medical_history = cursor.fetchall()

        con.close()

        return jsonify(
            logged_in=1,
            reports=[dict(x) for x in reports],
            new_applicant=[dict(x) for x in new_applicant],
            covid_screen=[dict(x) for x in covid_screen],
            medical_history=[dict(x) for x in medical_history]
        )

    def post(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = forms_parser.parse_args()

        if (args["action_type"] == "submit_form"):
            if (args["form_type"] == "report"):
                pass

            elif (args["form_type"] == "new_applicant_form"):
                self.update_new_applicant_form(current["ssn"], args["form"])

            elif (args["form_type"] == "medical_history"):
                pass

            else:
                pass
    
        else:
            if (args["form_type"] == "report"):
                pass 

            elif (args["form_type"] == "new_applicant_form"):
                form = self.get_new_applicant_form(current["ssn"], args["applicant_form"])

            elif (args["form_type"] == "medical_history"):
                pass

            else:
                pass

            return jsonify(
                logged_in=1,
                form=dict(form)
            )
        
    def get_new_applicant_form(self, ssn, email):

        con, cursor = db.connect_db()

        cursor.execute("SELECT * FROM New_Applicant_Form WHERE P_SSN = ? AND Email = ?;", (ssn, email))
        result = cursor.fetchone()

        con.close()

        return result

    def update_new_applicant_form(self, ssn, form):

        con, cursor = db.connect_db()

        cursor.execute("INSERT OR REPLACE INTO New_Applicant_Form VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            (
                form["email"],
                ssn,
                form["gender"],
                form["sex"],
                form["phone"],
                form["fname"],
                form["initial"],
                form["lname"],
                form["healthcare_no"],
                form["hcn_expiry"],
                form["hcn_province"],
                form["dob"]
            )    
        )
        con.commit()

        con.close()
