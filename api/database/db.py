from os import path
import sqlite3

DB_PATH = "database.db"
POPULATE_FILE = "populate.sql"

connection = None
cursor = None


def init_db():
    """Connect to the database and create the database cursor.
    """
    # If there is no database, connect and populate it.
    if not path.exists(DB_PATH):
        connect_db()
        populate_db()

    # Otherwise, just connect.
    else:
        connect_db()


def connect_db():
    """Connect to the database.
    """
    global connection, cursor

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()


def populate_db():
    """Creates and populates a new database.
    Called if one does not exist.
    """
    full_path = path.dirname(path.abspath(__file__)) + "/" + POPULATE_FILE

    if not path.exists(full_path):
        exit("Populate file does not exist.")

    with open(full_path, "r") as fp:
        cursor.executescript(fp.read())
