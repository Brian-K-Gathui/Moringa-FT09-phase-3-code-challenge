from database.setup import create_tables
from models.author import Author
from models.article import Article
from models.magazine import Magazine

def main():
    """
    Main entry point for the application.
    Demonstrates expanded sample data and relationships.
    """
    print("\n")
    print("=" * 40)
    print("WELCOME TO THE DATABASE DEMONSTRATION")
    print("=" * 40)
    
    # Step 1: Setting up the database
    print("\n")
    print("-" * 40)
    print("Step 1: Setting up the database...")
    print("-" * 40)
    create_tables()
    print("Database setup complete.")
    
    # Step 2: Generating sample data
    print("\n")
    print("-" * 40)
    print("Step 2: Generating sample data...")
    print("-" * 40)
    authors = [
        Author(1, "John Doe"),
        Author(2, "Jane Smith"),
        Author(3, "Albert Einstein"),
        Author(4, "Isaac Newton"),
        Author(5, "Marie Curie"),
        Author(6, "Ada Lovelace"),
        Author(7, "Nikola Tesla"),
        Author(8, "Elon Musk"),
        Author(9, "Stephen Hawking"),
        Author(10, "Rosalind Franklin"),
    ]
    magazines = [
        Magazine(1, "Tech Weekly", "Technology"),
        Magazine(2, "Health Monthly", "Health"),
        Magazine(3, "Science Digest", "Science"),
        Magazine(4, "History Guide", "History"),
        Magazine(5, "Innovator's Hub", "Innovation"),
        Magazine(6, "Quantum Times", "Quantum Physics"),
        Magazine(7, "Future Trends", "Futurism"),
        Magazine(8, "Medical News", "Medicine"),
        Magazine(9, "Coding Today", "Programming"),
        Magazine(10, "Electric News", "Electricity"),
    ]
    articles = [
        Article(1, "The Future of AI", "AI is evolving rapidly.", 1, 1),
        Article(2, "Tech in 2025", "Upcoming technology trends.", 1, 1),
        Article(3, "The Impact of AI", "How AI is changing industries.", 1, 1),
        Article(4, "Programming in 2030", "The future of coding languages.", 2, 1),
        Article(5, "Tech Startups to Watch", "Top startups in technology.", 2, 1),
        Article(6, "Innovations in Robotics", "Robots in everyday life.", 2, 1),
        Article(7, "Quantum Computers in Tech", "Quantum tech applications.", 3, 1),
        Article(8, "Big Data Explained", "Understanding big data.", 3, 1),
        Article(9, "Cybersecurity Trends", "How to stay safe online.", 3, 1),
        Article(10, "Health in 2025", "Health trends to watch out for.", 4, 2),
        Article(11, "Women in Science", "Highlighting women in science.", 5, 3),
        Article(12, "The History of Computers", "Tracing the evolution of computers.", 6, 4),
        Article(13, "The Power of Nikola Tesla", "Exploring Tesla's contributions.", 7, 10),
        Article(14, "Space Exploration in 2030", "What's next for space exploration?", 8, 7),
        Article(15, "Black Holes Decoded", "Understanding the mysteries of black holes.", 9, 6),
        Article(16, "DNA and the Double Helix", "The discovery that changed biology.", 10, 3),
    ]
    print("Sample data generation complete.")
    
    # Step 3: Displaying generated data
    print("\n")
    print("-" * 40)
    print("Step 3: Displaying generated data...")
    print("-" * 40)
    print("Authors:")
    for author in authors:
        print(f"  - {author}")
    print("\nMagazines:")
    for magazine in magazines:
        print(f"  - {magazine}")
    print("\nArticles:")
    for article in articles:
        print(f"  - {article}")
    
    # Step 4: Demonstrating relationships
    print("\n")
    print("-" * 40)
    print("Step 4: Demonstrating relationships...")
    print("-" * 40)
    print(f"Contributors for {magazines[0].name}:")
    for contributor in magazines[0].contributors():
        print(f"  - {contributor}")
    print("\nArticle Titles in Tech Weekly:")
    print(f"{', '.join(magazines[0].article_titles())}")
    print("\nContributing Authors with More Than 2 Articles in Tech Weekly:")
    for author in magazines[0].contributing_authors():
        print(f"  - {author}")
    
    print("\n" + "=" * 40)
    print("APPLICATION RUN SUCCESSFULLY")
    print("=" * 40)
    print("\n")

if __name__ == "__main__":
    main()