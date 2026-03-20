from cassandra.cluster import Cluster

def run_read_activity():
    # 1. Connect to the Cassandra database on port 9042
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()

    # 2. Connect to the books keyspace
    session.set_keyspace('books')

    # 3. Run a query to select all books
    print("Querying all books in the 'books' keyspace...\n")
    rows = session.execute("SELECT * FROM book;")

    # 4. Print each book
    # Note: Column names are case-insensitive in the result set
    for row in rows:
        print(f"ID: {row.book_id} | Title: {row.name} | Author: {row.author} | Year: {row.year_published} | Pages: {row.number_of_pages}")

    cluster.shutdown()

if __name__ == "__main__":
    run_read_activity()