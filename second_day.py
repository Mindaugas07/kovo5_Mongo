from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


# def find_documents(collection: Collection, query: Dict) -> List[Dict]:
#     documents = collection.find(query)
#     return list(documents)


# # Example usage
# if __name__ == "__main__":
#     # Connection details
#     mongodb_host = "localhost"
#     mongodb_port = 27017
#     database_name = "people"
#     collection_name = "employees"

#     # Connect to MongoDB
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     # Retrieve a specific collection
#     collection = db[collection_name]

#     # Read (Query) Operation
#     query = {"name": "descriptive-cabinet"}
#     results = find_documents(collection, query)
#     print("Matching documents:")
#     for result in results:
#         print(result)


# def update_document(collection: Collection, query: Dict, update: Dict) -> int:
#     result = collection.update_many(query, {"$set": update})
#     return result.modified_count

# # Example usage
# if __name__ == "__main__":
#     # Connection details
#     mongodb_host = 'localhost'
#     mongodb_port = 27017
#     database_name = 'people'
#     collection_name = 'employees'

#     # Connect to MongoDB
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     # Retrieve a specific collection
#     collection = db[collection_name]

#     # Update Operation
#     query = {"name": "descriptive-cabinet"}
#     update = {"age": 35}
#     modified_count = update_document(collection, query, update)
#     print(f"Modified {modified_count} documents")


def delete_documents(collection: Collection, query: Dict) -> int:
    result = collection.delete_many(query)
    return result.deleted_count


# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "people"
    collection_name = "employees"

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    # Delete Operation
    query = {"name": "rude-compass", "id": "65e89f1d3624d40e6e761270"}
    deleted_count = delete_documents(collection, query)
    print(f"Deleted {deleted_count} documents")
