from os import path
import sqlite3

DB_PATH = "database.db"
SCHEMA_FILE = "schema.sql"

TEST_DATA_FILE = "test-data.sql"
USE_TEST_DATA = True

def init_db():
    """Connect to the database and create the database cursor.
    """
    # If there is no database, connect and populate it.
    if not path.exists(DB_PATH):
        populate_db()


def connect_db():
    """Connect to the database.
    Call this to get the cursor when you need to access the database.
    """

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return (connection, connection.cursor())


def populate_db():
    """Creates and populates a new database.
    Called if one does not exist.
    """
    full_path = path.dirname(path.abspath(__file__)) + "/" + SCHEMA_FILE

    if not path.exists(full_path):
        exit("Populate file does not exist.")

    con, cursor = connect_db()

    with open(full_path, "r") as fp:
        cursor.executescript(fp.read())

    # Optionally populate the database with test data.
    if USE_TEST_DATA:
        test_data_path = path.dirname(path.abspath(__file__)) + "/" + TEST_DATA_FILE
        with open(test_data_path, "r") as fp:
            cursor.executescript(fp.read())

    con.commit()
    con.close()
        
