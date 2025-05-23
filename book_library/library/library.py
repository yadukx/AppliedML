# library/library.py

import json
from dataclasses import dataclass, field
from library.book import Book
from library.random_number_utils import RandomUtils
from library.file_io import Fstream

@dataclass
class Library:
    database_path: str
    isEmpty: bool = True
    isActive: bool = False
    id: str = field(init=False, default_factory=RandomUtils.generate_random_book_id)

    def get_all_books(self, verbose=0) -> dict:
        """
        Reads and returns a dictionary of all books in the library

        Args:
            verbose (int): If set to 1 it prints all books

        Returns:
            dict: All books loaded from JSON database
        """
        data_file = Fstream.load_json_file(self.database_path)

        if len(data_file["Books"].items()) > 0:
            self.isEmpty = False
            self.isActive = True

        if verbose == 1:
            Fstream.print_json_structure(data_file)
            return data_file
        else:
            return data_file

    def add_book(self, book: Book):
        """
        Adds a new book to the library and writes to database

        Args:
            book (Book): Book object to add
        """
        data = self.get_all_books()

        new_book = {
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "rating": book.rating
        }

        data["Books"][book.id] = new_book

        with open(self.database_path, 'w') as file:
            json.dump(data, file, indent=4)

        self.isEmpty = False
        self.isActive = True
        print(f"Added book: {book.title} by {book.author}")

    def search_books(self, query: str) -> list[Book]:
        """
        Searches books by title, author, or genre

        Args:
            query (str): Search string

        Returns:
            list[Book]: List of matching books
        """
        data = self.get_all_books()
        matching_books = []

        for book_id, book_data in data["Books"].items():
            book = Book(
                title=book_data["title"],
                author=book_data["author"],
                genre=book_data["genre"],
                _rating=book_data["rating"],
                id=book_id
            )
            if query.lower() in book.search_string.lower():
                matching_books.append(book)

        if not matching_books:
            print("No books found.")
        else:
            for book in matching_books:
                print(f"Found: {book.title} by {book.author} [{book.genre}] Rating: {book.rating}")

        return matching_books

    def remove_books_by_query(self, query: str):
        """
        Removes all books matching the query

        Args:
            query (str): Search string to match books
        """
        data = self.get_all_books()
        books_to_remove = []

        for book_id, book_data in data["Books"].items():
            if query.lower() in book_data["title"].lower() or query.lower() in book_data["author"].lower():
                books_to_remove.append(book_id)

        if not books_to_remove:
            print(f"No books found matching '{query}'")
            return

        for book_id in books_to_remove:
            title = data["Books"][book_id]["title"]
            del data["Books"][book_id]
            print(f"Removed: {title}")

        with open(self.database_path, 'w') as file:
            json.dump(data, file, indent=4)

        if not data["Books"]:
            self.isEmpty = True
            self.isActive = False

    def list_books_for_removal(self):
        """
        Lists books and removes one based on user selection
        """
        data = self.get_all_books()
        books = list(data["Books"].items())

        for i, (book_id, book_data) in enumerate(books, 1):
            print(f"{i}: {book_data['title']} by {book_data['author']}")

        try:
            usr_choice = int(input("Select the book to delete by number: ")) - 1
        except:
            raise ValueError("You must select a valid number!")

        if usr_choice >= len(books) or usr_choice < 0:
            print("Invalid selection.")
            return

        book_id = books[usr_choice][0]
        title = data["Books"][book_id]["title"]
        del data["Books"][book_id]
        print(f"Removed: {title}")

        with open(self.database_path, 'w') as file:
            json.dump(data, file, indent=4)

        if not data["Books"]:
            self.isEmpty = True
            self.isActive = False

    def get_total_book_count(self) -> int:
        """
        Returns the total number of books in the library

        Returns:
            int: Total count of books
        """
        data = self.get_all_books()
        return len(data["Books"].items())

    def empty_library(self):
        """
        Clears all books from the library
        """
        data = self.get_all_books()
        if len(data["Books"].items()) > 0:
            data = {"Books": {}}

            with open(self.database_path, 'w') as file:
                json.dump(data, file, indent=4)

            self.isEmpty = True
            self.isActive = False
            print("Library is now empty.")
        else:
            print("Library is already empty.")
