from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

import json

from database import db





class Clerk(Resource):
    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        return jsonify({**current, "logged_in": 1})


class ClerkForms(Resource):

    """
    Initialize arguments for a post request. Specifies the keys for the json object to be exchanged.
    Keys are for getting forms and submitting data. 
    Forms are either New_Applicant_Form or Covid_Screen.
    """
    parser = reqparse.RequestParser()
    parser.add_argument("form_type", type=str, required=True, choices=("new_applicant_form","covid_screen"),
                       help="Bad choice: {error_msg}")
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form"),
                       help="Bad choice: {error_msg}")
    parser.add_argument("new_form", type=int)
    parser.add_argument("applicant_form", type=str, required=False)
    parser.add_argument("screen_date", type=str, required=False)
    parser.add_argument("form", type=dict)


    def get(self):
        """
        A GET request returns all New_Applicant_Forms and Covid_Screens.
        """

        # Verify the request is sent from logged in user
        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

        # Get all new applicant forms.
        cursor.execute(
            "SELECT P_SSN FROM New_Applicant_Form")
        new_applicant = cursor.fetchall()

        # Get all covid screens.
        cursor.execute(
            "SELECT Date, P_SSN FROM Covid_Screen")
        covid_screens = cursor.fetchall()

        con.close()

        return jsonify (
            logged_in=1,
            covid_screens=[dict(s) for s in covid_screens],
            new_applicant=[dict(f) for f in new_applicant]
        )


    def post(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = self.parser.parse_args()

        con, cursor = db.connect_db()

        #get all existing patients who have not submitted an applicant form
        cursor.execute(
            "SELECT p.P_SSN FROM Patient as p WHERE NOT EXISTS (SELECT n.P_SSN FROM New_Applicant_Form as n WHERE n.P_SSN=p.P_SSN)")
        existing_ps = cursor.fetchall()

        return jsonify (
            logged_in=1,
            existingPatients = [dict(p) for p in existing_ps]
            )