from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json

class Entities(Resource):
    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()
            if current["user_type"] == "doctor" or current["user_type"] == "clerk":
                return jsonify({**current, "logged_in": 1, "user_type": current["user_type"]})
            else:
                return jsonify({**current, "logged_in": 0})

class EntitiesForms(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("entity_type", type=str, required=True, choices={"medication", "illness", "symptom"}, help="Bad choice: {error_msg}")
    parser.add_argument("method", type=str, required=True, choices={"add", "delete", "query"}, help="Bad choice: {error_msg}")
    parser.add_argument("med_name", type=int, required=False)
    parser.add_argument("ill_name", type=int, required=False)
    parser.add_argument("symp_name", type=str, required=False)
    parser.add_argument("form", type=dict, required=False)
    parser.add_argument("theMedicationName", type=str)

    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

        # Get all medications.
        cursor.execute("SELECT m.Name, s.Effect FROM Medication AS m LEFT OUTER JOIN Side_Effects AS s ON m.Name = s.Med_Name WHERE m.name LIKE ?;", ("%" + args["theMedicationName"] + "%",))
        medications = cursor.fetchall()

        con.close()

        return jsonify(
            logged_in=1,
            medications=[dict(x) for x in medications]
        )

    def post(self):
        """Returns the primary keys from certain tables in our database.
        This is needed for certain selectors on form pages on the front-end.
        """
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = self.parser.parse_args()

        con, cursor = db.connect_db()

        medications = {}

        if (args["entity_type"] == "medication"):
            cursor.execute("SELECT m.Name, s.Effect FROM Medication AS m LEFT OUTER JOIN Side_Effects AS s ON m.Name = s.Med_Name WHERE m.name LIKE ?;", ("%" + args["theMedicationName"] + "%",))
            medications = cursor.fetchall()
        elif (args["entity_type"] == "illness"):
            cursor.execute("SELECT Name FROM Illness;")
            results = cursor.fetchall()  
        elif (args["entity_type"] == "symptom"):
            cursor.execute("SELECT Symptom_name FROM Symptoms;")
            results = cursor.fetchall()    

        return jsonify(
            logged_in=1,
            medications=[dict(x) for x in medications]
        )
