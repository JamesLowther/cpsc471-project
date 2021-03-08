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
    MedCenter_id    INTEGER,
    MedCenter_Name  TEXT,
    Address         TEXT,
    Type            TEXT,
    PRIMARY KEY (MedCenter_id)
);

-- Might be problem with foreign key
CREATE TABLE Works_At (
    Loc_id          INTEGER,
    SSN             INTEGER,
    PRIMARY KEY (Loc_id, SSN),
    FOREIGN KEY (Loc_id) REFERENCES Medical_Centre(MedCenter_id),
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
    Initial          TEXT,
    Lname           TEXT NOT NULL,
    Healthcare_no   TEXT NOT NULL,
    HCN_expiry      TEXT NOT NULL,
    HCN_province    TEXT NOT NULL,
    DoB             TEXT,
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
    PRIMARY KEY (Report_ID, P_SSN, SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN),
    FOREIGN KEY (SSN) REFERENCES Doctor(SSN)
);

CREATE TABLE Assigned (
    Report_ID           INTEGER,
    P_SSN               INTEGER,
    SSN                 INTEGER,
    MedCenter_id      TEXT,
    PRIMARY KEY (Report_ID, P_SSN, SSN, MedCenter_id),
    FOREIGN KEY (Report_ID, P_SSN, SSN) REFERENCES Report(Report_ID, P_SSN, SSN),
    FOREIGN KEY (MedCenter_id) REFERENCES  Medical_Centre(MedCenter_id)
);

CREATE TABLE Medication (
    Med_id              INTEGER,
    Med_Name            TEXT,
    Is_prescription     INTEGER,
    PRIMARY KEY (Med_id)
);

CREATE TABLE Side_Effects (
    Med_id              INTEGER,
    Effect              TEXT,
    PRIMARY KEY (Effect, Med_id),
    FOREIGN KEY (Med_id) REFERENCES Medication(Med_id)
);

CREATE TABLE Prescribes (
    Med_id              INTEGER,
    Report_ID           INTEGER,
    P_SSN               INTEGER,
    SSN                 INTEGER,
    PRIMARY KEY (Med_id, Report_ID, P_SSN, SSN),
    FOREIGN KEY (Med_id) REFERENCES Medication(Med_id),
    FOREIGN KEY (Report_ID, P_SSN, SSN) REFERENCES Report(Report_ID, P_SSN, SSN)
);

CREATE TABLE Illness (
    Illness_id          INTEGER,
    Illness_Name        TEXT,
    Organ_system        TEXT,
    PRIMARY KEY (Illness_id)
);

CREATE TABLE Symptoms (
    Illness_id          INTEGER,
    Symptom_name        TEXT,
    PRIMARY KEY (Illness_id, Symptom_name),
    FOREIGN KEY (Illness_id) REFERENCES Illness(Illness_id)
);

CREATE TABLE Treats (
    Med_id            INTEGER,
    Illness_id        INTEGER,
    PRIMARY KEY (Med_id, Illness_id),
    FOREIGN KEY (Med_id) REFERENCES Medication(Med_id),
    FOREIGN KEY (Illness_id) REFERENCES Illness(Illness_id)
);

CREATE TABLE Diagnoses (
    Illness_id      INTEGER,
    Report_ID       INTEGER,
    P_SSN           INTEGER,
    SSN             INTEGER,
    PRIMARY KEY (Illness_id, Report_ID, P_SSN, SSN),
    FOREIGN KEY (Illness_id) REFERENCES Illness(Illness_id),
    FOREIGN KEY (Report_ID, P_SSN, SSN) REFERENCES Report(Report_ID, P_SSN, SSN)
);

CREATE TABLE Medical_History (
    Hx_ID           INTEGER,
    P_SSN           INTEGER,
    TPAL_total      INTEGER,
    TPAL_preterm    INTEGER,
    TPAL_aborted    INTEGER,
    TPAL_living     INTEGER,
    PRIMARY KEY (Hx_ID, P_SSN),
    FOREIGN KEY (P_SSN) REFERENCES Patient(P_SSN)
);

CREATE TABLE Allergies (
    Hx_ID           INTEGER,
    P_SSN           INTEGER,
    Allergy         TEXT,
    PRIMARY KEY (Hx_ID, P_SSN, Allergy),
    FOREIGN KEY (Hx_ID, P_SSN) REFERENCES Medical_History(Hx_ID, P_SSN)
);

CREATE TABLE Immunization (
    Hx_ID           INTEGER,
    P_SSN           INTEGER,
    Immunization    TEXT,
    PRIMARY KEY (Hx_ID, P_SSN, Immunization),
    FOREIGN KEY (Hx_ID, P_SSN) REFERENCES Medical_History(Hx_ID, P_SSN)
);

CREATE TABLE Treatment_Done (
    Hx_ID           INTEGER,
    P_SSN           INTEGER,
    Med_id          INTEGER,
    Illness_id      INTEGER,
    Date            TEXT,
    PRIMARY KEY (Hx_ID, P_SSN, Med_id, Illness_id),
    FOREIGN KEY (Hx_ID, P_SSN) REFERENCES Medical_History(Hx_ID, P_SSN),
    FOREIGN KEY (Med_id) REFERENCES Medication(Med_id),
    FOREIGN KEY (Illness_id) REFERENCES Illness(Illness_id)
);

CREATE TABLE Past_Illnesses (
    Hx_ID           INTEGER,
    P_SSN           INTEGER,
    Illness_id      INTEGER,
    Age_of_onset    INTEGER,
    PRIMARY KEY (Hx_ID, P_SSN, Illness_id),
    FOREIGN KEY (Hx_ID, P_SSN) REFERENCES Medical_History(Hx_ID, P_SSN),
    FOREIGN KEY (Illness_id) REFERENCES Illness(Illness_id)
);