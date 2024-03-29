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
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Bowmont Medical Clinic', 200000004);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Wellness Medical Clinic', 200000004);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Brentwood Family Medical Centre', 200000004);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Alberta Childrens Hospital', 200000004);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Peter Lougheed Centre', 200000004);
INSERT INTO Works_At (Loc_Name, SSN) VALUES ('Rockyview General Hospital', 200000004);

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
INSERT INTO Patient (P_SSN, Password) VALUES (101000018, 'pass');
INSERT INTO Patient (P_SSN, Password) VALUES (101000019, 'pass');

INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000000, 'BestDressed_2020@goomail.com', 'M', 'M', '403-111-0002', 'Simon', 'S', 'Cowell', 	'1111111112', '2025-01-01', 'AB', '1959-10-07', 0);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000001, 'Greg.man@goomail.com', 	'M', 'M', '403-111-0000', 'Greg', 'M', 'Man', 	'1111111110', '2025-01-01', 'AB', '1960-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000002, 'Brenda.boo@goomail.com', 'F', 'F', '403-111-0001', 'Brenda', 'B', 'Boo', 	'1111111111', '2025-01-01', 'AB', '1975-01-01', 0);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000003, 'Jenny.girl@goomail.com', 'F', 'F', '403-111-0002', 'Jenny', 'G', 'Girl', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000004, 'Cierra.Vega@goomail.com', 'F', 'F', '403-111-0003', 'Cierra', 'G', 'Vega', 	'1111111113', '2025-01-01', 'AB', '2002-01-01', 0);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000005, 'Alden.Cantrell@goomail.com', 'F', 'F', '403-111-0004', 'Alden', 'G', 'Cantrell', 	'1111111114', '2025-01-01', 'AB', '2002-01-01', 0);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000006, 'Kierra.Gentry@goomail.com', 'F', 'F', '403-111-0005', 'Kierra', 'G', 'Gentry', 	'1111111115', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000007, 'Pierre.Cox@goomail.com', 'F', 'F', '403-111-0006', 'Pierre', 'G', 'Cox', 	'1111111116', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000008, 'Thomas.Crane@goomail.com', 'F', 'F', '403-111-0007', 'Thomas', 'G', 'Crane', 	'1111111117', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000009, 'Jenny.Shaffer@goomail.com', 'F', 'F', '403-111-0008', 'Miranda', 'G', 'Shaffer', 	'1111111118', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000010, 'Bradyn.Kramer@goomail.com', 'F', 'F', '403-111-0009', 'Bradyn', 'G', 'Kramer', 	'1111111119', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000011, 'Alvaro.Mcgee@goomail.com', 'F', 'F', '403-111-0010', 'Alvaro', 'G', 'Mcgee', 	'1111111120', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000012, 'Celeste.Luna@goomail.com', 'F', 'F', '403-111-0002', 'Celeste', 'G', 'Luna', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000013, 'Gwen.Benally@goomail.com', 'F', 'F', '403-111-0002', 'Gwen', 'G', 'Benally', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000014, 'Paulita.Esslinger@goomail.com', 'F', 'F', '403-111-0002', 'Paulita', 'G', 'Esslinger', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000015, 'Keva.Rioux@goomail.com', 'F', 'F', '403-111-0002', 'Keva', 'G', 'Rioux', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000016, 'Madelaine.Elmendorf@goomail.com', 'F', 'F', '403-111-0002', 'Madelaine', 'G', 'Elmendorf', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 1);
INSERT INTO New_Applicant_Form (P_SSN, Email, Gender, Sex, Phone, Fname, Initial, Lname, Healthcare_no, HCN_expiry, HCN_province, DoB, Is_approved) VALUES (100000017, 'Isidro.Landaverde@goomail.com', 'F', 'F', '403-111-0002', 'Isidro', 'G', 'Landaverde', 	'1111111112', '2025-01-01', 'AB', '2002-01-01', 0);


INSERT INTO Authorizes (P_SSN, SSN) VALUES (100000001, 300000000);

 -- MEDICAL HISORY AND APPLICANT FORM INFORMATION for Simon - SSN [100000000]
INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose, Has_passed) VALUES ('2021-03-07', 100000000, 0, 0, 0, 0, 0, 0);
INSERT INTO Medical_History (P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (100000000, 0, 0, 0, 0);
INSERT INTO Allergies (P_SSN, Allergy) VALUES (100000000, 'Peanuts');
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000000, 'Measles');
INSERT INTO Past_Illnesses (P_SSN, Illness_Name, Age_of_onset) VALUES (100000000, 'High Blood Pressure', 	61);
INSERT INTO Past_Illnesses (P_SSN, Illness_Name, Age_of_onset) VALUES (100000000, 'Common Cold', 	35);
 -- Report #3 for Simon - SSN [100000000]
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (3, 100000000, 200000000, "Just feel horrible and been sweating. Chest sometimes hurts");
INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES ('High Blood Pressure', 	3, 100000000);
INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES ('Common Cold', 	3, 100000000);
INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES ('Lisinopril', 	3, 100000000);
INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES ('Advil', 	3, 100000000);
INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (3, 100000000, 'UofC Clinic');
 -- Report #4 for Simon - SSN [100000000]
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (4, 100000000, 200000000, "My chest is hurting worse then before now");


 -- MEDICAL HISORY AND APPLICANT FORM INFORMATION for Greg - SSN [100000001]
INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose, Has_passed) VALUES ('2021-02-06', 100000001, 1, 1, 1, 1, 0, 0);
INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose, Has_passed) VALUES ('2021-03-06', 100000001, 1, 1, 1, 1, 1, 1);
INSERT INTO Medical_History (P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (100000001, 0, 0, 0, 0);
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000001, 'Measles');
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000001, 'Tetanus');
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000001, 'Covid-19');
INSERT INTO Past_Illnesses (P_SSN, Illness_Name, Age_of_onset) VALUES (100000001, 'Common Cold',58);
INSERT INTO Past_Illnesses (P_SSN, Illness_Name, Age_of_onset) VALUES (100000001, 'Diabetes',60);
 -- Report #0 for Greg - SSN [100000001]
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (0, 100000001, 200000000, "I've had a cough for a few months but lately I've been waking up and coughing blood");
INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES ('Pneumonia', 0, 100000001);
INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES ('Azithromycin', 0, 100000001);
INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (0, 100000001, 'UofC Clinic');


 -- MEDICAL HISORY AND APPLICANT FORM INFORMATION for Brenda - SSN [100000002]
INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose, Has_passed) VALUES ('2021-02-06', 100000002, 1, 1, 1, 1, 1, 1);
INSERT INTO Medical_History (P_SSN, TPAL_total, TPAL_preterm, TPAL_aborted, TPAL_living) VALUES (100000002, 6, 1, 1, 4);
INSERT INTO Allergies (P_SSN, Allergy) VALUES (100000002, 'Peanuts');
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000002, 'Measles');
INSERT INTO Past_Illnesses (P_SSN, Illness_Name, Age_of_onset) VALUES (100000002, 'Pneumonia', 	30);
 -- Report #1 for Brenda - SSN [100000002]
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (1, 100000002, 200000001, "I've had lower back pain for several years but after vaccuming last week it's been unbareable. The pain goes all the way down my leg. I need an x-ray.");
INSERT INTO Diagnoses (Illness_Name, Report_ID, P_SSN) VALUES ('Low Back Pain', 1, 100000002);
INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES ('Ibuprofen', 1, 100000002);
INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (1, 100000002, 'Foothills');


 -- MEDICAL HISORY AND APPLICANT FORM INFORMATION for Jenny - SSN [100000003]INSERT INTO Allergies (P_SSN, Allergy) VALUES (100000001, 'Peanuts');
INSERT INTO Covid_Screen (Date, P_SSN, Shortness_breath, New_cough, Fever, Sore_throat, Runny_nose, Has_passed) VALUES ('2021-02-06', 100000003, 1, 1, 1, 1, 1, 1);
INSERT INTO Medical_History (P_SSN) VALUES (100000003);
INSERT INTO Allergies (P_SSN, Allergy) VALUES (100000003, 'Shrimp');
INSERT INTO Allergies (P_SSN, Allergy) VALUES (100000003, 'Penicillin');
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000003, 'Measles');
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000003, 'Tetanus');
INSERT INTO Immunization (P_SSN, Immunization) VALUES (100000003, 'GARDASIL9');
INSERT INTO Past_Illnesses (P_SSN, Illness_Name, Age_of_onset) VALUES (100000003, 'Asthma',7);
 -- Report #2 for Jenny - SSN [100000003]
INSERT INTO Report (Report_ID, P_SSN, SSN, Complaint) VALUES (2, 100000003, 200000002, "I'm considering dating but want to discuss birth control");
INSERT INTO Prescribes (Med_Name, Report_ID, P_SSN) VALUES ('Alesse', 2, 100000003);
INSERT INTO Assigned (Report_ID, P_SSN, MedCenter_Name) VALUES (2, 100000003, 'Foothills');








