from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb+srv://katerynapomazunova:Dk12345678@cluster0.4koqews.mongodb.net")

    db = client.hw10
    return db