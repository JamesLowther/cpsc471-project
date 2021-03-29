PRAGMA foreign_keys = ON;

-- Drop tables
DROP TABLE IF EXISTS Doctor;
DROP TABLE IF EXISTS Clerk;
DROP TABLE IF EXISTS Medical_Centre;
DROP TABLE IF EXISTS Works_At;
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS New_Applicant_Form;
DROP TABLE IF EXISTS Authorizes;
DROP TABLE IF EXISTS Covid_Screen;
DROP TABLE IF EXISTS Report;
DROP TABLE IF EXISTS Assigned;
DROP TABLE IF EXISTS Medication;
DROP TABLE IF EXISTS Side_Effects;
DROP TABLE IF EXISTS Prescribes;
DROP TABLE IF EXISTS Illness;
DROP TABLE IF EXISTS Symptoms;
DROP TABLE IF EXISTS Treats;
DROP TABLE IF EXISTS Diagnoses;
DROP TABLE IF EXISTS Medical_History;
DROP TABLE IF EXISTS Allergies;
DROP TABLE IF EXISTS Immunization;
DROP TABLE IF EXISTS Treatment_Done;
DROP TABLE IF EXISTS Past_Illnesses;

-- Create new tables
CREATE TABLE Doctor (
    SSN             INTEGER NOT NULL,
    Specialization  TEXT,
    Fname           TEXT NOT NULL,
    Lname           TEXT NOT NULL,
    Initial         TEXT,
    DoB             TEXT,
    Password        TEXT NOT NULL,
    PRIMARY KEY (SSN)
);

CREATE TABLE Clerk (
    SSN             INTEGER NOT NULL,
    Fname           TEXT NOT NULL,
    Lname           TEXT NOT NULL,
    Initial          TEXT,
    DoB             TEXT,
    Password        TEXT NOT NULL,
    PRIMARY KEY (SSN)
);

CREATE TABLE Medical_Centre (
    Name            TEXT,
    Address         TEXT,
    Type            TEXT,
    PRIMARY KEY (Name)
);

-- Might be problem with foreign key
CREATE TABLE Works_At (
    Loc_Name            TEXT,
    SSN             INTEGER,
    PRIMARY KEY (Loc_Name, SSN),
    FOREIGN KEY (Loc_Name) REFERENCES Medical_Centre(Name),
    FOREIGN KEY (SSN) REFERENCES Doctor(SSN)
);

CREATE TABLE Patient (
    P_SSN           INTEGER NOT NULL,
    Password        TEXT NOT NULL,
    PRIMARY KEY (P_SSN)
);

CREATE TABLE New_Applicant_Form (
    P_SSN           INTEGER,
    Email           TEXT,
    Gender          TEXT,
    Sex             TEXT,
    Phone           TEXT,
    Fname           TEXT NOT NULL,
    Initial         TEXT,
    Lname           TEXT NOT NULL,
    Healthcare_no   TEXT NOT NULL,
    HCN_expiry      TEXT NOT NULL,
    HCN_province    TEXT NOT NULL,
    DoB             TEXT,
    Is_approved     INTEGER,
    PRIMARY KEY (P_SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN)
);

CREATE TABLE Authorizes (
    P_SSN           INTEGER,
    SSN             INTEGER,
    PRIMARY KEY (P_SSN, SSN),
    FOREIGN KEY (P_SSN) REFERENCES New_Applicant_Form(P_SSN),
    FOREIGN KEY (SSN) REFERENCES Clerk(SSN)
);

CREATE TABLE Covid_Screen (
    Date                TEXT,
    P_SSN               INTEGER,
    Shortness_breath    INTEGER NOT NULL,
    New_cough           INTEGER NOT NULL,
    Fever               INTEGER NOT NULL,
    Sore_throat         INTEGER NOT NULL,
    Runny_nose          INTEGER NOT NULL,
    PRIMARY KEY (Date, P_SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN)
);

CREATE TABLE Report (
    Report_ID           INTEGER,
    P_SSN               INTEGER,
    SSN                 INTEGER,
    Complaint           TEXT,
    PRIMARY KEY (Report_ID, P_SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN),
    FOREIGN KEY (SSN) REFERENCES Doctor(SSN)
);

CREATE TABLE Assigned (
    Report_ID           INTEGER,
    P_SSN               INTEGER,
    MedCenter_Name      TEXT,
    PRIMARY KEY (Report_ID, P_SSN, MedCenter_Name),
    FOREIGN KEY (Report_ID, P_SSN) REFERENCES Report(Report_ID, P_SSN),
    FOREIGN KEY (MedCenter_Name) REFERENCES  Medical_Centre(Name)
);

CREATE TABLE Medication (
    Name                TEXT,
    Is_prescription     INTEGER,
    PRIMARY KEY (Name)
);

CREATE TABLE Side_Effects (
    Med_Name            TEXT,
    Effect              TEXT,
    PRIMARY KEY (Effect, Med_Name),
    FOREIGN KEY (Med_Name) REFERENCES Medication(Name)
);

CREATE TABLE Prescribes (
    Med_Name            TEXT,
    Report_ID           INTEGER,
    P_SSN               INTEGER,
    PRIMARY KEY (Med_Name, Report_ID, P_SSN),
    FOREIGN KEY (Med_Name) REFERENCES Medication(Name),
    FOREIGN KEY (Report_ID, P_SSN) REFERENCES Report(Report_ID, P_SSN)
);

CREATE TABLE Illness (
    Name                TEXT,
    Organ_system        TEXT,
    PRIMARY KEY (Name)
);

CREATE TABLE Symptoms (
    Illness_name        TEXT,
    Symptom_name        TEXT,
    PRIMARY KEY (Illness_name, Symptom_name),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);

CREATE TABLE Treats (
    Med_Name          TEXT,
    Illness_name      TEXT,
    PRIMARY KEY (Med_Name, Illness_name),
    FOREIGN KEY (Med_Name) REFERENCES Medication(Name),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);

CREATE TABLE Diagnoses (
    Illness_name    TEXT,
    Report_ID       INTEGER,    
    P_SSN           INTEGER,
    PRIMARY KEY (Illness_name, Report_ID, P_SSN),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name),
    FOREIGN KEY (Report_ID, P_SSN) REFERENCES Report(Report_ID, P_SSN)
);

CREATE TABLE Medical_History (
    P_SSN           INTEGER,
    TPAL_total      INTEGER,
    TPAL_preterm    INTEGER,
    TPAL_aborted    INTEGER,
    TPAL_living     INTEGER,
    PRIMARY KEY (P_SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN)
);

CREATE TABLE Allergies (
    P_SSN           INTEGER,
    Allergy         TEXT,
    PRIMARY KEY (P_SSN, Allergy),
    FOREIGN KEY (P_SSN) REFERENCES Medical_History(P_SSN)
);

CREATE TABLE Immunization (
    P_SSN           INTEGER,
    Immunization    TEXT,
    PRIMARY KEY (P_SSN, Immunization),
    FOREIGN KEY (P_SSN) REFERENCES Medical_History(P_SSN)
);

CREATE TABLE Treatment_Done (
    P_SSN           INTEGER,
    Med_Name        TEXT,
    Illness_name    TEXT,
    Date            TEXT,
    PRIMARY KEY (P_SSN, Med_Name, Illness_name),
    FOREIGN KEY (P_SSN) REFERENCES Medical_History(P_SSN),
    FOREIGN KEY (Med_Name) REFERENCES Medication(Name),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);

CREATE TABLE Past_Illnesses (
    P_SSN           INTEGER,
    Illness_name    TEXT,
    Age_of_onset    INTEGER,
    PRIMARY KEY (P_SSN, Illness_name),
    FOREIGN KEY (P_SSN) REFERENCES Medical_History(P_SSN),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);




INSERT INTO Illness (Name, Organ_system) VALUES ('Common Cold',             'Respiratory');
INSERT INTO Illness (Name, Organ_system) VALUES ('Asthma',                  'Respiratory');
INSERT INTO Illness (Name, Organ_system) VALUES ('COPD',                    'Respiratory');
INSERT INTO Illness (Name, Organ_system) VALUES ('Congestive Heart Failure', 'Circulatory');
INSERT INTO Illness (Name, Organ_system) VALUES ('High Blood Pressure',     'Circulatory');
INSERT INTO Illness (Name, Organ_system) VALUES ('Pneumonia',               'Respiratory');

INSERT INTO Medication (Name, Is_prescription) VALUES ('Advil',         0);
INSERT INTO Medication (Name, Is_prescription) VALUES ('Tramadol',      1);
INSERT INTO Medication (Name, Is_prescription) VALUES ('Lisinopril',    1);

INSERT INTO Side_Effects (Med_Name, Effect) VALUES ('Advil', 'Nausea');
INSERT INTO Side_Effects (Med_Name, Effect) VALUES ('Lisinopril', 'Tiredness');
INSERT INTO Side_Effects (Med_Name, Effect) VALUES ('Lisinopril', 'Headache');

INSERT INTO Treats (Med_Name, Illness_Name) VALUES ('Advil',        'Common Cold');
INSERT INTO Treats (Med_Name, Illness_Name) VALUES ('Lisinopril',   'High Blood Pressure');

INSERT INTO Symptoms (Illness_Name, Symptom_name) VALUES ('Common Cold', 'Fever');
INSERT INTO Symptoms (Illness_Name, Symptom_name) VALUES ('Common Cold', 'Cough');
INSERT INTO Symptoms (Illness_Name, Symptom_name) VALUES ('Common Cold', 'Sore Throat');
INSERT INTO Symptoms (Illness_Name, Symptom_name) VALUES ('Common Cold', 'Congestion');
INSERT INTO Symptoms (Illness_Name, Symptom_name) VALUES ('Common Cold', 'Sneezing');