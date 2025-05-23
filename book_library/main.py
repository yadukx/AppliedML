from library.book import Book
from library.library import Library

if __name__ == "__main__":

    # Set the path to the database JSON file
    database = "./database.json"
    my_library = Library(database)

    # Search for a book
    print("Searching for a book...")
    results = my_library.search_books("tolkien")
    print("------------------------")

    # Get total number of books in the library
    print("Total books in the library:")
    total_book_count = my_library.get_total_book_count()
    print(f"Total book count: {total_book_count}")
    print("------------------------")

    # Add new books to the library
    print("Adding books to the library:")
    print("------------------------")

    dune = Book("Dune", "Frank Herbert", "Science Fiction", 4.6)
    my_library.add_book(dune)

    # Display all books in the library
    print("------------------------")
    print("Books currently in the library:")
    print("------------------------")
    my_library.get_all_books(verbose=1)
    print("------------------------")

    # Remove books by search query
    query = "hobbit"
    print("Removing books by search query - '" + query + "' : ")
    print("------------------------")
    my_library.remove_books_by_query(query)
    print("------------------------\n")

    # Remove a book by user selection
    print("Removing a specific book by selection:")
    print("------------------------")
    my_library.list_books_for_removal()
    print("------------------------")
    
    # Show remaining books
    print("Current books in the library:")
    my_library.get_all_books(verbose=1)
    print("------------------------")
