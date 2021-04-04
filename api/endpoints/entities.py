from flask import jsonify
from flask_restful import Resource, reqparse
import sqlite3

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
    parser.add_argument("entity_type", type=str, required=True, choices={"medication", "illness"}, help="Bad choice: {error_msg}")
    parser.add_argument("method", type=str, required=True, choices={"add", "update", "delete", "query"}, help="Bad choice: {error_msg}")
    
    parser.add_argument("med_name", type=str, required=False)
    parser.add_argument("is_pres", type=int, required=False)
    
    parser.add_argument("ill_name", type=str, required=False)
    parser.add_argument("org_sys", type=str, required=False)
    
    # either side-effects or symptoms for newly added med or illness
    parser.add_argument("effects", action='append', type=str, required=False)
    
    parser.add_argument("form", type=dict, required=False)
    parser.add_argument("query_string", type=str)

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

        results = {}

        if args["method"] == "query":
            results = self.query(args)

        # Only doctors and clerks can accses add/delete functions.
        elif current["user_type"] in {"doctor", "clerk"}:
            if args["method"] == "add":
                return self.add_new_entity(args)

            elif args["method"] == "update":
                # Write code to delete illness/medication.
                return self.update_entity(args)

            elif args["method"] == "delete":
                # Write code to delete illness/medication.
                pass

        return jsonify(
            logged_in=1,
            results=[dict(x) for x in results]
        )

    def query(self, args):
        results = {}

        # This to to prevent returning all results (issue when lots of data).
        if args["query_string"] == "":
            return {}

        con, cursor = db.connect_db()

        entity_type = args["entity_type"]

        if (entity_type == "medication"):
            # Select all medications that match the query string.
            cursor.execute("SELECT Name, Is_prescription FROM Medication WHERE Name LIKE ? ORDER BY Name;", ("%" + args["query_string"] + "%",))
            results = cursor.fetchall()
            results = [dict(x) for x in results]
            
            # Add side effects as a list to the with the key "Effects".
            # We have to build this list manually afaik.
            for medication in results:
                cursor.execute("SELECT s.Effect FROM Side_Effects AS s WHERE s.Med_Name = ?;", (medication["Name"],))
                side_effects = cursor.fetchall()

                medication["Effects"] = [x["Effect"] for x in side_effects]
            
        elif (entity_type == "illness"):
            cursor.execute("SELECT Name, Organ_system FROM Illness WHERE Name LIKE ? ORDER BY Name;", ("%" + args["query_string"] + "%",))
            results = cursor.fetchall()
            results = [dict(x) for x in results]

            for illness in results:
                cursor.execute("SELECT s.Symptom_name FROM Symptoms AS s WHERE s.Illness_Name = ?;", (illness["Name"],))
                symptoms = cursor.fetchall()

                illness["Effects"] = [x["Symptom_name"] for x in symptoms]

        con.close()

        return results




    def add_new_entity(self, args):
        """
        Add a new entity to the database and its corresponding
        effects or symptoms.
        """

        con, cursor = db.connect_db()

        # Add a new medication, and its specified side-effects
        # catch any SQL errors eg key or unique name constraints
        if(args["entity_type"] == "medication"):
            try:
                cursor.execute("INSERT INTO Medication VALUES (?, ?);", (args["med_name"], args["is_pres"]) )

                # if users included side-effects, insert into database
                if(args["effects"]):
                    for effect in args["effects"]:
                        cursor.execute("INSERT INTO Side_Effects VALUES (?,?);", (args["med_name"], effect) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    error_msg=er,
                    sys_msg="Error: Could not Add",
                    )
        
        # Add a new illness, and its specified symptoms. Catch any SQL errors
        elif (args["entity_type"] == "illness"):
            try:
                #cursor.execute("DELETE FROM Illness WHERE  (?);", (args["ill_name"],),)
                cursor.execute("INSERT INTO Illness VALUES (?, ?);", (args["ill_name"], args["org_sys"],),)

                # if users included symptoms, insert into database
                if(args["effects"]):
                    for symptom in args["effects"]:
                        cursor.execute("INSERT INTO Symptoms VALUES (?,?);", (args["ill_name"], symptom) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    error_msg=er,
                    sys_msg="Error: Could not Add",
                    )

        con.commit()
        con.close()

        return jsonify(
            status=1,
            sys_msg="Successfully Added",
            )


    def update_entity(self, args):
        """
        Update an existing entity in the database and its corresponding
        effects or symptoms.
        """

        con, cursor = db.connect_db()

        # Update an existing medication, and its specified side-effects
        # catch any SQL errors eg key or unique name constraints
        if(args["entity_type"] == "medication"):
            try:
                cursor.execute("DELETE FROM Medication WHERE Name = ?;", (args["med_name"],),)
                cursor.execute("INSERT INTO Medication VALUES (?, ?);", (args["med_name"], args["is_pres"]) )

                # if users included side-effects, insert into database
                cursor.execute("DELETE FROM Side_Effects WHERE Med_Name = (?);", (args["med_name"],),)
                if(args["effects"]):
                    for effect in args["effects"]:
                        cursor.execute("INSERT INTO Side_Effects VALUES (?,?);", (args["med_name"], effect) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    error_msg=er,
                    sys_msg="Error: Could not update",
                    )
        
        # Update an existing illness, and its specified symptoms. Catch any SQL errors
        elif (args["entity_type"] == "illness"):
            try:
                cursor.execute("DELETE FROM Illness WHERE Name = ?;", (args["ill_name"],),)
                cursor.execute("INSERT INTO Illness VALUES (?, ?);", (args["ill_name"], args["org_sys"],),)

                # if users included symptoms, insert into database
                cursor.execute("DELETE FROM Symptoms WHERE Illness_name = (?);", (args["ill_name"],),)
                if(args["effects"]):
                    for symptom in args["effects"]:
                        cursor.execute("INSERT INTO Symptoms VALUES (?,?);", (args["ill_name"], symptom) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    error_msg=er,
                    sys_msg="Error: Could not update",
                    )


        con.commit()
        con.close()

        return jsonify(
            status=1,
            sys_msg="Successfully Updated",
            )