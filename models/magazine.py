from database.connection import get_db_connection

class Magazine:
    """
    Represents a magazine that contains multiple articles.
    """

    def __init__(self, id, name, category):
        """
        Initialize a Magazine instance and save it to the database if it doesn't already exist.
        """
        if not (isinstance(name, str) and 2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string.")

        self._id = id
        self._name = name
        self._category = category

        # Save the magazine to the database if it doesn't already exist
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        existing_magazine = cursor.fetchone()

        if not existing_magazine:
            cursor.execute("INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)", (id, name, category))
            connection.commit()

        connection.close()

    @property
    def id(self):
        """Get the ID of the magazine."""
        return self._id

    @property
    def name(self):
        """Get the name of the magazine."""
        return self._name

    @property
    def category(self):
        """Get the category of the magazine."""
        return self._category

    def articles(self):
        """
        Retrieve all articles associated with this magazine.
        Returns a list of Article instances.
        """
        from models.article import Article  # Lazy import to avoid circular dependency
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self._id,))
        articles = [Article(row["id"], row["title"], row["content"], row["author_id"], row["magazine_id"]) for row in cursor.fetchall()]
        connection.close()
        return articles

    def contributors(self):
        """
        Retrieve all authors who have contributed to this magazine.
        Returns a list of Author instances.
        """
        from models.author import Author  # Lazy import to avoid circular dependency
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        SELECT DISTINCT a.* FROM authors a
        JOIN articles ar ON a.id = ar.author_id
        WHERE ar.magazine_id = ?
        """
        cursor.execute(query, (self._id,))
        authors = [Author(row["id"], row["name"]) for row in cursor.fetchall()]
        connection.close()
        return authors

    def article_titles(self):
        """
        Retrieve the titles of all articles in this magazine.
        """
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self._id,))
        titles = [row["title"] for row in cursor.fetchall()]
        connection.close()
        return titles

    def contributing_authors(self):
        """
        Retrieve authors who have written more than 2 articles for this magazine.
        Returns a list of Author instances.
        """
        from models.author import Author  # Lazy import to avoid circular dependency
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        SELECT a.* FROM authors a
        JOIN articles ar ON a.id = ar.author_id
        WHERE ar.magazine_id = ?
        GROUP BY a.id
        HAVING COUNT(ar.id) > 2
        """
        cursor.execute(query, (self._id,))
        authors = [Author(row["id"], row["name"]) for row in cursor.fetchall()]
        connection.close()
        return authors

    def __repr__(self):
        """Return the name of the Magazine."""
        return self._name
