import pytest
from library.library import Library
from library.book import Book

@pytest.fixture
def library():
    database = "./test/test_database.json"
    lib = Library(database)
    lib.empty_library()
    return lib

def test_add_and_total_books(library):
    book1 = Book("1984", "George Orwell", "Dystopian", 4.5)
    book2 = Book("Brave New World", "Aldous Huxley", "Dystopian", 4.2)
    library.add_book(book1)
    library.add_book(book2)
    assert library.get_total_book_count() == 2

def test_empty_library(library):
    book = Book("Test Book", "Test Author", "Test Genre", 3.0)
    library.add_book(book)
    library.empty_library()
    assert len(library.get_all_books()["Books"].items()) == 0

def test_search_book(library):
    book = Book("Dune", "Frank Herbert", "Science Fiction", 4.7)
    library.add_book(book)
    result = library.search_books("dune")
    assert result[0].title.lower() == "dune"

def test_get_all_books(library):
    book1 = Book("Sapiens", "Yuval Noah Harari", "Non-fiction", 4.6)
    book2 = Book("Homo Deus", "Yuval Noah Harari", "Non-fiction", 4.4)
    library.add_book(book1)
    library.add_book(book2)
    data = library.get_all_books()
    titles_to_compare = [book1.title, book2.title]
    results = [item_data["title"] for item_id, item_data in data["Books"].items()]
    assert titles_to_compare == results

def test_get_total_book_count(library):
    book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 4.8)
    book2 = Book("The Silmarillion", "J.R.R. Tolkien", "Fantasy", 4.3)
    library.add_book(book1)
    library.add_book(book2)
    assert library.get_total_book_count() == 2
