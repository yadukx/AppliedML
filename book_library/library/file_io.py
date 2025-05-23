import json
import os 
from dataclasses import dataclass, field

@dataclass
class Fstream:
    """
    A class to handle file operations such as reading and writing JSON files.
    """
    name: str
    path: str
    extension: str
    data_file: dict = field(init=False, default_factory=dict)

    @classmethod
    def load_json_file(cls, path:str) -> dict:
         """
        reads JSON data from a file and stores it in the class variable.

        Args:
            path : the path to the JSON file.

        Returns:
            dict: hash map with the JSON content
        """
        
         if not os.path.exists(path):
            cls.data_file = {} #empty dict if file does not exist
            return cls.data_file
         
         with open(path, "r", encoding="utf-8") as data_file:
            cls.data_file = json.load(data_file)
         return cls.data_file
    
    @staticmethod
    def print_json_structure(data_file):
        # Adjust for Books key, not Items
        for book_id, book_data in data_file.get("Books", {}).items():
            print(book_id, book_data)