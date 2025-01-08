from database.connection import get_db_connection

class Article:
    """
    Represents an article written by an author for a magazine.
    """

    def __init__(self, id, title, content, author_id, magazine_id):
        """
        Initialize an Article instance and save it to the database if it doesn't already exist.
        """
        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

        # Save the article to the database if it doesn't already exist
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        existing_article = cursor.fetchone()

        if not existing_article:
            cursor.execute("""
                INSERT INTO articles (id, title, content, author_id, magazine_id)
                VALUES (?, ?, ?, ?, ?)
            """, (id, title, content, author_id, magazine_id))
            connection.commit()

        connection.close()

    @property
    def id(self):
        """
        Get the ID of the article.
        """
        return self._id

    @property
    def title(self):
        """
        Get the title of the article.
        """
        return self._title

    @property
    def author(self):
        """
        Retrieve the author of this article.
        """
        from models.author import Author  # Lazy import to avoid circular dependency
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (self._author_id,))
        row = cursor.fetchone()
        connection.close()
        return Author(row["id"], row["name"]) if row else None

    @property
    def magazine(self):
        """
        Retrieve the magazine of this article.
        """
        from models.magazine import Magazine  # Lazy import to avoid circular dependency
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (self._magazine_id,))
        row = cursor.fetchone()
        connection.close()
        return Magazine(row["id"], row["name"], row["category"]) if row else None

    def __repr__(self):
        """
        Return the title of the Article.
        """
        return self._title


