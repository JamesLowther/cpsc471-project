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
    """
    parser = reqparse.RequestParser()
    parser.add_argument("form_type", type=str, required=True, choices=("new_application_form","covid_screen"),
                       help="Bad choice: {error_msg}")
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form"),
                       help="Bad choice: {error_msg}")
    parser.add_argument("P_SSN", type=int, required=False)


    def get(self):
        """
        A GET request returns all Patient's SSN's and the keys of their existing forms.
        """

        # Verify the request is sent from logged in user
        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

       
        # Get Patients and keys of all their forms. Null if no report of that kind exists
        cursor.execute(
            "SELECT p.P_SSN, n.Fname, n.Lname, n.Email, n.Is_approved \
            FROM Patient as p \
            LEFT JOIN New_Applicant_Form as n ON p.P_SSN=n.P_SSN;")
        forms = cursor.fetchall()
        forms = [dict(f) for f in forms]

        # Get all covid screens of each patient
        for form in forms:
            cursor.execute("SELECT Date FROM Covid_screen WHERE P_SSN = ?;", (form["P_SSN"],))
            screens = cursor.fetchall()

            form["dates"] = [f["Date"] for f in screens]


        con.close()

        return jsonify (
            logged_in = 1,
            forms = [dict(f) for f in forms] )


    def post(self):
        """
        A POST request takes parameters to decide on the action type
        and perform the specified action, using the given data.
        """
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = self.parser.parse_args()

        if(args["action_type"] == "submit_form"):
            if(args["form_type"]== "new_application_form"):
                self.approve_applicant(args["P_SSN"])



    def approve_applicant(self,ssn):
        # Set a new_applicant_form specified by ssn, to approved

        con, cursor = db.connect_db()

        # update the form corresponding to the patients ssn to 'approved' (1)
        cursor.execute("UPDATE New_Applicant_Form SET Is_approved = ? WHERE P_SSN = ?;", (1,ssn))

        con.commit()
        con.close()