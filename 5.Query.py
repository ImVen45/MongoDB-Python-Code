import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
query={"name":{"$gt":"b"}}        ''' gt means greater than '''
documents=collection.find(query)
for a in documents:
    print(a)