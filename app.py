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
        Author("John Doe"),
        Author("Jane Smith"),
        Author("Albert Einstein"),
        Author("Isaac Newton"),
        Author("Marie Curie"),
        Author("Ada Lovelace"),
        Author("Nikola Tesla"),
        Author("Elon Musk"),
        Author("Stephen Hawking"),
        Author("Rosalind Franklin"),
    ]
    magazines = [
        Magazine("Tech Weekly", "Technology"),
        Magazine("Health Monthly", "Health"),
        Magazine("Science Digest", "Science"),
        Magazine("History Guide", "History"),
        Magazine("Innovator's Hub", "Innovation"),
        Magazine("Quantum Times", "Quantum Physics"),
        Magazine("Future Trends", "Futurism"),
        Magazine("Medical News", "Medicine"),
        Magazine("Coding Today", "Programming"),
        Magazine("Electric News", "Electricity"),
    ]
    articles = [
        Article("The Future of AI", "AI is evolving rapidly.", authors[0].id, magazines[0].id),
        Article("Tech in 2025", "Upcoming technology trends.", authors[0].id, magazines[0].id),
        Article("The Impact of AI", "How AI is changing industries.", authors[0].id, magazines[0].id),
        Article("Programming in 2030", "The future of coding languages.", authors[1].id, magazines[0].id),
        Article("Tech Startups to Watch", "Top startups in technology.", authors[1].id, magazines[0].id),
        Article("Innovations in Robotics", "Robots in everyday life.", authors[1].id, magazines[0].id),
        Article("Quantum Computers in Tech", "Quantum tech applications.", authors[2].id, magazines[0].id),
        Article("Big Data Explained", "Understanding big data.", authors[2].id, magazines[0].id),
        Article("Cybersecurity Trends", "How to stay safe online.", authors[2].id, magazines[0].id),
        Article("Health in 2025", "Health trends to watch out for.", authors[3].id, magazines[1].id),
        Article("Women in Science", "Highlighting women in science.", authors[4].id, magazines[2].id),
        Article("The History of Computers", "Tracing the evolution of computers.", authors[5].id, magazines[3].id),
        Article("The Power of Nikola Tesla", "Exploring Tesla's contributions.", authors[6].id, magazines[9].id),
        Article("Space Exploration in 2030", "What's next for space exploration?", authors[7].id, magazines[6].id),
        Article("Black Holes Decoded", "Understanding the mysteries of black holes.", authors[8].id, magazines[5].id),
        Article("DNA and the Double Helix", "The discovery that changed biology.", authors[9].id, magazines[2].id),
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
