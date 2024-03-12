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


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


# def insert_document(collection: Collection, document: Dict) -> str:
#     result = collection.insert_one(document)
#     print(f"Printed result: {result}")
#     return str(result.inserted_id)


def get_database_collection(database: Database, collection_name: str) -> Collection:
    collection = database[collection_name]
    return collection


def create_document() -> Dict:
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


if __name__ == "__main__":
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "numbers"
    collection_name = "letters"

    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)
    collection = db[collection_name]

    # itteration = 1000
    # for _ in range(itteration):
    #     document = create_document()
    #     inserted_id = insert_document(collection, document)
    #     print(f"Inserted document with ID: {inserted_id}")

    collection = get_database_collection(db, collection_name)

    # query = {
    #     "number": {"$eq": 1000},
    # }

    # query = {
    #     "number": {"$gt": 99, "$lt": 10000},
    # }

    # query = {
    #     "number": {"$gt": 9999, "$lt": 1000000},
    # }

    # response = collection.find(query, {"_id": 0})

    # for document in response:
    #     print(document)

    # dominant letter within  five and 6 digits area range.
    # dominant_letter = {}

    # for document in response:
    #     for letter in document["letters"]:
    #         dominant_letter[letter] = dominant_letter.get(letter, 0) + 1

    # print(dominant_letter)

    query = {
        "number": {"$gt": 0},
    }

    response = collection.find(query, {"_id": 0})

    def get_lowest_and_highest_numbers_from_db():
        lowest_number = 1000000
        highest_number = 0
        for document in response:
            if document["number"] < lowest_number:
                lowest_number = document["number"]
            if document["number"] > highest_number:
                highest_number = document["number"]

        return (
            f"Lowest number is {lowest_number} and highest number is {highest_number}"
        )

    print(get_lowest_and_highest_numbers_from_db())
