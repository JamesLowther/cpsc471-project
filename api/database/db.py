from os import path
import sqlite3

DB_PATH = "database.db"
POPULATE_FILE = "populate.sql"

connection = None
cursor = None

"""
Connect to the database and create the database cursor.
"""
def init_db():
    # If there is no database, connect and populate it.
    if not path.exists(DB_PATH):
        connect_db()
        populate_db()

    # Otherwise, just connect.
    else:
        connect_db()


"""
Connect to the database.
"""
def connect_db():
    global connection, cursor

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

"""
Creates and populates a new database.
Called if one does not exist.
"""
def populate_db():
    full_path = path.dirname(path.abspath(__file__)) + "/" + POPULATE_FILE 

    if not path.exists(full_path):
        exit("Populate file does not exist.")

    with open(full_path, "r") as fp:
        cursor.executescript(fp.read())