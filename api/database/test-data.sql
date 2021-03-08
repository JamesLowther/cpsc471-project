INSERT INTO Illness (Name, Organ_system) VALUES ('Common Cold', 'Respiratory');
INSERT INTO Illness (Name, Organ_system) VALUES ('Asthma', 'Respiratory');
INSERT INTO Illness (Name, Organ_system) VALUES ('COPD', 'Respiratory');
INSERT INTO Illness (Name, Organ_system) VALUES ('Congestive Heart Failure', 'Circulatory');
INSERT INTO Illness (Name, Organ_system) VALUES ('High Blood Pressure', 'Circulatory');
INSERT INTO Illness (Name, Organ_system) VALUES ('Pneumonia', 'Respiratory');

INSERT INTO Medication (Name, Is_prescription) VALUES ('Advil', 0);
INSERT INTO Medication (Name, Is_prescription) VALUES ('Tramadol', 1);
INSERT INTO Medication (Name, Is_prescription) VALUES ('Lisinopril', 1);

-- INSERT INTO Side_Effects (Effect, Med_name) VALUES ('Advil', 'Nausea');

-- INSERT INTO Treats (Med_name, Illness_name) VALUES ('Advil', 'Headache');
-- INSERT INTO Treats (Med_name, Illness_name) VALUES ('Advil', 'Joint Pain');
-- INSERT INTO Treats (Med_name, Illness_name) VALUES ('Lisinopril', 'High Blood Pressure');

INSERT INTO Symptoms (Symptom_name, Illness_name) VALUES ('Fever', 'Common Cold');
INSERT INTO Symptoms (Symptom_name, Illness_name) VALUES ('Cough', 'Common Cold');
INSERT INTO Symptoms (Symptom_name, Illness_name) VALUES ('Sore Throat', 'Common Cold');
INSERT INTO Symptoms (Symptom_name, Illness_name) VALUES ('Congestion', 'Common Cold');
INSERT INTO Symptoms (Symptom_name, Illness_name) VALUES ('Sneezing', 'Common Cold');



INSERT INTO Medical_Centre (Name, Location, Type) VALUES ('UofC Clinic', '2500 University Dr NW', 'Clinic');
INSERT INTO Medical_Centre (Name, Location, Type) VALUES ('Foothills', '1403 29 St NW', 'Hospital');

INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000000, 'GP', 'Brody', 'Wells', 'W', '1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000001, 'Oncology', 'James', 'Lowther', 'L', '1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000002, 'Nephrology', 'Logan', 'Perry-Din', 'P', '1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000003, 'GP', 'Ann', 'Preston', 'P', '1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000004, 'Obstetrics', 'Virginia', 'Apgar', 'A', '1990-01-01', 'pass123');

INSERT INTO Clerk (SSN, Fname, Lname, Intial, DoB, Password) VALUES (300000000, 'Justin', 'P', 'Trudeau', '1990-01-01', 'primePass');
INSERT INTO Clerk (SSN, Fname, Lname, Intial, DoB, Password) VALUES (300000001, 'Sherry', 'W', 'Worth', '1990-01-01', 'clerk');

INSERT INTO Works_At (Loc_Name, SSN) VALUES ('UofC Clinic', 200000000);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Foothills', 200000001);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Foothills', 200000002);

INSERT INTO Patient (P_SSN, Password) VALUES (100000000, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000001, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000002, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000003, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000004, 'pass');

INSERT INTO New_Applicant_Form (Email, P_SSN, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB) VALUES ('Greg.man@goomail.com', 100000001, 'M', 'M', '4031110000', 'Greg', 'M', 'Man', '1111111110', '2025-01-01', 'AB', '1960-01-01');
INSERT INTO New_Applicant_Form (Email, P_SSN, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB) VALUES ('Brenda.boo@goomail.com', 100000002, 'F', 'F', '4031110001', 'Brenda', 'B', 'Boo', '1111111111', '2025-01-01', 'AB', '1975-01-01');
INSERT INTO New_Applicant_Form (Email, P_SSN, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB) VALUES ('Jenny.girl@goomail.com', 100000003, 'F', 'F', '4031110002', 'Jenny', 'G', 'Girl', '1111111112', '2025-01-01', 'AB', '2002-01-01');

INSERT INTO Medical_History (HID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (1, 100000001, 0, 0, 0, 0);
INSERT INTO Medical_History (HID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (2, 100000002, 2, 0, 0, 2);
INSERT INTO Medical_History (HID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (3, 100000000, 0, 0, 0, 0);

INSERT INTO Allergies (HID, P_SSN, Allergy) VALUES (1, 100000001, 'Peanuts');
INSERT INTO Allergies (HID, P_SSN, Allergy) VALUES (2, 100000002, 'Peanuts');

INSERT INTO Immunization (HID, P_SSN, Immunization) VALUES (1, 100000001, 'Measles');
INSERT INTO Immunization (HID, P_SSN, Immunization) VALUES (2, 100000002, 'Measles');

INSERT INTO Past_Illnesses (HID, P_SSN, Illness_name, Age_of_onset) VALUES (1, 100000001, 'Common Cold', 35);
INSERT INTO Past_Illnesses (HID, P_SSN, Illness_name, Age_of_onset) VALUES (2, 100000002, 'Pneumonia', 30);

-- INSERT INTO Diagnoses (Name, Report_ID, P_SSN, SSN) VALUES ('Common Cold', 0, 100000001, 200000000);
-- INSERT INTO Diagnoses (Name, Report_ID, P_SSN, SSN) VALUES ('Congestive Heart Failure', 3, 100000000, 200000000);

-- INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose) VALUES ('2021-03-07', 100000000, 0, 0, 0, 0, 0);
-- INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose) VALUES ('2021-03-06', 100000001, 1, 1, 1, 1, 1);

INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (0, 100000001, 200000000);
INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (1, 100000002, 200000001);
INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (2, 100000003, 200000002);
INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (3, 100000000, 200000000);

INSERT INTO Assigned (Report_ID, P_SSN, SSN, Med_Centre_Name) VALUES (0, 100000001, 200000000, 'UofC Clinic');
INSERT INTO Assigned (Report_ID, P_SSN, SSN, Med_Centre_Name) VALUES (1, 100000002, 200000001, 'Foothills');
INSERT INTO Assigned (Report_ID, P_SSN, SSN, Med_Centre_Name) VALUES (2, 100000003, 200000002, 'Foothills');

-- INSERT INTO Prescribes (Med_name, Report_ID, P_SSN, SSN) VALUES ('Advil', 1, 100000001, 200000000);
-- INSERT INTO Prescribes (Med_name, Report_ID, P_SSN, SSN) VALUES ('Lisinopril', 3, 100000000, 200000000);

-- INSERT INTO Treatment_Done (HID, P_SSN, Med_name, Illness_name, Date) VALUES (1, 100000001, 'Advil', 'Common Cold', '2021-03-07');
-- INSERT INTO Treatment_Done (HID, P_SSN, Med_name, Illness_name, Date) VALUES (3, 100000000, 'Lisinopril', 'High Blood Pressure', '2021-03-07');

