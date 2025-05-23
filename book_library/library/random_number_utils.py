import random
import string

class RandomUtils:
    """
    Class for generation of random numbers
    """
    @staticmethod
    def generate_random_book_id(length: int = 8) -> str:
        """
        Generates a random alphanumeric ID of a given length (default: 8).
        used as a ISBN or a book id

        Returns:
            str: A random ID made of uppercase letters and digits.       
        """
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=length))
