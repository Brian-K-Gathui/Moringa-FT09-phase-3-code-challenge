from database.connection import get_db_connection

class Author:
    """
    Represents an author in the system, who can write multiple articles.
    """

    def __init__(self, id, name):
        """
        Initialize an Author instance and save it to the database if it doesn't already exist.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")

        self._id = id
        self._name = name

        # Save the author to the database if it doesn't already exist
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        existing_author = cursor.fetchone()

        if not existing_author:
            cursor.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (id, name))
            connection.commit()

        connection.close()

    @property
    def id(self):
        """Get the ID of the author."""
        return self._id

    @property
    def name(self):
        """Get the name of the author."""
        return self._name

    def articles(self):
        """
        Retrieve all articles written by this author.
        Returns a list of Article instances.
        """
        from models.article import Article  # Lazy import to avoid circular dependency
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        articles = [Article(row["id"], row["title"], row["content"], row["author_id"], row["magazine_id"]) for row in cursor.fetchall()]
        connection.close()
        return articles

    def magazines(self):
        """
        Retrieve all magazines associated with this author through their articles.
        Returns a list of Magazine instances.
        """
        from models.magazine import Magazine  # Lazy import to avoid circular dependency
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        SELECT DISTINCT m.* FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        WHERE a.author_id = ?
        """
        cursor.execute(query, (self._id,))
        magazines = [Magazine(row["id"], row["name"], row["category"]) for row in cursor.fetchall()]
        connection.close()
        return magazines

    def __repr__(self):
        """Return the name of the Author."""
        return self._name
