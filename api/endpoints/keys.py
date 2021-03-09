from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json

class Keys(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("entity", type=str, required=True, choices={"medical_centre"})

    def post(self):
        """Returns the primary keys from certain tables in our database.
        This is needed for certain selectors on form pages on the front-end.
        """
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = self.parser.parse_args()

        con, cursor = db.connect_db()

        results = {}

        if (args["entity"] == "medical_centre"):
            cursor.execute("SELECT Name FROM Medical_Centre;")
            results = cursor.fetchall()    

        return jsonify(result=[dict(x) for x in results])