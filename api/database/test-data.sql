/* The following INSERTS are deployment data */
INSERT INTO Illness (Illness_id, Illness_Name, Organ_system) VALUES (0, 'Common Cold', 				'Respiratory');
INSERT INTO Illness (Illness_id, Illness_Name, Organ_system) VALUES (1, 'Asthma', 					'Respiratory');
INSERT INTO Illness (Illness_id, Illness_Name, Organ_system) VALUES (2, 'COPD', 					'Respiratory');
INSERT INTO Illness (Illness_id, Illness_Name, Organ_system) VALUES (3, 'Congestive Heart Failure', 'Circulatory');
INSERT INTO Illness (Illness_id, Illness_Name, Organ_system) VALUES (4, 'High Blood Pressure', 		'Circulatory');
INSERT INTO Illness (Illness_id, Illness_Name, Organ_system) VALUES (5, 'Pneumonia', 				'Respiratory');

INSERT INTO Medication (Med_id, Med_Name, Is_prescription) VALUES (0, 'Advil', 			0);
INSERT INTO Medication (Med_id, Med_Name, Is_prescription) VALUES (1, 'Tramadol', 		1);
INSERT INTO Medication (Med_id, Med_Name, Is_prescription) VALUES (2, 'Lisinopril', 	1);

INSERT INTO Side_Effects (Med_id, Effect) VALUES (0, 'Nausea');

INSERT INTO Treats (Med_id, Illness_id) VALUES (0,	0);
INSERT INTO Treats (Med_id, Illness_id) VALUES (2,	4);

INSERT INTO Symptoms (Illness_id, Symptom_name) VALUES (0, 'Fever');
INSERT INTO Symptoms (Illness_id, Symptom_name) VALUES (0, 'Cough');
INSERT INTO Symptoms (Illness_id, Symptom_name) VALUES (0, 'Sore Throat');
INSERT INTO Symptoms (Illness_id, Symptom_name) VALUES (0, 'Congestion');
INSERT INTO Symptoms (Illness_id, Symptom_name) VALUES (0, 'Sneezing');





/* The following INSERTS are for development testing*/
INSERT INTO Medical_Centre (MedCenter_id, MedCenter_Name, Address, Type) VALUES (0, 'UofC Clinic', 		'2500 University Dr NW', 	'Clinic');
INSERT INTO Medical_Centre (MedCenter_id, MedCenter_Name, Address, Type) VALUES (1, 'Foothills', 		'1403 29 St NW', 			'Hospital');

INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000000, 'GP', 			'Brody', 	'Wells', 'W', 		'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000001, 'Oncology', 	'James', 	'Lowther', 'L', 	'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000002, 'Nephrology', 	'Logan', 	'Perry-Din', 'P', 	'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000003, 'GP', 			'Ann', 		'Preston', 'P', 	'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Intial, DoB, Password) VALUES (200000004, 'Obstetrics', 	'Virginia', 'Apgar', 'A', 		'1990-01-01', 'pass123');

INSERT INTO Clerk (SSN, Fname, Lname, Intial, DoB, Password) VALUES (300000000, 'Justin', 'P', 'Trudeau', 	'1990-01-01', 'primePass');
INSERT INTO Clerk (SSN, Fname, Lname, Intial, DoB, Password) VALUES (300000001, 'Sherry', 'W', 'Worth', 	'1990-01-01', 'clerk');

INSERT INTO Works_At (Loc_id, SSN) VALUES (0, 200000000);
INSERT INTO Works_At (Loc_id, SSN) VALUES (1, 200000001);
INSERT INTO Works_At (Loc_id, SSN) VALUES (1, 200000002);

INSERT INTO Patient (P_SSN, Password) VALUES (100000000, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000001, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000002, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000003, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000004, 'pass');

INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB) VALUES (100000001, 'Greg.man@goomail.com', 	'M', 'M', '4031110000', 'Greg', 'M', 'Man', 	'1111111110', '2025-01-01', 'AB', '1960-01-01');
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB) VALUES (100000002, 'Brenda.boo@goomail.com', 'F', 'F', '4031110001', 'Brenda', 'B', 'Boo', 	'1111111111', '2025-01-01', 'AB', '1975-01-01');
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB) VALUES (100000003, 'Jenny.girl@goomail.com', 'F', 'F', '4031110002', 'Jenny', 'G', 'Girl', 	'1111111112', '2025-01-01', 'AB', '2002-01-01');

INSERT INTO Medical_History (Hx_ID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (1, 100000001, 0, 0, 0, 0);
INSERT INTO Medical_History (Hx_ID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (2, 100000002, 2, 0, 0, 2);
INSERT INTO Medical_History (Hx_ID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (3, 100000000, 0, 0, 0, 0);

INSERT INTO Allergies (Hx_ID, P_SSN, Allergy) VALUES (1, 100000001, 'Peanuts');
INSERT INTO Allergies (Hx_ID, P_SSN, Allergy) VALUES (2, 100000002, 'Peanuts');

INSERT INTO Immunization (Hx_ID, P_SSN, Immunization) VALUES (1, 100000001, 'Measles');
INSERT INTO Immunization (Hx_ID, P_SSN, Immunization) VALUES (2, 100000002, 'Measles');

INSERT INTO Past_Illnesses (Hx_ID, P_SSN, Illness_id, Age_of_onset) VALUES (1, 100000001, 0, 35);
INSERT INTO Past_Illnesses (Hx_ID, P_SSN, Illness_id, Age_of_onset) VALUES (2, 100000002, 5, 30);

INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose) VALUES ('2021-03-07', 100000000, 0, 0, 0, 0, 0);
INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose) VALUES ('2021-03-06', 100000001, 1, 1, 1, 1, 1);

INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (0, 100000001, 200000000);
INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (1, 100000002, 200000001);
INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (2, 100000003, 200000002);
INSERT INTO Report (Report_ID, P_SSN, SSN) VALUES (3, 100000000, 200000000);

INSERT INTO Diagnoses (Illness_id, Report_ID, P_SSN, SSN) VALUES (0, 0, 100000001, 200000000);
INSERT INTO Diagnoses (Illness_id, Report_ID, P_SSN, SSN) VALUES (3, 3, 100000000, 200000000);

INSERT INTO Assigned (Report_ID, P_SSN, SSN, MedCenter_id) VALUES (0, 100000001, 200000000, 0);
INSERT INTO Assigned (Report_ID, P_SSN, SSN, MedCenter_id) VALUES (1, 100000002, 200000001, 1);
INSERT INTO Assigned (Report_ID, P_SSN, SSN, MedCenter_id) VALUES (2, 100000003, 200000002, 1);

INSERT INTO Prescribes (Med_id, Report_ID, P_SSN, SSN) VALUES (0, 0, 100000001, 200000000);
INSERT INTO Prescribes (Med_id, Report_ID, P_SSN, SSN) VALUES (1, 3, 100000000, 200000000);

INSERT INTO Treatment_Done (Hx_ID, P_SSN, Med_id, Illness_id, Date) VALUES (1, 100000001, 0, 0, '2021-03-07');
INSERT INTO Treatment_Done (Hx_ID, P_SSN, Med_id, Illness_id, Date) VALUES (3, 100000000, 2, 4, '2021-03-07');

