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
    SSN             TEXT,
    Specialization  TEXT,
    Fname           TEXT,
    Lname           TEXT,
    Intial          TEXT,
    DoB             TEXT,
    Password        TEXT,
    PRIMARY KEY (SSN)
);

CREATE TABLE Clerk (
    SSN             TEXT,
    Fname           TEXT,
    Lname           TEXT,
    Intial          TEXT,
    DoB             TEXT,
    Password        TEXT,
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
    SSN             TEXT,
    PRIMARY KEY (Loc_Name, SSN),
    FOREIGN KEY (Loc_Name) REFERENCES Medical_Centre(Location),
    FOREIGN KEY (SSN) REFERENCES Doctor(SSN)
);

CREATE TABLE Patient (
    PID             TEXT,
    Password        TEXT,
    PRIMARY KEY (PID)
);

CREATE TABLE New_Applicant_Form (
    Email           TEXT,
    PID             TEXT,
    Gender          TEXT,
    Sex             TEXT,
    Phone           TEXT,
    Fname           TEXT,
    Intial          TEXT,
    Lname           TEXT,
    Healthcare_no   TEXT,
    HCN_expiry      TEXT,
    HCN_province    TEXT,
    DoB             TEXT,
    PRIMARY KEY (Email, PID),
    FOREIGN KEY (PID) REFERENCES Patient(PID)
);

CREATE TABLE Authorizes (
    Email           TEXT,
    PID             TEXT,
    SSN             TEXT,
    PRIMARY KEY (Email, PID),
    FOREIGN KEY (Email, PID) REFERENCES New_Applicant_Form(Email, PID),
    FOREIGN KEY (SSN) REFERENCES Clerk(SSN)
);

CREATE TABLE Covid_Screen (
    Date                TEXT,
    PID                 TEXT,
    Shortness_breath    INTEGER,
    New_cough           INTEGER,
    Fever               INTEGER,
    Sore_throat         INTEGER,
    Runny_nose          INTEGER,
    PRIMARY KEY (Date, PID),
    FOREIGN KEY (PID) REFERENCES Patient(PID)
);

CREATE TABLE Report (
    Report_ID           TEXT,
    PID                 TEXT,
    SSN                 TEXT,
    PRIMARY KEY (Report_ID, PID, SSN),
    FOREIGN KEY (PID) REFERENCES Patient(PID),
    FOREIGN KEY (SSN) REFERENCES Doctor(SSN)
);

CREATE TABLE Assigned (
    Report_ID           TEXT,
    PID                 TEXT,
    SSN                 TEXT,
    Med_Centre_Name     TEXT,
    PRIMARY KEY (Report_ID, PID, SSN, Med_Centre_Name),
    FOREIGN KEY (Report_ID, PID, SSN) REFERENCES Report(Report_ID, PID, SSN),
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
    PID                 TEXT,
    SSN                 TEXT,
    PRIMARY KEY (Med_name, Report_ID, PID, SSN),
    FOREIGN KEY (Med_name) REFERENCES Medication(Name),
    FOREIGN KEY (Report_ID, PID, SSN) REFERENCES Report(Report_ID, PID, SSN)
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
    PID             TEXT,
    SSN             TEXT,
    PRIMARY KEY (Name, Report_ID, PID, SSN),
    FOREIGN KEY (Name) REFERENCES Illness(Name),
    FOREIGN KEY (Report_ID, PID, SSN) REFERENCES Report(Report_ID, PID, SSN)
);

CREATE TABLE Medical_History (
    HID             TEXT,
    PID             TEXT,
    Age_of_onset    INTEGER,
    TPAL_total      INTEGER,
    TPAL_preterm    INTEGER,
    TPAL_aborted    INTEGER,
    TPAL_living     INTEGER,
    PRIMARY KEY (HID, PID),
    FOREIGN KEY (PID) REFERENCES Patient(PID)
);

CREATE TABLE Allergies (
    HID             TEXT,
    PID             TEXT,
    Allergy         TEXT,
    PRIMARY KEY (HID, PID, Allergy),
    FOREIGN KEY (HID, PID) REFERENCES Medical_History(HID, PID)
);

CREATE TABLE Immunization (
    HID             TEXT,
    PID             TEXT,
    Immunization    TEXT,
    PRIMARY KEY (HID, PID, Immunization),
    FOREIGN KEY (HID, PID) REFERENCES Medical_History(HID, PID)
);

CREATE TABLE Treatment_Done (
    HID             TEXT,
    PID             TEXT,
    Med_name        TEXT,
    Illness_name    TEXT,
    Date            TEXT,
    PRIMARY KEY (HID, PID, Med_name, Illness_name),
    FOREIGN KEY (HID, PID) REFERENCES Medical_History(HID, PID),
    FOREIGN KEY (Med_name) REFERENCES Medication(Name),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);

CREATE TABLE Past_Illnesses (
    HID             TEXT,
    PID             TEXT,
    Illness_name    TEXT,
    PRIMARY KEY (HID, PID, Illness_name),
    FOREIGN KEY (HID, PID) REFERENCES Medical_History(HID, PID),
    FOREIGN KEY (Illness_name) REFERENCES Illness(Name)
);