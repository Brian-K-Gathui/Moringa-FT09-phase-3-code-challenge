import unittest
from database.setup import create_tables
from database.connection import get_db_connection
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the in-memory database for testing.
        """
        cls.connection = get_db_connection()
        create_tables()

    def test_author_creation(self):
        """
        Test creating an author and retrieving its properties.
        """
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        """
        Test creating an article and retrieving its title.
        """
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        """
        Test creating a magazine and retrieving its name.
        """
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the in-memory database.
        """
        cls.connection.close()

if __name__ == "__main__":
    unittest.main()
