import pymongo
from pymongo import MongoClient
from pymongo import errors

client = MongoClient("mongodb+srv://admin:admin123@dbcelebrate-pu5ja.mongodb.net/test?retryWrites=true&w=majority",connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1)
           
db     = client.get_database("dbCelebrate",connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1)

users = db["USERS"]
            
result = users.find_one()
print(result)
client.close()