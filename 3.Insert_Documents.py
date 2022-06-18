import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
insert=[{"name":"David","age":"20"},
{"name":"Bob","age":"21"},
{"name":"alexa","age":"25"},
{"name":"alex","age":"30"},
{"name":"trodu","age":"29"},
{"name":"john","age":"28"},
{"name":"ben","age":"20"},
{"name":"betty","age":"27"},
{"name":"anna","age":"18"},
{"name":"vasu","age":"16"},
]

''' a=collection.insert_one(insert)  ---- if we insert_one() can one record data at time and insert_many() is can multiple records at time. '''

a=collection.insert_many(insert)  
print(a.inserted_ids)