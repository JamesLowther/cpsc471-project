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
    Intial          TEXT,
    DoB             TEXT,
    Password        TEXT NOT NULL,
    PRIMARY KEY (SSN)
);

CREATE TABLE Clerk (
    SSN             INTEGER NOT NULL,
    Fname           TEXT NOT NULL,
    Lname           TEXT NOT NULL,
    Intial          TEXT,
    DoB             TEXT,
    Password        TEXT NOT NULL,
    PRIMARY KEY (SSN)
);

CREATE TABLE Medical_Centre (
    Name            TEXT,
    Location        TEXT,
    Type            TEXT,
    PRIMARY KEY (Name)
);

-- Might be problem with foreign key
CREATE TABLE Works_At (
    Loc_Name        TEXT,
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
    Email           TEXT,
    P_SSN           INTEGER,
    Gender          TEXT,
    Sex             TEXT,
    Phone           TEXT,
    Fname           TEXT NOT NULL,
    Initial          TEXT,
    Lname           TEXT NOT NULL,
    Healthcare_no   TEXT NOT NULL,
    HCN_expiry      TEXT NOT NULL,
    HCN_province    TEXT NOT NULL,
    DoB             TEXT,
    PRIMARY KEY (Email, P_SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN)
);

CREATE TABLE Authorizes (
    Email           TEXT,
    P_SSN           INTEGER,
    SSN             TEXT,
    PRIMARY KEY (Email, P_SSN),
    FOREIGN KEY (Email, P_SSN) REFERENCES New_Applicant_Form(Email, P_SSN),
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
    Report_ID           TEXT,
    P_SSN               INTEGER,
    SSN                 TEXT,
    PRIMARY KEY (Report_ID, P_SSN, SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN),
    FOREIGN KEY (SSN) REFERENCES Doctor(SSN)
);

CREATE TABLE Assigned (
    Report_ID           TEXT,
    P_SSN               INTEGER,
    SSN                 INTEGER,
    Med_Centre_Name     TEXT,
    PRIMARY KEY (Report_ID, P_SSN, SSN, Med_Centre_Name),
    FOREIGN KEY (Report_ID, P_SSN, SSN) REFERENCES Report(Report_ID, P_SSN, SSN),
    FOREIGN KEY (Med_Centre_Name) REFERENCES  Medical_Centre(Name)
);

CREATE TABLE Medication (
    Name                TEXT,
    Is_prescription     INTEGER,
    PRIMARY KEY (Name)
);

CREATE TABLE Side_Effects (
    Effect              TEXT,
    Med_name            TEXT,
    PRIMARY KEY (Effect, Med_name),
    FOREIGN KEY (Med_name) REFERENCES Medication(Name)
);

CREATE TABLE Prescribes (
    Med_name            TEXT,
    Report_ID           TEXT,
    P_SSN               TEXT,
    SSN                 INTEGER,
    PRIMARY KEY (Med_name, Report_ID, P_SSN, SSN),
    FOREIGN KEY (Med_name) REFERENCES Medication(Name),
    FOREIGN KEY (Report_ID, P_SSN, SSN) REFERENCES Report(Report_ID, P_SSN, SSN)
);

CREATE TABLE Illness (
    Name                TEXT,
    Organ_system        TEXT,
    PRIMARY KEY (Name)
);

CREATE TABLE Symptoms (
    Symptom_name        TEXT,
    Illness_name        TEXT,
    PRIMARY KEY (Symptom_name, Illness_name),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);

CREATE TABLE Treats (
    Med_name            TEXT,
    Illness_name        TEXT,
    PRIMARY KEY (Med_name, Illness_name),
    FOREIGN KEY (Med_name) REFERENCES Medication(Name),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);

CREATE TABLE Diagnoses (
    Name            TEXT,
    Report_ID       TEXT,
    P_SSN           INTEGER,
    SSN             INTEGER,
    PRIMARY KEY (Name, Report_ID, P_SSN, SSN),
    FOREIGN KEY (Name) REFERENCES Illness(Name),
    FOREIGN KEY (Report_ID, P_SSN, SSN) REFERENCES Report(Report_ID, P_SSN, SSN)
);

CREATE TABLE Medical_History (
    HID             TEXT,
    P_SSN           INTEGER,
    TPAL_total      INTEGER,
    TPAL_preterm    INTEGER,
    TPAL_aborted    INTEGER,
    TPAL_living     INTEGER,
    PRIMARY KEY (HID, P_SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN)
);

CREATE TABLE Allergies (
    HID             TEXT,
    P_SSN           INTEGER,
    Allergy         TEXT,
    PRIMARY KEY (HID, P_SSN, Allergy),
    FOREIGN KEY (HID, P_SSN) REFERENCES Medical_History(HID, P_SSN)
);

CREATE TABLE Immunization (
    HID             TEXT,
    P_SSN           INTEGER,
    Immunization    TEXT,
    PRIMARY KEY (HID, P_SSN, Immunization),
    FOREIGN KEY (HID, P_SSN) REFERENCES Medical_History(HID, P_SSN)
);

CREATE TABLE Treatment_Done (
    HID             TEXT,
    P_SSN           INTEGER,
    Med_name        TEXT,
    Illness_name    TEXT,
    Date            TEXT,
    PRIMARY KEY (HID, P_SSN, Med_name, Illness_name),
    FOREIGN KEY (HID, P_SSN) REFERENCES Medical_History(HID, P_SSN),
    FOREIGN KEY (Med_name) REFERENCES Medication(Name),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);

CREATE TABLE Past_Illnesses (
    HID             TEXT,
    P_SSN           INTEGER,
    Illness_name    TEXT,
    Age_of_onset    INTEGER,
    PRIMARY KEY (HID, P_SSN, Illness_name),
    FOREIGN KEY (HID, P_SSN) REFERENCES Medical_History(HID, P_SSN),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);