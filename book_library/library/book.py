from dataclasses import dataclass, field
from library.random_number_utils import RandomUtils

@dataclass(frozen=True,order=True, slots=True)
class Book:
    title: str
    author: str
    genre: str
    _rating: float = 0.0
    id: str = field(default_factory=RandomUtils.generate_random_book_id)

    @property
    def rating(self):
        """
        Returns the rating of the book.
        """
        return round(self._rating, 2)
    
    @property
    def search_string(self):
        """
        Returns a string representation of the book for searching.
        """
        return f"{self.title} {self.author} {self.genre}"