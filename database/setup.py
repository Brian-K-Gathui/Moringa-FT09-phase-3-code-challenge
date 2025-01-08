import sqlite3

DATABASE_NAME = './database/database.db'

def create_tables():
    """
    Create the database and tables if they do not already exist.
    Ensures the tables are properly created with the necessary relationships.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Drop tables if they already exist (to avoid duplication issues)
    cursor.execute("DROP TABLE IF EXISTS articles")
    cursor.execute("DROP TABLE IF EXISTS authors")
    cursor.execute("DROP TABLE IF EXISTS magazines")

    # Create the 'authors' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    """)

    # Create the 'magazines' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    """)

    # Create the 'articles' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors (id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (id)
    )
    """)

    # Commit changes and close the connection
    connection.commit()
    connection.close()
