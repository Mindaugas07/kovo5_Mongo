# Create a python script that would generate a sequence of 1000 random numbers from 1 to 1000000 .
#  A number sequence from 0 to 9 represents letters from A to J.
# (lets say we have 101 = BAB) . All those 1000 values should be written to database (number and it's representation)
# Please find:
# - All documents where number is 100,1000,10000
# - All documents where numbers are at least triple or four digits
# - What is the dominant letter within  five and 6 digits area range.
# - Tell me the sum on numbers where majority letters are : (letter 1, letter 2, letter 3)
# - Show me the lowest and highest number and their representations

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List
from random import randint, randrange

numb_letter_dict = {
    "0": "A",
    "1": "B",
    "2": "C",
    "3": "D",
    "4": "E",
    "5": "F",
    "6": "G",
    "7": "H",
    "8": "I",
    "9": "J",
}


class NumbersLetters:

    def __init__(
        self,
        mongodb_host: str,
        mongodb_port: str,
        db_name: str,
        collection_name: Collection,
    ) -> None:
        self.mongodb_host = mongodb_host
        self.mongodb_port = mongodb_port
        self.db_name = db_name
        self.collection_name = collection_name

    def connect_to_mongodb(self) -> Database:
        client = MongoClient(self.mongodb_host, self.mongodb_port)
        database = client[self.db_name]
        return database

    def insert_document(self, collection: Collection, document: Dict) -> str:
        result = collection.insert_one(document)
        print(f"Printed result: {result}")

    @staticmethod
    def get_database_collection(database: Database, collection_name: str) -> Collection:
        collection = database[collection_name]
        return collection

    @staticmethod
    def create_document(numb_letter_dict) -> Dict:
        letter_string = ""
        digit_letter_dict = {}
        number = randint(1, 1000000)
        number_list = [digit for digit in str(number)]
        for element in number_list:
            letter = numb_letter_dict[element]
            letter_string += letter
        digit_letter_dict[number] = letter_string
        letter_string = ""

        return {
            "number": number,
            "letters": digit_letter_dict[number],
        }

    def insert_several_documents(self, document_amount: int) -> None:
        for _ in range(document_amount):
            document = self.create_document(numb_letter_dict)
            inserted_id = self.insert_document(collection, document)
            print(f"Inserted document with ID: {inserted_id}")

    def get_documents_with_specific_number(
        self, number: int, collection: Collection
    ) -> Dict:
        query = {
            "number": {"$eq": number},
        }
        response = collection.find(query, {"_id": 0})
        for document in response:
            print(document)

    def get_documents_with_triple_four_digits(self, collection: Collection) -> Dict:
        query = {
            "number": {"$gt": 99, "$lt": 10000},
        }
        response = collection.find(query, {"_id": 0})
        for document in response:
            print(document)

    def dominant_letter_in_document(self, collection: Collection) -> Dict:
        query = {
            "number": {"$gt": 9999, "$lt": 1000000},
        }
        response = collection.find(query, {"_id": 0})
        dominant_letters = {}
        for document in response:
            for letter in document["letters"]:
                dominant_letters[letter] = dominant_letters.get(letter, 0) + 1

        dominant_letter = max(dominant_letters, key=dominant_letters.get)
        print(f"Dominant letter in documents is {dominant_letter}")

    def low_high_and_represented_letters(self, collection: Collection) -> Dict:
        query = {
            "number": {"$gt": 0},
        }
        response = collection.find(query, {"_id": 0})
        lowest_number = 1000000
        highest_number = 0
        for document in response:
            if document["number"] < lowest_number:
                lowest_number = document["number"]
            if document["number"] > highest_number:
                highest_number = document["number"]

        print(
            f"Lowest number is {lowest_number} and highest number is {highest_number}"
        )


if __name__ == "__main__":
    number_letters = NumbersLetters(
        mongodb_host="localhost",
        mongodb_port=27017,
        db_name="numbers2",
        collection_name="letters2",
    )

    db = number_letters.connect_to_mongodb()
    collection = db[number_letters.collection_name]

    # number_letters.insert_several_documents(1000)

    collection = number_letters.get_database_collection(
        db, number_letters.collection_name
    )

    # - All documents where number is 100,1000,10000
    # number_letters.get_documents_with_specific_number(100, collection)
    # number_letters.get_documents_with_specific_number(1000, collection)
    # number_letters.get_documents_with_specific_number(1000, collection)

    # - All documents where numbers are at least triple or four digits
    # number_letters.get_documents_with_triple_four_digits(collection)

    # - What is the dominant letter within  five and 6 digits area range.
    # number_letters.dominant_letter_in_document(collection)

    # - Tell me the sum on numbers where majority letters are : (letter 1, letter 2, letter 3)
    # xxx

    # - Show me the lowest and highest number and their representations
    # number_letters.low_high_and_represented_letters(collection)
