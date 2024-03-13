from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List, Union
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


# class Database:

#     def __init__(
#         self,
#         mongodb_host: str,
#         mongodb_port: int,
#         db_name: str,
#         collection_name: Collection,
#     ) -> None:
#         self.mongodb_host = mongodb_host
#         self.mongodb_port = mongodb_port
#         self.db_name = db_name
#         self.collection_name = collection_name

#     def connect_to_mongodb(self) -> Database:
#         client = MongoClient(self.mongodb_host, self.mongodb_port)
#         database = client[self.db_name]
#         return database

#     def insert_document(self, collection: Collection, document: Dict) -> str:
#         result = collection.insert_one(document)
#         print(f"Printed result: {result}")

#     def find_documents(self, collection: Collection, query: Dict) -> List[Dict]:
#         results = collection.find(query)
#         print("Matching documents:")
#         for result in results:
#             print(result)

#     def update_document(collection: Collection, query: Dict, update: Dict) -> int:
#         result = collection.update_many(query, {"$set": update})

#     def delete_documents(collection: Collection, query: Dict) -> int:
#         result = collection.delete_many(query)
#         return result.deleted_count

#     @staticmethod
#     def filter_by_equals(
#         collection: Collection,
#         field_name: str,
#         value: Union[str, int, float, bool],
#         parameter: Dict = {},
#     ) -> List[dict]:
#         query = {field_name: {"$eq": value}}
#         result = collection.find(query, parameter)
#         return list(result)

#     @staticmethod
#     def filter_by_not_equals(
#         collection: Collection,
#         field_name: str,
#         value: Union[str, int, float, bool],
#         parameter: Dict = {},
#     ) -> List[dict]:
#         query = {field_name: {"$ne": value}}
#         result = collection.find(query, parameter)
#         return list(result)

#     @staticmethod
#     def filter_by_greater_than(
#         collection: Collection,
#         field_name: str,
#         value: Union[str, int, float, bool],
#         parameter: Dict = {},
#     ) -> List[dict]:
#         query = {field_name: {"$gt": value}}
#         result = collection.find(query, parameter)
#         return list(result)

#     @staticmethod
#     def filter_by_less_than(
#         collection: Collection,
#         field_name: str,
#         value: Union[str, int, float, bool],
#         parameter: Dict = {},
#     ) -> List[dict]:
#         query = {field_name: {"$lt": value}}
#         result = collection.find(query, parameter)
#         return list(result)

#     @staticmethod
#     def filter_by_greater_than_equal(
#         collection: Collection,
#         field_name: str,
#         value: Union[str, int, float, bool],
#         parameter: Dict = {},
#     ) -> List[dict]:
#         query = {field_name: {"$gte": value}}
#         result = collection.find(query, parameter)
#         return list(result)

#     @staticmethod
#     def filter_by_less_than_equal(
#         collection: Collection,
#         field_name: str,
#         value: Union[str, int, float, bool],
#         parameter: Dict = {},
#     ) -> List[dict]:
#         query = {field_name: {"$lte": value}}
#         result = collection.find(query, parameter)
#         return list(result)

#     @staticmethod
#     def filter_by_in(
#         collection: Collection, field_name: str, values: List[str], parameter: Dict = {}
#     ) -> List[dict]:
#         query = {field_name: {"$in": values}}
#         result = collection.find(query, parameter)
#         return list(result)

#     @staticmethod
#     def filter_by_not_in(
#         collection: Collection, field_name: str, values: List[str], parameter: Dict = {}
#     ) -> List[dict]:
#         query = {field_name: {"$nin": values}}
#         result = collection.find(query, parameter)
#         return list(result)


# document = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}

# if __name__ == "__main__":
#     people_db = Database(
#         mongodb_host="localhost",
#         mongodb_port=27017,
#         db_name="Peoplee",
#         collection_name="employeees",
#     )
#     new_db = people_db.connect_to_mongodb()
#     collection = new_db[people_db.collection_name]
#     # print(collection)
#     # people_db.insert_document(collection, document)
#     # query = {"name": "John Doe"}
#     # people_db.find_documents(collection, query)
#     # print(
#     #     people_db.filter_by_equals(
#     #         collection, field_name="name", value="Ryan", parameter={"_id": 0}
#     #     )
#     # )
#     print(
#         people_db.filter_by_not_in(collection, "name", ["Ryan"], parameter={"_id": 0})
#     )


import datetime
from random import randint
from faker import Faker
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Dict, List, Union


class MongoDB:
    def __init__(
        self, host: str, port: int, db_name: str, collection_name: str
    ) -> None:
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def find_documents(self, query: Dict) -> List[Dict]:
        documents = self.collection.find(query)
        return list(documents)

    def update_one_document(self, query: Dict, update: Dict) -> int:
        result = self.collection.update_one(query, {"$set": update})
        return result.modified_count

    def update_many_document(self, query: Dict, update: Dict) -> int:
        result = self.collection.update_many(query, {"$set": update})
        return result.modified_count

    def delete_one_documents(self, query: Dict) -> int:
        result = self.collection.delete_one(query)
        return result.deleted_count

    def delete_many_documents(self, query: Dict) -> int:
        result = self.collection.delete_many(query)
        return result.deleted_count

    def insert_one_document(self, document: Dict) -> str:
        result = self.collection.insert_one(document)
        print(f"Printed result: {result}")
        return str(result.inserted_id)

    def insert_many_document(self, document: Dict) -> List[str]:
        result = self.collection.insert_many(document)
        print(f"Printed result: {result}")
        return list(result.inserted_ids)

    def create_random_person(self) -> str:
        fake = Faker()
        name = fake.first_name()
        surname = fake.last_name()
        age = randint(18, 65)
        now = datetime.datetime.now()
        year_salary = randint(15000, 25000)

        document = {
            "name": name,
            "surname": surname,
            "age": age,
            "salary": year_salary,
        }
        result = self.collection.insert_one(document)
        print(f"Inserted document with ID: {result.inserted_id}")
        print(f"This person was inserted into the database: {document}")

        return str(result.inserted_id)

    def generate_data_base(self, numb_of_documents):
        for _ in range(numb_of_documents):
            self.create_random_person()

    def query_equal(
        self, field_name: str, value: Union[str, int, float, bool], parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$eq": value}}
        result = self.collection.find(query, parameter)
        return list(result)

    def query_greater_than(
        self, field_name: str, value: Union[str, int, float, bool], parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$gt": value}}
        result = self.collection.find(query, parameter)
        return list(result)

    def query_greater_than_or_equal(
        self, field_name: str, value: Union[str, int, float, bool], parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$gte": value}}
        result = self.collection.find(query, parameter)
        return list(result)

    def query_in_array(
        self, field_name: str, value: List, parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$in": value}}
        result = self.collection.find(query, parameter)
        return list(result)

    def query_less_than(
        self, field_name: str, value: Union[str, int, float, bool], parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$lt": value}}
        result = self.collection.find(query, parameter)
        return list(result)

    def query_less_than_or_equal(
        self, field_name: str, value: Union[str, int, float, bool], parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$lte": value}}
        result = self.collection.find(query, parameter)
        return list(result)

    def query_not_equal(
        self, field_name: str, value: Union[str, int, float, bool], parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$ne": value}}
        result = self.collection.find(query, parameter)
        return list(result)

    def query_not_in_array(
        self, field_name: str, value: List, parameter: Dict = {}
    ) -> List[dict]:
        query = {field_name: {"$nin": value}}
        result = self.collection.find(query, parameter)
        return list(result)


if __name__ == "__main__":
    mongodb = MongoDB(
        host="localhost",
        port=27017,
        db_name="workers",
        collection_name="employees_salary",
    )
