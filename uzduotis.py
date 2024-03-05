# Create a CLI application that takes name surname gender and age (in a single sentence).
# Check if gender or age is provided correctly. Result save to database with timestamp of the event.
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict
import os
from datetime import datetime


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    return str(result.inserted_id)


if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "User"
    collection_name = "Personal information"

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    # Create (Insert) Operation
    while True:
        try:
            user_input = input("Please enter your name, surname, gender and age: ")
            input_list = user_input.split(" ")
            break
        except:
            print("Wrong input.")
            break

    document = {
        "name": input_list[0],
        "surname": input_list[1],
        "gender": input_list[2],
        "age": input_list[3],
        "timestamp": datetime.now(),
    }

    if (document["gender"] == "male" or document["gender"] == "female") and 0 < int(
        document["age"]
    ) < 150:
        inserted_id = insert_document(collection, document)
        print(f"Inserted document with ID: {inserted_id}")
    else:
        print("You entered wrong gender or age!")
