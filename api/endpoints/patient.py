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


class PatientForms(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("form_type", type=str, required=True, choices=("report", "new_applicant_form", "medical_history", "covid_screen"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("new_form", type=int)
    parser.add_argument("report_id", type=int, required=False)
    parser.add_argument("applicant_form", type=str, required=False)
    parser.add_argument("history_id", type=int, required=False)
    parser.add_argument("screen_date", type=str, required=False)
    parser.add_argument("form", type=dict)

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
            "SELECT Hx_ID FROM Medical_History WHERE P_SSN = ?;", (current["ssn"],))
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

        args = self.parser.parse_args()

        if (args["action_type"] == "submit_form"):
            if (args["form_type"] == "report"):
                if args["new_form"]:
                    self.create_report(current["ssn"], args["form"])
                else:
                    self.update_report(current["ssn"], args["report_id"], args["form"])

            elif (args["form_type"] == "new_applicant_form"):
                self.update_new_applicant_form(current["ssn"], args["form"])

            elif (args["form_type"] == "medical_history"):
                pass

            else:
                pass

            return jsonify(
                successful=1
            )

        else:
            if (args["form_type"] == "report"):
                form = self.get_report(current["ssn"], args["report_id"])

            elif (args["form_type"] == "new_applicant_form"):
                form = self.get_new_applicant_form(
                    current["ssn"], args["applicant_form"])

            elif (args["form_type"] == "medical_history"):
                pass

            else:
                pass

            return jsonify(
                logged_in=1,
                form=form
            )

    def create_report(self, ssn, form):
        """Creates a new report to be added to the database.
        Picks a random doctor from the selected location.
        """

        con, cursor = db.connect_db()

        # Select a doctor from the medial centre.
        cursor.execute(
            "SELECT d.SSN as SSN FROM Doctor d, Works_At w, Medical_Centre m WHERE d.SSN = w.SSN AND w.Loc_Name = ? ORDER BY RANDOM() LIMIT 1;", (form["medical_centre"],))
        doctor = cursor.fetchone()

        # Get largest primary key.
        cursor.execute(
            "SELECT Report_ID FROM Report WHERE P_SSN = ? ORDER BY Report_ID DESC LIMIT 1;", (ssn,))
        report_id = cursor.fetchone()
        if not report_id:
            new_id = 0
        else:
            new_id = report_id["Report_ID"] + 1

        # Add report to the database.
        cursor.execute("INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (?, ?, ?, ?);",
                       (new_id, ssn, doctor["SSN"], form["Complaint"]))
        con.commit()
        con.close()

    def get_report(self, ssn, id):

        con, cursor = db.connect_db()

        # Get form.
        cursor.execute(
            "SELECT Complaint FROM Report WHERE Report_ID = ? AND P_SSN = ?;",
            (id, ssn)
        )
        result = cursor.fetchone()

        # Get doctor's name.
        cursor.execute(
            "SELECT d.Fname, d.Initial, d.Lname FROM Doctor d, Report r WHERE r.Report_ID = ? AND r.P_SSN = ? AND r.SSN = d.SSN;",
            (id, ssn)
        )
        doctor = cursor.fetchone()

        con.close()

        return {**dict(result), **dict(doctor)}

    def update_report(self, ssn, id, form):
         
        con, cursor = db.connect_db()

        cursor.execute("UPDATE Report SET Complaint = ? WHERE Report_ID = ? AND P_SSN = ?;", (form["Complaint"], id, ssn))

        con.commit()
        con.close()

    def get_new_applicant_form(self, ssn, email):

        con, cursor = db.connect_db()

        cursor.execute(
            "SELECT * FROM New_Applicant_Form WHERE P_SSN = ? AND Email = ?;", (ssn, email))
        result = cursor.fetchone()

        con.close()

        return dict(result)

    def update_new_applicant_form(self, ssn, form):

        con, cursor = db.connect_db()

        cursor.execute("INSERT OR REPLACE INTO New_Applicant_Form VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (
                           ssn,
                           form["email"],
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
