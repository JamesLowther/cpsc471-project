from flask import jsonify
from flask_restful import Resource, reqparse

from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database import db

import json, datetime


class Patient(Resource):
    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        return jsonify({**current, "logged_in": 1})


class PatientForms(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("form_type", type=str, required=True, choices=("report", "new_applicant_form", "medical_history", "covid_screen"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("action_type", type=str, required=True, choices=("get_form", "submit_form"),
                        help="Bad choice: {error_msg}")
    parser.add_argument("new_form", type=int)
    parser.add_argument("report_id", type=int, required=False)
    parser.add_argument("applicant_form", type=str, required=False)
    parser.add_argument("history_id", type=int, required=False)
    parser.add_argument("screen_date", type=str, required=False)
    parser.add_argument("form", type=dict)

    def get(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        con, cursor = db.connect_db()

        # Get all reports.
        cursor.execute(
            "SELECT Report_ID FROM Report WHERE P_SSN = ?;", (current["ssn"],))
        reports = cursor.fetchall()

        # Get all new applicant forms.
        cursor.execute(
            "SELECT Email FROM New_Applicant_Form WHERE P_SSN = ?;", (current["ssn"],))
        new_applicant = cursor.fetchall()

        # Get all covid screens.
        cursor.execute(
            "SELECT Date FROM Covid_Screen WHERE P_SSN = ?;", (current["ssn"],))
        covid_screen = cursor.fetchall()

        # Get medical history forms.
        cursor.execute(
            "SELECT Hx_ID FROM Medical_History WHERE P_SSN = ?;", (current["ssn"],))
        medical_history = cursor.fetchall()

        con.close()

        return jsonify(
            logged_in=1,
            reports=[dict(x) for x in reports],
            new_applicant=[dict(x) for x in new_applicant],
            covid_screen=[dict(x) for x in covid_screen],
            medical_history=[dict(x) for x in medical_history]
        )

    def post(self):
        if verify_jwt_in_request():
            current = get_jwt_identity()

        args = self.parser.parse_args()

        if (args["action_type"] == "submit_form"):
            if (args["form_type"] == "report"):
                if args["new_form"]:
                    self.create_report(current["ssn"], args["form"])
                else:
                    self.update_report(
                        current["ssn"], args["report_id"], args["form"])

            elif (args["form_type"] == "new_applicant_form"):
                self.update_new_applicant_form(current["ssn"], args["form"])

            elif (args["form_type"] == "covid_screen"):
                if args["new_form"]:
                    self.create_covid_screen(current["ssn"], args["form"])
                else:
                    self.update_covid_screen(current["ssn"], args["screen_date"], args["form"])
            else:
                pass

            return jsonify(
                successful=1
            )

        else:
            if (args["form_type"] == "report"):
                form = self.get_report(
                    current["ssn"], args["report_id"])

            elif (args["form_type"] == "new_applicant_form"):
                form = self.get_new_applicant_form(
                    current["ssn"], args["applicant_form"])

            elif (args["form_type"] == "covid_screen"):
                form = self.get_covid_screen(
                    current["ssn"], args["screen_date"])

            else:
                pass

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
        if not report_id:
            new_id = 0
        else:
            new_id = report_id["Report_ID"] + 1

        # Add report to the database.
        cursor.execute("INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (?, ?, ?, ?);",
                       (new_id, ssn, doctor["SSN"], form["Complaint"]))
        con.commit()
        con.close()

    def get_report(self, ssn, id):

        con, cursor = db.connect_db()

        # Get form.
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
            **dict(result),
            **dict(doctor),
            **dict(illnesses),
            "Illness": list(illnesses),
            "Medications": list(medications),
            "Medical_centres": list(medical_centres)}

    def update_report(self, ssn, id, form):

        con, cursor = db.connect_db()

        cursor.execute(
            "UPDATE Report SET Complaint = ? WHERE Report_ID = ? AND P_SSN = ?;", (form["Complaint"], id, ssn))

        con.commit()
        con.close()

    def get_new_applicant_form(self, ssn, email):

        con, cursor = db.connect_db()

        cursor.execute(
            "SELECT * FROM New_Applicant_Form WHERE P_SSN = ? AND Email = ?;", (ssn, email))
        result = cursor.fetchone()

        con.close()

        return dict(result)

    def update_new_applicant_form(self, ssn, form):

        con, cursor = db.connect_db()

        cursor.execute("INSERT OR REPLACE INTO New_Applicant_Form VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
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
                           form["dob"]
                       )
                       )
        con.commit()
        con.close()

    def get_covid_screen(self, ssn, date):
        con, cursor = db.connect_db()

        cursor.execute("SELECT * FROM Covid_Screen WHERE Date = ? AND P_SSN = ?;", (date, ssn))
        result = cursor.fetchone()

        con.close()

        return dict(result)

    def create_covid_screen(self, ssn, form):
        con, cursor = db.connect_db()

        date = str(datetime.date.today())

        # Create new covid screen.
        cursor.execute(
            "INSERT OR REPLACE INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose) VALUES (?, ?, ?, ?, ?, ?, ?);",
            (   
                date,
                ssn,
                form["Shortness_breath"],
                form["New_cough"],
                form["Fever"],
                form["Sore_throat"],
                form["Runny_nose"]
            )
        )

        con.commit()
        con.close()

    def update_covid_screen(self, ssn, date, form):
        con, cursor = db.connect_db()

        print(ssn)
        print(date)

        cursor.execute("UPDATE Covid_Screen SET Shortness_breath = ?, New_cough = ?, Fever = ?, Sore_throat = ?, Runny_nose = ? WHERE Date = ? AND P_SSN = ?;",
            (
                form["Shortness_breath"],
                form["New_cough"],
                form["Fever"],
                form["Sore_throat"],
                form["Runny_nose"],
                date,
                ssn
            )
        )

        con.commit()
        con.close()

