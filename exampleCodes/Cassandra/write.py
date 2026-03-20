from cassandra.cluster import Cluster

def run_write_activity():
    # 1. Connect to the Cassandra database on port 9042
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()

    # 2. Create a new keyspace called 'books'
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS books 
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """)

    # 3. Set the current session to the books keyspace
    session.set_keyspace('books')

    # 4. Create a new table called 'book'
    session.execute("""
        CREATE TABLE IF NOT EXISTS book (
            Book_ID int PRIMARY KEY,
            Name text,
            Author text,
            Year_Published int,
            Number_of_Pages int
        )
    """)

    # 5. Insert the four required rows
    books_to_insert = [
        (1, 'The Mystery of Capital', 'Hernando de Soto', 1970, 209),
        (2, 'Fairy Tales', 'Hans Christian Andersen', 1836, 784),
        (3, 'The Divine Comedy', 'Dante Alighieri', 1315, 928),
        (4, 'Romeo and Juliet', 'William Shakespeare', 1597, 100)
    ]

    query = "INSERT INTO book (Book_ID, Name, Author, Year_Published, Number_of_Pages) VALUES (%s, %s, %s, %s, %s)"

    for book in books_to_insert:
        session.execute(query, book)
        print(f"Inserted: {book[1]}")
        # print(f"") is due to code inside the text
        # book[1] is the name of the book, which is the second element in the tuple (index 1)

    print("\nDatabase setup and data insertion complete!")
    cluster.shutdown()

# Main Guard 
if __name__ == "__main__":
    run_write_activity()
