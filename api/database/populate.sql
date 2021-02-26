PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    uid             text,
    username        text,
    password        text,
    PRIMARY KEY (uid)
);