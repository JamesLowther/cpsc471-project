from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json


class Keys(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("entity", type=str, required=True,
                        choices={"medical_centre"})
    parser.add_argument("query_string", type=str)

    def post(self):
        """Returns the primary keys from certain tables in our database.
        This is needed for certain selectors on form pages on the front-end.
        """
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = self.parser.parse_args()

        con, cursor = db.connect_db()

        results = {}

        # Get all keys for medical centre table.
        if (args["entity"] == "medical_centre"):
            if (args["query_string"] is not None):
                if args["query_string"] == "":
                    con.close()
                    return jsonify(
                        result=[dict(x) for x in results],
                        logged_in=1,
                    )
                else:
                    cursor.execute("SELECT Name, Type, Address FROM Medical_Centre WHERE Name LIKE ?;", (
                        "%" + args["query_string"] + "%",),)
                    results = cursor.fetchall()
            else:
                cursor.execute("SELECT Name FROM Medical_Centre;")
                results = cursor.fetchall()

        con.close()

        return jsonify(
            result=[dict(x) for x in results],
            logged_in=1,
        )
