#    To Delete One Record
'''
import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
database=conn["Python"]
collection=database["user"]
query={"name":"David"}
collection.delete_one(query)
for a in collection.find():
    print(a)
'''



import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
query={"age":{"$regex":"^16"}} # it deletes the age:16 record
count=collection.delete_many(query)
print(count.deleted_count,"documents deleted")
for a in collection.find():
    print(a)

#collection.delete_many({})  --- To Delete Many Records
