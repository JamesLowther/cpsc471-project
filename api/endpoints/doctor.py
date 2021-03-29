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
    parser.add_argument("form_type", type=str, required=True, choices=("patient_search", "medical_history", "report"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form", "remove_illness", "add_illness", "remove_medication", "add_medication"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("thePatientName", type=str)
    parser.add_argument("p_ssn", type=int)
    parser.add_argument("id", type=int)
    parser.add_argument("form", type=dict)
    parser.add_argument("illness_to_remove", type=str)
    parser.add_argument("illness_to_add", type=str)
    parser.add_argument("medication_to_remove", type=str)
    parser.add_argument("medication_to_add", type=str)


    def get(self):
        
        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

        # Get all reports.
        cursor.execute(
            "SELECT * FROM New_Applicant_Form AS a LEFT OUTER JOIN  Report AS r ON r.P_SSN = a.P_SSN WHERE r.Report_ID NOT NULL ORDER BY Fname DESC LIMIT 10;")
        patients = cursor.fetchall()

        con.close()

        return jsonify(
            logged_in=1,
            patients=[dict(x) for x in patients]
        )


    def post(self):
        
        args = self.parser.parse_args()
        
        if args["thePatientName"] is not None:
            if(args["p_ssn"] == -1):

                con, cursor = db.connect_db()

                # Get form.
                cursor.execute(
                    "SELECT * FROM New_Applicant_Form AS a LEFT OUTER JOIN  Report AS r ON r.P_SSN = a.P_SSN WHERE r.Report_ID NOT NULL AND Fname ||' '|| Lname  LIKE ? ORDER BY Fname DESC LIMIT 10;", ("%" + args["thePatientName"] + "%",)
                )
                patients = cursor.fetchall()

                con.close()

                return jsonify(
                    logged_in=1,
                    patients=[dict(x) for x in patients]
                )

        elif (args["p_ssn"] != -1):
            if (args["action_type"] == "get_form"):
                if (args["form_type"] == "report"): 

                    form = self.get_report(args["p_ssn"], args["id"])

                    return jsonify(
                        logged_in=1,
                        p_ssn=args["p_ssn"],
                        form=form,
                    )

            #If the doctor is requesting to remove a Diagnosised Illness from the patients report
            elif (args["action_type"] == "remove_illness"):

                    #first remove the diagnosis from the database
                    self.remove_diagnosis(args["p_ssn"], args["id"], args["illness_to_remove"])
                    #then return updated report information
                    # form = self.get_report(args["p_ssn"], args["id"])

                    return jsonify(
                        logged_in=1,
                        p_ssn=args["p_ssn"],
                    )

            #If the doctor is requesting to add a Diagnosised Illness from the patients report
            elif (args["action_type"] == "add_illness"):

                    #first remove the diagnosis from the database
                    self.add_diagnosis(args["p_ssn"], args["id"], args["illness_to_add"])
                    #then return updated report information
                    # form = self.get_report(args["p_ssn"], args["id"])

                    return jsonify(
                        logged_in=1,
                        p_ssn=args["p_ssn"],
                    )
            #If the doctor is requesting to remove a Medication from the patients report
            elif (args["action_type"] == "remove_medication"):

                    #first remove the diagnosis from the database
                    self.remove_medication(args["p_ssn"], args["id"], args["medication_to_remove"])
                    #then return updated report information
                    # form = self.get_report(args["p_ssn"], args["id"])

                    return jsonify(
                        logged_in=1,
                        p_ssn=args["p_ssn"],
                    )

            #If the doctor is requesting to add a Medication from the patients report
            elif (args["action_type"] == "add_medication"):

                    #first remove the diagnosis from the database
                    self.add_medication(args["p_ssn"], args["id"], args["medication_to_add"])
                    #then return updated report information
                    # form = self.get_report(args["p_ssn"], args["id"])

                    return jsonify(
                        logged_in=1,
                        p_ssn=args["p_ssn"],
                    )

    def add_diagnosis(self, ssn, id, illness):

        con, cursor = db.connect_db()

        # Add a diagnosed illness.
        cursor.execute("INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES (?,?,?);", (illness, id, ssn,),)

        con.commit()
        con.close()


    def remove_diagnosis(self, ssn, id, illness):

        con, cursor = db.connect_db()

        # Remove a diagnosed illness.
        cursor.execute("DELETE FROM Diagnoses WHERE P_SSN = ? AND Report_ID = ? AND Illness_name = ?;", (ssn, id, illness,),)

        con.commit()
        con.close()

    def add_medication(self, ssn, id, medication):

        con, cursor = db.connect_db()

        # Add a diagnosed illness.
        cursor.execute("INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES (?,?,?);", (medication, id, ssn,),)

        con.commit()
        con.close()


    def remove_medication(self, ssn, id, medication):

        con, cursor = db.connect_db()

        # Remove a diagnosed illness.
        cursor.execute("DELETE FROM Prescribes WHERE P_SSN = ? AND Report_ID = ? AND Med_Name = ?;", (ssn, id, medication,),)

        con.commit()
        con.close()

    def update_patient_report(self, p_ssn, form):
        con, cursor = db.connect_db()

        # Update diagnosed illnesses.
        cursor.execute("DELETE FROM Past_Illnesses WHERE P_SSN = ?;", (ssn,))
        for illness in form["Past_illnesses"]:
            cursor.execute("INSERT INTO Past_Illnesses VALUES (?, ?, ?);", (ssn, illness["Illness_name"], illness["Age_of_onset"]))

        con.commit()
        con.close()


    def get_report(self, ssn, id):

        con, cursor = db.connect_db()

        #Get patient name.
        cursor.execute(
            "SELECT a.Fname, a.Initial, a.Lname FROM New_Applicant_Form AS a WHERE P_SSN = ?;", (ssn,),
        )
        patient = cursor.fetchone()

        # Get form.
        cursor.execute(
            "SELECT Complaint FROM Report WHERE Report_ID = ? AND P_SSN = ?;",
            (id, ssn)
        )
        complaint = cursor.fetchone()

        # Get doctor's name.
        cursor.execute(
            "SELECT d.Fname AS Doc_Fname, d.Initial AS Doc_Initial, d.Lname AS Doc_Lname FROM Doctor d, Report r WHERE r.Report_ID = ? AND r.P_SSN = ? AND r.SSN = d.SSN;",
            (id, ssn)
        )
        doctor = cursor.fetchone()

        # Get diagnosed illnesses.
        cursor.execute(
            "SELECT i.Name, i.Organ_system FROM Illness i, Diagnoses d WHERE d.Illness_name = i.Name AND d.Report_ID = ? AND d.P_SSN = ?;",
            (id, ssn)
        )
        illnesses = cursor.fetchall()
        illnesses = [dict(x) for x in illnesses]

        # Get assigned medications.
        cursor.execute(
            "SELECT m.Name, m.Is_prescription FROM Medication m, Prescribes p WHERE m.Name = p.Med_Name AND p.Report_ID = ? AND p.P_SSN = ?;",
            (id, ssn)
        )
        medications = cursor.fetchall()
        medications = [dict(x) for x in medications]

        # Get side-effects
        cursor.execute(
            "SELECT m.Name, s.Effect FROM Medication m, Prescribes p, Side_Effects s WHERE s.Med_Name = m.Name AND m.Name = p.Med_Name AND p.Report_ID = ? AND p.P_SSN = ?;",
            (id, ssn)
        )
        side_effects = cursor.fetchall()
        side_effects = [dict(x) for x in side_effects]

        # Add the effects to the medications.
        for medication in medications:
            medication["Effects"] = []
            for side_effect in side_effects:
                if medication["Name"] == side_effect["Name"]:
                    medication["Effects"].append(side_effect["Effect"])

        # Get assigned medical centres.
        cursor.execute(
            "SELECT m.Name, m.Address, m.type FROM Medical_Centre m, Assigned a WHERE m.Name = a.MedCenter_Name AND a.Report_ID = ? AND a.P_SSN = ?;",
            (id, ssn)
        )
        medical_centres = cursor.fetchall()
        medical_centres = [dict(x) for x in medical_centres]

        con.close()

        return {
            **dict(patient),
            **dict(complaint),
            **dict(doctor),
            **dict(illnesses),
            "Diagnosis": list(illnesses),
            "Medications": list(medications),
            "Medical_centres": list(medical_centres)}