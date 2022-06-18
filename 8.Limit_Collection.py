import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
query=collection.find().limit(8)
for a in query:
    print(a)
