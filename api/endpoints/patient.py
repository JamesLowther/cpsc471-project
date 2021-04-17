from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json
import datetime


class Patient(Resource):
    def get(self):
        """Handle get request to patient endpoint.
        """
        if verify_jwt_in_request():
            current = get_jwt_identity()

        # Return the current patient information.
        return jsonify({**current, "logged_in": 1})


class PatientForms(Resource):
    # Set expected body parameters.
    parser = reqparse.RequestParser()
    parser.add_argument("form_type", type=str, required=True, choices=("report", "new_applicant_form", "medical_history", "covid_screen"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("new_form", type=int)
    parser.add_argument("report_id", type=int, required=False)
    parser.add_argument("p_ssn", type=int, required=False)
    parser.add_argument("screen_date", type=str, required=False)
    parser.add_argument("form", type=dict)

    authorized_types = {"patient", "clerk"}

    def get(self):
        """Handle get request to patient/forms endpoint.
        Returns the keys for all of the patient's forms.
        """
        if verify_jwt_in_request():
            current = get_jwt_identity()

        # Check to make sure correct user is accessing api.
        if not (current["user_type"] in self.authorized_types):
            return "You don't have permission to use this endpoint."

        # Set the ssn depending on the accessing user.
        p_ssn = current["ssn"]

        con, cursor = db.connect_db()

        # Get all reports.
        cursor.execute(
            "SELECT Report_ID FROM Report WHERE P_SSN = ?;", (p_ssn,))
        reports = cursor.fetchall()

        # Get all new applicant forms.
        cursor.execute(
            "SELECT P_SSN, Email, Is_approved FROM New_Applicant_Form WHERE P_SSN = ?;", (p_ssn,))
        new_applicant = cursor.fetchall()

        # Get all covid screens.
        cursor.execute(
            "SELECT Date, Has_passed FROM Covid_Screen WHERE P_SSN = ?;", (p_ssn,))
        covid_screen = cursor.fetchall()

        # Get medical history forms.
        cursor.execute(
            "SELECT P_SSN FROM Medical_History WHERE P_SSN = ?;", (p_ssn,))
        medical_history = cursor.fetchall()

        con.close()

        # Return keys for all forms associated with the patient's account.
        return jsonify(
            logged_in=1,
            reports=[dict(x) for x in reports],
            new_applicant=[dict(x) for x in new_applicant],
            covid_screen=[dict(x) for x in covid_screen],
            medical_history=[dict(x) for x in medical_history]
        )

    def post(self):
        """Handle post request to the patient/forms endpoint.
        """
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = self.parser.parse_args()

        # Check to make sure correct user is accessing api.
        if not (current["user_type"] in self.authorized_types):
            return "You don't have permission to use this endpoint."

        # Set the ssn depending on the accessing user.
        p_ssn = current["ssn"]
        if current["user_type"] == "clerk":
            p_ssn = args["p_ssn"]

        # If submit form action type is requested.
        if (args["action_type"] == "submit_form"):
            try:
                # Handle logic for reports.
                if (args["form_type"] == "report"):
                    if args["new_form"]:
                        self.create_report(p_ssn, args["form"])
                    else:
                        self.update_report(
                            p_ssn, args["report_id"], args["form"])

                # Handle logic for new applicant forms.
                elif (args["form_type"] == "new_applicant_form"):
                    self.update_new_applicant_form(
                        p_ssn, args["form"], 1 if current["user_type"] == "clerk" else 0)

                # Handle logic for covid screens.
                elif (args["form_type"] == "covid_screen"):
                    if args["new_form"]:
                        self.create_covid_screen(p_ssn, args["form"])
                    else:
                        self.update_covid_screen(
                            p_ssn, args["screen_date"], args["form"])

                # Handle logic for medical history.
                elif (args["form_type"] == "medical_history"):
                    self.update_medical_history(p_ssn, args["form"])

            except Exception as e:
                print(e)
                return jsonify(
                    succsessful=0
                )

            return jsonify(
                successful=1
            )

        # Get form action type was requested.
        else:
            # Handle logic for getting report.
            if (args["form_type"] == "report"):
                form = self.get_report(p_ssn, args["report_id"])

            # Handle logic for getting new applicant form.
            elif (args["form_type"] == "new_applicant_form"):
                form = self.get_new_applicant_form(p_ssn)

            # Handle logic for getting covid screen.
            elif (args["form_type"] == "covid_screen"):
                form = self.get_covid_screen(p_ssn, args["screen_date"])

            # Handle logic for getting medical history.
            elif (args["form_type"] == "medical_history"):
                form = self.get_medical_history(p_ssn)

            return jsonify(
                logged_in=1,
                form=form
            )

    def create_report(self, ssn, form):
        """Creates a new report to be added to the database.
        Picks a random doctor from the selected location.
        """

        con, cursor = db.connect_db()

        # Select a doctor from the medial centre.
        cursor.execute(
            "SELECT d.SSN as SSN FROM Doctor d, Works_At w, Medical_Centre m WHERE d.SSN = w.SSN AND w.Loc_Name = ? ORDER BY RANDOM() LIMIT 1;", (form["medical_centre"],))
        doctor = cursor.fetchone()

        # Get largest primary key.
        cursor.execute(
            "SELECT Report_ID FROM Report WHERE P_SSN = ? ORDER BY Report_ID DESC LIMIT 1;", (ssn,))
        report_id = cursor.fetchone()

        # Set id if it is the first report.
        if not report_id:
            new_id = 0
        else:
            new_id = report_id["Report_ID"] + 1

        # Add report to the database.
        cursor.execute("INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (?, ?, ?, ?);",
                       (new_id, ssn, doctor["SSN"] if doctor else None, form["Complaint"]))
        con.commit()
        con.close()

    def get_report(self, ssn, id):
        """Get a specific report given an ssn and id.
        """

        con, cursor = db.connect_db()

        # Get report.
        cursor.execute(
            "SELECT Complaint FROM Report WHERE Report_ID = ? AND P_SSN = ?;",
            (id, ssn)
        )
        result = cursor.fetchone()

        # Get doctor's name.
        cursor.execute(
            "SELECT d.Fname, d.Initial, d.Lname FROM Doctor d, Report r WHERE r.Report_ID = ? AND r.P_SSN = ? AND r.SSN = d.SSN;",
            (id, ssn)
        )
        doctor = cursor.fetchone()

        # If the hospital does not have a doctor.
        if not doctor:
            doctor = {"Fname": "", "Initial": "", "Lname": ""}

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

        # Join side effects to medications.
        for medication in medications:
            cursor.execute(
                "SELECT s.Effect FROM Side_Effects s WHERE s.Med_Name = ?;", (medication["Name"],))
            side_effects = cursor.fetchall()

            medication["Effects"] = [x["Effect"] for x in side_effects]

        # Get assigned medical centres.
        cursor.execute(
            "SELECT m.Name, m.Address, m.type FROM Medical_Centre m, Assigned a WHERE m.Name = a.MedCenter_Name AND a.Report_ID = ? AND a.P_SSN = ?;",
            (id, ssn)
        )
        medical_centres = cursor.fetchall()
        medical_centres = [dict(x) for x in medical_centres]

        con.close()

        return {
            **dict(result),
            **dict(doctor),
            **dict(illnesses),
            "Illness": list(illnesses),
            "Medications": list(medications),
            "Medical_centres": list(medical_centres)}

    def update_report(self, ssn, id, form):
        """Update a report given an ssn, id, and new form data.
        """

        con, cursor = db.connect_db()

        # Update the report.
        cursor.execute(
            "UPDATE Report SET Complaint = ? WHERE Report_ID = ? AND P_SSN = ?;", (form["Complaint"], id, ssn))

        con.commit()
        con.close()

    def get_new_applicant_form(self, ssn):
        """Get the new applicant form for a patient given their ssn.
        """

        con, cursor = db.connect_db()

        # Get all new applicant form data.
        cursor.execute(
            "SELECT * FROM New_Applicant_Form WHERE P_SSN = ?;", (ssn,))
        result = cursor.fetchone()

        con.close()

        return dict(result)

    def update_new_applicant_form(self, ssn, form, approved):
        """Update new applicant form data for a patient.
        """

        con, cursor = db.connect_db()

        # Update the form with the replacement data.
        cursor.execute("INSERT OR REPLACE INTO New_Applicant_Form VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (
                           ssn,
                           form["email"],
                           form["gender"],
                           form["sex"],
                           form["phone"],
                           form["fname"],
                           form["initial"],
                           form["lname"],
                           form["healthcare_no"],
                           form["hcn_expiry"],
                           form["hcn_province"],
                           form["dob"],
                           approved
                       )
                       )
        con.commit()
        con.close()

    def get_covid_screen(self, ssn, date):
        """Get covid screen data given a patient's ssn and date.
        """

        con, cursor = db.connect_db()

        # Get the covid screen data.
        cursor.execute(
            "SELECT * FROM Covid_Screen WHERE Date = ? AND P_SSN = ?;", (date, ssn))
        result = cursor.fetchone()

        con.close()

        return dict(result)

    def create_covid_screen(self, ssn, form):
        """Create a new covid screen for a patient.
        Uses the current date as the key.
        """

        con, cursor = db.connect_db()

        date = str(datetime.date.today())

        has_passed = 1

        # Check to see if the patient has passed
        for x in list(form.values()):
            if x == 1:
                has_passed = 0
                break

        # Create new covid screen.
        cursor.execute(
            "INSERT OR REPLACE INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose, Has_passed) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
            (
                date,
                ssn,
                form["Shortness_breath"],
                form["New_cough"],
                form["Fever"],
                form["Sore_throat"],
                form["Runny_nose"],
                has_passed
            )
        )

        con.commit()
        con.close()

    def update_covid_screen(self, ssn, date, form):
        """Update an existing covid screen with new data.
        """

        con, cursor = db.connect_db()

        has_passed = 1

        # Check to see if the patient has passed
        for x in list(form.values()):
            if x == 1:
                has_passed = 0
                break

        # Update the form.
        cursor.execute("UPDATE Covid_Screen SET Shortness_breath = ?, New_cough = ?, Fever = ?, Sore_throat = ?, Runny_nose = ?, Has_passed = ? WHERE Date = ? AND P_SSN = ?;",
                       (
                           form["Shortness_breath"],
                           form["New_cough"],
                           form["Fever"],
                           form["Sore_throat"],
                           form["Runny_nose"],
                           has_passed,
                           date,
                           ssn
                       )
                       )

        con.commit()
        con.close()

    def get_medical_history(self, ssn):
        """Get a medical history form data for a patient.
        """

        con, cursor = db.connect_db()

        # Get medical history form data.
        cursor.execute(
            "SELECT * FROM Medical_History WHERE P_SSN = ?;", (ssn,))
        medical_history = cursor.fetchone()
        medical_history = dict(medical_history)

        # Get all past illnesses.
        cursor.execute(
            "SELECT p.Illness_name, p.Age_of_onset FROM Past_Illnesses p WHERE P_SSN = ?;", (ssn,))
        past_illnesses = cursor.fetchall()
        past_illnesses = [dict(x) for x in past_illnesses]
        medical_history["Past_illnesses"] = past_illnesses

        # Get all allergies.
        cursor.execute(
            "SELECT a.Allergy FROM Allergies a WHERE P_SSN = ?;", (ssn,))
        allergies = cursor.fetchall()
        allergies = [x["Allergy"] for x in allergies]
        medical_history["Allergies"] = allergies

        # Get all immunizations.
        cursor.execute(
            "SELECT i.Immunization FROM Immunization i WHERE P_SSN = ?;", (ssn,))
        immunizations = cursor.fetchall()
        immunizations = [x["Immunization"] for x in immunizations]
        medical_history["Immunizations"] = immunizations

        return medical_history

    def update_medical_history(self, ssn, form):
        """Update the medical history form for a patient.
        """

        con, cursor = db.connect_db()

        # Create the medical history form.
        cursor.execute("INSERT OR REPLACE INTO Medical_History VALUES (?, ?, ?, ?, ?);",
                       (
                           ssn,
                           form["TPAL_total"],
                           form["TPAL_preterm"],
                           form["TPAL_aborted"],
                           form["TPAL_living"]
                       )
                       )

        # Update past illness.
        cursor.execute("DELETE FROM Past_Illnesses WHERE P_SSN = ?;", (ssn,))
        for illness in form["Past_illnesses"]:
            cursor.execute("INSERT INTO Past_Illnesses VALUES (?, ?, ?);",
                           (ssn, illness["Illness_name"], illness["Age_of_onset"]))

        # Update allergies.
        cursor.execute("DELETE FROM Allergies WHERE P_SSN = ?;", (ssn,))
        for allergy in form["Allergies"]:
            cursor.execute(
                "INSERT INTO Allergies VALUES (?, ?);", (ssn, allergy))

        # Update immunizations.
        cursor.execute("DELETE FROM Immunization WHERE P_SSN = ?;", (ssn,))
        for immunization in form["Immunizations"]:
            cursor.execute(
                "INSERT INTO Immunization VALUES (?, ?);", (ssn, immunization))

        con.commit()
        con.close()
