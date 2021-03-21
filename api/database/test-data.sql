INSERT INTO Medical_Centre (Name, Address, Type) VALUES ('UofC Clinic', 	'2500 University Dr NW', 	'Clinic');
INSERT INTO Medical_Centre (Name, Address, Type) VALUES ('Foothills', 		'1403 29 St NW', 			'Hospital');

INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Initial, DoB, Password) VALUES (200000000, 'GP', 			'Brody', 	'Wells', 'W', 		'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Initial, DoB, Password) VALUES (200000001, 'Oncology', 	'James', 	'Lowther', 'L', 	'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Initial, DoB, Password) VALUES (200000002, 'Nephrology', 	'Logan', 	'Perry-Din', 'P', 	'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Initial, DoB, Password) VALUES (200000003, 'GP', 			'Ann', 		'Preston', 'P', 	'1990-01-01', 'pass123');
INSERT INTO Doctor (SSN, Specialization, Fname, Lname, Initial, DoB, Password) VALUES (200000004, 'Obstetrics', 	'Virginia', 'Apgar', 'A', 		'1990-01-01', 'pass123');

INSERT INTO Clerk (SSN, Fname, Lname, Initial, DoB, Password) VALUES (300000000, 'Justin', 'P', 'Trudeau', 	'1990-01-01', 'primePass');
INSERT INTO Clerk (SSN, Fname, Lname, Initial, DoB, Password) VALUES (300000001, 'Sherry', 'W', 'Worth', 	'1990-01-01', 'clerk');

INSERT INTO Works_At (Loc_Name, SSN) VALUES ('UofC Clinic', 200000000);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Foothills', 200000001);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Foothills', 200000002);

INSERT INTO Patient (P_SSN, Password) VALUES (100000000, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000001, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000002, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000003, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000004, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000005, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000006, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000007, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000008, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000009, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000010, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000011, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000012, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000013, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000014, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000015, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000016, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (100000017, 'pass');

INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000001, 'Greg.man@goomail.com', 	'M', 'M', '4031110000', 'Greg', 'M', 'Man', 	'1111111110', '2025-01-01', 'AB', '1960-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000002, 'Brenda.boo@goomail.com', 'F', 'F', '4031110001', 'Brenda', 'B', 'Boo', 	'1111111111', '2025-01-01', 'AB', '1975-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000003, 'Jenny.girl@goomail.com', 'F', 'F', '4031110002', 'Jenny', 'G', 'Girl', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000004, 'Cierra.Vega@goomail.com', 'F', 'F', '4031110003', 'Cierra', 'G', 'Vega', 	'1111111113', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000005, 'Alden.Cantrell@goomail.com', 'F', 'F', '4031110004', 'Alden', 'G', 'Cantrell', 	'1111111114', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000006, 'Kierra.Gentry@goomail.com', 'F', 'F', '4031110005', 'Kierra', 'G', 'Gentry', 	'1111111115', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000007, 'Pierre.Cox@goomail.com', 'F', 'F', '4031110006', 'Pierre', 'G', 'Cox', 	'1111111116', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000008, 'Thomas.Crane@goomail.com', 'F', 'F', '4031110007', 'Thomas', 'G', 'Crane', 	'1111111117', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000009, 'Jenny.Shaffer@goomail.com', 'F', 'F', '4031110008', 'Miranda', 'G', 'Shaffer', 	'1111111118', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000010, 'Bradyn.Kramer@goomail.com', 'F', 'F', '4031110009', 'Bradyn', 'G', 'Kramer', 	'1111111119', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000011, 'Alvaro.Mcgee@goomail.com', 'F', 'F', '4031110010', 'Alvaro', 'G', 'Mcgee', 	'1111111120', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000012, 'Celeste.Luna@goomail.com', 'F', 'F', '4031110002', 'Celeste', 'G', 'Luna', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000013, 'Gwen.Benally@goomail.com', 'F', 'F', '4031110002', 'Gwen', 'G', 'Benally', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000014, 'Paulita.Esslinger@goomail.com', 'F', 'F', '4031110002', 'Paulita', 'G', 'Esslinger', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000015, 'Keva.Rioux@goomail.com', 'F', 'F', '4031110002', 'Keva', 'G', 'Rioux', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000016, 'Madelaine.Elmendorf@goomail.com', 'F', 'F', '4031110002', 'Madelaine', 'G', 'Elmendorf', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000017, 'Isidro.Landaverde@goomail.com', 'F', 'F', '4031110002', 'Isidro', 'G', 'Landaverde', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 0);

INSERT INTO Authorizes (P_SSN, SSN) VALUES (100000001, 300000000);

INSERT INTO Medical_History (Hx_ID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (1, 100000001, 0, 0, 0, 0);
INSERT INTO Medical_History (Hx_ID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (2, 100000002, 2, 0, 0, 2);
INSERT INTO Medical_History (Hx_ID, P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (3, 100000000, 0, 0, 0, 0);

INSERT INTO Allergies (Hx_ID, P_SSN, Allergy) VALUES (1, 100000001, 'Peanuts');
INSERT INTO Allergies (Hx_ID, P_SSN, Allergy) VALUES (2, 100000002, 'Peanuts');

INSERT INTO Immunization (Hx_ID, P_SSN, Immunization) VALUES (1, 100000001, 'Measles');
INSERT INTO Immunization (Hx_ID, P_SSN, Immunization) VALUES (2, 100000002, 'Measles');

INSERT INTO Past_Illnesses (Hx_ID, P_SSN, Illness_Name, Age_of_onset) VALUES (1, 100000001, 'Common Cold', 	35);
INSERT INTO Past_Illnesses (Hx_ID, P_SSN, Illness_Name, Age_of_onset) VALUES (2, 100000002, 'Pneumonia', 	30);

INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose) VALUES ('2021-03-07', 100000000, 0, 0, 0, 0, 0);
INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose) VALUES ('2021-03-06', 100000001, 1, 1, 1, 1, 1);

INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (0, 100000001, 200000000, "Test 1");
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (1, 100000002, 200000001, "Test 2");
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (2, 100000003, 200000002, "Test 3");
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (3, 100000000, 200000000, "Test 4");

INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES ('Common Cold', 			0, 100000001);
INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES ('High Blood Pressure', 	3, 100000000);
INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES ('Common Cold', 	3, 100000000);

INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (3, 100000000, 'UofC Clinic');
INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (0, 100000001, 'UofC Clinic');
INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (1, 100000002, 'Foothills');
INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (2, 100000003, 'Foothills');

INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES ('Advil', 		0, 100000001);
INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES ('Lisinopril', 	3, 100000000);

INSERT INTO Treatment_Done (Hx_ID, P_SSN, Med_Name, Illness_Name, Date) VALUES (1, 100000001, 'Advil', 		'Common Cold', 			'2021-03-07');
INSERT INTO Treatment_Done (Hx_ID, P_SSN, Med_Name, Illness_Name, Date) VALUES (3, 100000000, 'Lisinopril', 'High Blood Pressure', 	'2021-03-07');

