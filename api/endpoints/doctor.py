from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json


class Doctor(Resource):
    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()
            if current["user_type"] == "doctor":
                return jsonify({**current, "logged_in": 1})
            else:
                return jsonify({**current, "logged_in": 0})



class DoctorForms(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("form_type", type=str, required=True, choices=("patient_search", "medical_history"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("thePatientName", type=str)

    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

        # Get all reports.
        cursor.execute(
            "SELECT * FROM New_Applicant_Form ORDER BY Fname DESC LIMIT 10;")
        patients = cursor.fetchall()

        con.close()

        return jsonify(
            logged_in=1,
            patients=[dict(x) for x in patients]
        )


    def post(self):

        args = self.parser.parse_args()

        con, cursor = db.connect_db()

        # Get form.
        cursor.execute(
            "SELECT * FROM New_Applicant_Form WHERE Fname ||' '|| Lname  LIKE ? ORDER BY Fname DESC LIMIT 10;", ("%" + args["thePatientName"] + "%",)
        )
        patients = cursor.fetchall()

        con.close()

        return jsonify(
            logged_in=1,
            patients=[dict(x) for x in patients]
        )