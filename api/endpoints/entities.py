from flask import jsonify
from flask_restful import Resource, reqparse
import sqlite3

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json


class EntitiesForms(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("entity_type", type=str, required=True, choices={"medication", "illness", "symptom"}, help="Bad choice: {error_msg}")
    parser.add_argument("method", type=str, required=True, choices={"add", "update", "delete", "query"}, help="Bad choice: {error_msg}")
    

    parser.add_argument("entity_name", type=str, required=False)
    #Medication attributes
    parser.add_argument("is_pres", type=int, required=False)
    #illness attributes
    parser.add_argument("org_sys", type=str, required=False)
    
    # either side-effects or symptoms for newly added med or illness
    parser.add_argument("effects", action='append', type=str, required=False)
    
    parser.add_argument("form", type=dict, required=False)
    parser.add_argument("query_string", type=str)


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

        # Only doctors and clerks can access add/delete functions.
        elif current["user_type"] in {"doctor", "clerk"}:
            if args["method"] == "add":
                return self.add_new_entity(args)

            elif args["method"] == "update":
                # update illness/medication.
                return self.update_entity(args)

            elif args["method"] == "delete":
                # delete illness/medication.
                return self.delete_entity(args)

        return jsonify(
            logged_in=1,
            results=[dict(x) for x in results]
        )

    def query(self, args):
        limit = 8

        results = {}

        # This to to prevent returning all results (issue when lots of data).
        if not args["query_string"]:
            return {}

        con, cursor = db.connect_db()

        entity_type = args["entity_type"]

        if (entity_type == "medication"):
            # Select all medications that match the query string.
            cursor.execute("SELECT Name, Is_prescription FROM Medication WHERE Name LIKE ? ORDER BY Name LIMIT ?;", ("%" + args["query_string"] + "%", limit))
            results = cursor.fetchall()
            results = [dict(x) for x in results]
            
            # Add side effects as a list to the with the key "Effects".
            # We have to build this list manually afaik.
            for medication in results:
                cursor.execute("SELECT s.Effect FROM Side_Effects AS s WHERE s.Med_Name = ? LIMIT ?;", (medication["Name"], limit))
                side_effects = cursor.fetchall()

                medication["Effects"] = [x["Effect"] for x in side_effects]
            
        elif (entity_type == "illness"):
            cursor.execute("SELECT Name, Organ_system FROM Illness WHERE Name LIKE ? ORDER BY Name LIMIT ?;", ("%" + args["query_string"] + "%", limit))
            results = cursor.fetchall()
            results = [dict(x) for x in results]

            for illness in results:
                cursor.execute("SELECT s.Symptom_name FROM Symptoms AS s WHERE s.Illness_Name = ? LIMIT ?;", (illness["Name"], limit))
                symptoms = cursor.fetchall()

                illness["Effects"] = [x["Symptom_name"] for x in symptoms]

        elif (entity_type == "symptom"):
            cursor.execute("SELECT DISTINCT Symptom_name FROM Symptoms WHERE Symptom_name LIKE ? ORDER BY Symptom_name LIMIT ?;", ("%" + args["query_string"] + "%", limit))
            results = cursor.fetchall()
            results = [dict(x) for x in results]

            for symptom in results:
                cursor.execute("SELECT s.Illness_name FROM Symptoms AS s WHERE s.Symptom_name = ? LIMIT ?;", (symptom["Symptom_name"], limit))
                illnesses = cursor.fetchall()

                symptom["Effects"] = [x["Illness_name"] for x in illnesses]

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
                cursor.execute("INSERT INTO Medication VALUES (?, ?);", (args["entity_name"], args["is_pres"]) )

                # if users included side-effects, insert into database
                if(args["effects"]):
                    for effect in args["effects"]:
                        cursor.execute("INSERT INTO Side_Effects VALUES (?,?);", (args["entity_name"], effect) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    sys_msg="Error: Could not Add. Entity may already exist.",
                    )
        
        # Add a new illness, and its specified symptoms. Catch any SQL errors
        elif (args["entity_type"] == "illness"):
            try:
                cursor.execute("INSERT INTO Illness VALUES (?, ?);", (args["entity_name"], args["org_sys"],),)

                # if users included symptoms, insert into database
                if(args["effects"]):
                    for symptom in args["effects"]:
                        cursor.execute("INSERT INTO Symptoms VALUES (?,?);", (args["entity_name"], symptom) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    sys_msg="Error: Could not Add. Entity may already exist.",
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
                cursor.execute("UPDATE Medication SET Is_prescription = ? WHERE Name = ?;", (args["is_pres"], args["entity_name"]))

                # if users included side-effects, insert into database
                # delete the all side-effects first, then insert to avoid distinguishing between new and existing tuples
                cursor.execute("DELETE FROM Side_Effects WHERE Med_Name = (?);", (args["entity_name"],),)
                if(args["effects"]):
                    for effect in args["effects"]:
                        cursor.execute("INSERT INTO Side_Effects VALUES (?,?);", (args["entity_name"], effect) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    sys_msg="Error: Could not update",
                    )
        
        # Update an existing illness, and its specified symptoms. Catch any SQL errors
        elif (args["entity_type"] == "illness"):
            try:
                cursor.execute("UPDATE Illness SET Organ_system = ? WHERE Name = ?;",(args["org_sys"], args["entity_name"]))

                # if users included symptoms, insert into database
                cursor.execute("DELETE FROM Symptoms WHERE Illness_name = (?);", (args["entity_name"],),)
                if(args["effects"]):
                    for symptom in args["effects"]:
                        cursor.execute("INSERT INTO Symptoms VALUES (?,?);", (args["entity_name"], symptom) )

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    sys_msg="Error: Could not update",
                    )


        con.commit()
        con.close()

        return jsonify(
            status=1,
            sys_msg="Successfully Updated",
            )

    def delete_entity(self, args):
        """
        Update an existing entity in the database and its corresponding
        effects or symptoms.
        """

        con, cursor = db.connect_db()

        # Update an existing medication, and its specified side-effects
        # catch any SQL errors eg key or unique name constraints
        if(args["entity_type"] == "medication"):
            try:
                # Delete from Medication table and all side effects
                cursor.execute("DELETE FROM Medication WHERE Name = ?;", (args["entity_name"],),)
                cursor.execute("DELETE FROM Side_Effects WHERE Med_Name = ?;", (args["entity_name"],))

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    sys_msg="Error: Could not delete",
                    )
        
        # Update an existing illness, and its specified symptoms. Catch any SQL errors
        elif (args["entity_type"] == "illness"):
            try:
                # Delete illness and all Symptoms
                cursor.execute("DELETE FROM Illness WHERE Name = ?;", (args["entity_name"],),)
                cursor.execute("DELETE FROM Symptoms WHERE Illness_Name = ?;", (args["entity_name"],))

            except sqlite3.Error as er:
                print(er)
                con.close()
                return jsonify(
                    status=0,
                    sys_msg="Error: Could not delete",
                    )


        con.commit()
        con.close()

        return jsonify(
            status=1,
            sys_msg="Successfully Deleted",
            )