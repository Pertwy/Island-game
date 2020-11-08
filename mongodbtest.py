import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://pertwy:Bobbobb0bbob@cluster0.akhrt.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]


post1 = {"_id": 0, "name": "Tim", "Score": 5}
post2 = {"_id": 1, "name": "John", "Score": 10}


# Insert one  post

collection.insert_one(post1)


# Insert more than one post
'''
collection.insert_many(post1, post2)
'''
'''
results = collection.find({"name":"Tim"})
for result in results:
    print(result)
    print(result["_id"])


#finds one one result
results = collection.find_one({"_id":0})
print(results)


#return everyhting
results = collection.find({})
for x in results:
    print(x)
'''

# Deleting stuff works the same as adding
'''
results = collection.delete_one({"_id":0})
'''

# Update data
'''
results = collection.update_one({"_id":0}, {"$set":{"name":"Jimmy"}})
'''

# Update with nrew feild
'''
results = collection.update_one({"_id":0}, {"$set":{"Hello":"Sup"}})
'''

'''
post_count = collection.count_documents({})
print(post_count)

#$in ???
'''
