from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List
from faker import Faker
from random import randint


# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database


# def insert_document(collection: Collection, document: Dict) -> str:
#     result = collection.insert_one(document)
#     print(f"Printed result: {result}")
#     return str(result.inserted_id)


# def create_a_person():
#     fake = Faker()
#     name = fake.first_name()
#     surname = fake.last_name()
#     age = randint(18, 75)
#     years_employed = (
#         -1
#     )  # Cannot use zero, as it is a valid value, can't use None, as it wont work
#     while age - 18 < years_employed or years_employed == -1:
#         years_employed = randint(0, 55)
#     return name, surname, age, years_employed


# if __name__ == "__main__":
#     mongodb_host = "localhost"
#     mongodb_port = 27017
#     database_name = "Peoplee"
#     collection_name = "employeees"

#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     collection = db[collection_name]
#     fake = Faker()
#     for _ in range(10):
#         name, surname, age, years_employed = create_a_person()
#         document = {
#             "name": name,
#             "surname": surname,
#             "age": age,
#             "years_employed": years_employed,
#         }
#         inserted_id = insert_document(collection, document)
#         print(f"Inserted document with ID: {inserted_id}")
#         print(f"This person was inserted into the database: {document}")

# Create a class that would repsresent all basic CRUD operations with MongoDB.


class Database:
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017

    def __init__(self, db_name: str, collection_name: Collection) -> None:
        self.db_name = db_name
        self.collection_name = collection_name

    def connect_to_mongodb(self) -> Database:
        client = MongoClient(Database.MONGODB_HOST, Database.MONGODB_PORT)
        database = client[self.db_name]
        return database

    def insert_document(self, collection: Collection, document: Dict) -> str:
        result = collection.insert_one(document)
        print(f"Printed result: {result}")

    def find_documents(self, collection: Collection, query: Dict) -> List[Dict]:
        results = collection.find(query)
        print("Matching documents:")
        for result in results:
            print(result)

    def update_document(collection: Collection, query: Dict, update: Dict) -> int:
        result = collection.update_many(query, {"$set": update})

    def delete_documents(collection: Collection, query: Dict) -> int:
        result = collection.delete_many(query)
        return result.deleted_count


document = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}

if __name__ == "__main__":
    people_db = Database(db_name="Peoplee", collection_name="employeees")
    new_db = people_db.connect_to_mongodb()
    collection = new_db[people_db.collection_name]
    print(collection)
    people_db.insert_document(collection, document)
    query = {"name": "John Doe"}
    people_db.find_documents(collection, query)
