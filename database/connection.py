import sqlite3

# Define the path to the database file
DATABASE_NAME = './database/database.db'

def get_db_connection():
    """
    Establish and return a connection to the SQLite database.
    Sets the row factory to sqlite3.Row to retrieve rows as dictionaries.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Ensures results are dictionary-like for easier use
    return conn