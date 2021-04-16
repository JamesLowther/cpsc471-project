from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json


class Doctor(Resource):
    def get(self):
        """Handle get request for doctor endpoint.
        """

        # Returns doctor information for logged in user.
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
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form", "update_complaint", "remove_illness", "add_illness", "remove_medication", "add_medication", "remove_medCenter", "add_medCenter"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("thePatientName", type=str)
    parser.add_argument("p_ssn", type=int)
    parser.add_argument("id", type=int)
    parser.add_argument("form", type=dict)
    parser.add_argument("illness_to_remove", type=str)
    parser.add_argument("illness_to_add", type=str)
    parser.add_argument("medication_to_remove", type=str)
    parser.add_argument("medication_to_add", type=str)
    parser.add_argument("medCenter_to_remove", type=str)
    parser.add_argument("medCenter_to_add", type=str)
    parser.add_argument("complaint", type=str)

    def get(self):
        """Handle get request for doctor/forms endpoint.
        """

        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

        # Get all reports.
        cursor.execute(
            "SELECT * FROM New_Applicant_Form AS a LEFT OUTER JOIN  Report AS r ON r.P_SSN = a.P_SSN WHERE r.Report_ID NOT NULL ORDER BY Fname ASC, Report_ID DESC LIMIT 10;")
        patients = cursor.fetchall()

        con.close()

        return jsonify(
            logged_in=1,
            patients=[dict(x) for x in patients]
        )

    def post(self):
        """Handle post request for doctor/forms endpoint.
        """

        args = self.parser.parse_args()

        if args["thePatientName"] is not None:
            if(args["p_ssn"] == -1):

                con, cursor = db.connect_db()

                # Get form.
                cursor.execute(
                    "SELECT * FROM New_Applicant_Form AS a LEFT OUTER JOIN  Report AS r ON r.P_SSN = a.P_SSN WHERE r.Report_ID NOT NULL AND Fname ||' '|| Lname  LIKE ? ORDER BY Fname ASC, Report_ID DESC LIMIT 10;", (
                        "%" + args["thePatientName"] + "%",)
                )
                patients = cursor.fetchall()

                con.close()

                return jsonify(
                    logged_in=1,
                    patients=[dict(x) for x in patients]
                )

        elif (args["p_ssn"] != -1):
            # If the doctor wants to save changes to the complaint form.
            if (args["action_type"] == "update_complaint"):
                self.update_complaint(
                    args["p_ssn"], args["id"], args["complaint"])

                return jsonify(
                    logged_in=1,
                )

            elif (args["action_type"] == "get_form"):
                if (args["form_type"] == "report"):

                    form = self.get_report(args["p_ssn"], args["id"])

                    return jsonify(
                        logged_in=1,
                        p_ssn=args["p_ssn"],
                        form=form,
                    )

            # If the doctor is requesting to remove a Diagnosised Illness from the patients report.
            elif (args["action_type"] == "remove_illness"):

                self.remove_diagnosis(
                    args["p_ssn"], args["id"], args["illness_to_remove"])

                return jsonify(
                    logged_in=1,
                    p_ssn=args["p_ssn"],
                )

            # If the doctor is requesting to add a Diagnosised Illness from the patients report.
            elif (args["action_type"] == "add_illness"):

                self.add_diagnosis(
                    args["p_ssn"], args["id"], args["illness_to_add"])

                return jsonify(
                    logged_in=1,
                    p_ssn=args["p_ssn"],
                )

            # If the doctor is requesting to remove a Medication from the patients report.
            elif (args["action_type"] == "remove_medication"):

                self.remove_medication(
                    args["p_ssn"], args["id"], args["medication_to_remove"])

                return jsonify(
                    logged_in=1,
                    p_ssn=args["p_ssn"],
                )

            # If the doctor is requesting to add a Medication from the patients report.
            elif (args["action_type"] == "add_medication"):

                self.add_medication(
                    args["p_ssn"], args["id"], args["medication_to_add"])

                return jsonify(
                    logged_in=1,
                    p_ssn=args["p_ssn"],
                )
            # If the doctor is requesting to remove a Medical Center from the patients report.
            elif (args["action_type"] == "remove_medCenter"):

                self.remove_medCenter(
                    args["p_ssn"], args["id"], args["medCenter_to_remove"])

                return jsonify(
                    logged_in=1,
                    p_ssn=args["p_ssn"],
                )

            # If the doctor is requesting to add a Medical Center from the patients report.
            elif (args["action_type"] == "add_medCenter"):

                self.add_medCenter(
                    args["p_ssn"], args["id"], args["medCenter_to_add"])

                return jsonify(
                    logged_in=1,
                    p_ssn=args["p_ssn"],
                )

    def update_complaint(self, ssn, id, complaint):
        """Update the compaint for a patient's report.
        """

        con, cursor = db.connect_db()

        # Update the patients complaint for the report
        cursor.execute(
            "UPDATE Report SET Complaint = ? WHERE P_SSN = ? AND Report_ID = ?;", (complaint, ssn, id,),)
        con.commit()
        con.close()

    def add_diagnosis(self, ssn, id, illness):
        """Add a diagnosis to a report.
        """

        con, cursor = db.connect_db()

        # Add a diagnosed illness.
        cursor.execute(
            "INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES (?,?,?);", (illness, id, ssn,),)

        con.commit()
        con.close()

    def remove_diagnosis(self, ssn, id, illness):
        """Remove a diagnosis from a report.
        """

        con, cursor = db.connect_db()

        # Remove a diagnosed illness from patients report.
        cursor.execute(
            "DELETE FROM Diagnoses WHERE P_SSN = ? AND Report_ID = ? AND Illness_name = ?;", (ssn, id, illness,),)

        con.commit()
        con.close()

    def add_medication(self, ssn, id, medication):
        """Add a medication for to a report.
        """

        con, cursor = db.connect_db()

        # Add a medication to patients report.
        cursor.execute(
            "INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES (?,?,?);", (medication, id, ssn,),)

        con.commit()
        con.close()

    def remove_medication(self, ssn, id, medication):
        """Remove a medication from a report.
        """

        con, cursor = db.connect_db()

        # Remove a medication that was prescribed on patients report.
        cursor.execute(
            "DELETE FROM Prescribes WHERE P_SSN = ? AND Report_ID = ? AND Med_Name = ?;", (ssn, id, medication,),)

        con.commit()
        con.close()

    def add_medCenter(self, ssn, id, medCenter):
        """Add a medical centre to a report.
        """

        con, cursor = db.connect_db()

        # Add a medcenter to patients report.
        cursor.execute(
            "INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (?,?,?);", (id, ssn, medCenter,),)

        con.commit()
        con.close()

    def remove_medCenter(self, ssn, id, medCenter):
        """Remove a medical centr from a report.
        """

        con, cursor = db.connect_db()

        # Remove a medcenter from patients report.
        cursor.execute(
            "DELETE FROM Assigned WHERE P_SSN = ? AND Report_ID = ? AND MedCenter_Name = ?;", (ssn, id, medCenter,),)

        con.commit()
        con.close()

    def get_report(self, ssn, id):
        """Get the data from a patient's report.
        """

        con, cursor = db.connect_db()

        # Get patient name.
        cursor.execute(
            "SELECT a.Fname, a.Initial, a.Lname, a.Gender, a.Sex, CAST(STRFTIME('%Y.%m%d', 'now') - STRFTIME('%Y.%m%d', a.DoB) AS INT) AS Age FROM New_Applicant_Form AS a WHERE P_SSN = ?;", (ssn,),
        )
        patient = cursor.fetchone()

        # Get the complaint from patients report.
        cursor.execute(
            "SELECT Complaint FROM Report WHERE Report_ID = ? AND P_SSN = ?;",
            (id, ssn)
        )
        complaint = cursor.fetchone()

        # Get name of the doctor assigned to the patients report.
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

        # Add the side effects to the medications.
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

        # RETRIEVE ALL MEDICAL HISORY INFORMTATION *If it exists
        # -----------------------------------------

        # Check if patient has a medical history filled out

        # Initialize dict() variables in case the if statement can't.
        TPAL = {}
        past_illnesses = {}
        allergies = {}
        immunizations = {}

        # To check is theres a medical history tuple.
        has_row = 0
        cursor.execute(
            "SELECT * FROM Medical_History WHERE P_SSN = ?;", (ssn,))
        # has_row will be true if a medical history tuple exists for the patient
        has_row = cursor.fetchone()

        # If history exists:
        # retrieve TPAL (Pregnancy) info
        if has_row:
            # Retrieve TPAL info.
            cursor.execute(
                "SELECT TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living FROM Medical_History WHERE P_SSN = ?;",
                (ssn,)
            )
            TPAL = cursor.fetchone()

            # Retrieve Past_Illnesses.
            cursor.execute(
                "SELECT Illness_name, Age_of_onset FROM Past_Illnesses WHERE P_SSN = ?;",
                (ssn,)
            )
            past_illnesses = cursor.fetchall()
            past_illnesses = [dict(x) for x in past_illnesses]

            # Retrieve Allergies.
            cursor.execute(
                "SELECT Allergy FROM Allergies WHERE P_SSN = ?;",
                (ssn,)
            )
            allergies = cursor.fetchall()
            allergies = [dict(x) for x in allergies]

            # Retrieve Immunizations.
            cursor.execute(
                "SELECT Immunization FROM Immunization WHERE P_SSN = ?;",
                (ssn,)
            )
            immunizations = cursor.fetchall()
            immunizations = [dict(x) for x in immunizations]

        # Retrieve if they've passed their covid screen.
        cursor.execute(
            "SELECT Has_passed, MAX(Date) FROM Covid_Screen WHERE P_SSN = ?;",
            (ssn,)
        )
        covid_screen = cursor.fetchone()

        con.close()

        return {
            **dict(patient),
            **dict(complaint),
            **dict(doctor),
            **dict(illnesses),
            "Diagnosis": list(illnesses),
            "Medications": list(medications),
            "Medical_centres": list(medical_centres),
            **dict(TPAL),
            "past_illnesses": list(past_illnesses),
            "allergies": list(allergies),
            "immunizations": list(immunizations),
            **dict(covid_screen),
        }
