import os, sys
from os.path  import dirname,join,abspath

# print(dirname(__file__)) 
# print(join(dirname(__file__),'env.py'))

# print(abspath(join(dirname(__file__),'env.py')))

toBeInsertedPath = abspath(join(dirname(__file__),'env.py'))

sys.path.insert(0, toBeInsertedPath)

from env import env


# we now have access to the variable from the env.py file

# print(env)

import pymongo
client = pymongo.MongoClient(env["mongoURI"])


# create a database
db = client["mongo-python"]

# creating collection
UserCollection = db["users"]

# creating a document
user={
    "name":"Johvbvbvn",
    "email":"johnJosbvbvhua@ok.com",
    "password":[
        {
            "password":"123456",
            "salt":"sdsd"
        },
        {
            "password":"123456",
            "salt":"sdsd"
        }
    ]
}
UserCollection.insert_one(user)

# insert many
users = [
    {
        "name":"John",
        "email":"dfdfD",
        "password":"123456"
    },
    {
        "name":"John",
        "email":"dfdfD",
        "password":"123456"
    }]

UserCollection.insert_many(users)

# display data
# data = UserCollection.find()
# for d in data:
#     print(d)
    
    
# find one
data = UserCollection.find_one(
    {
        "email":"dfdfD",
    }
)


print(data["_id"])
# get doc from id
data = UserCollection.find_one(
    filter={
        "_id":data["_id"]
    }
)
print(data)

# dropping the collection
UserCollection.drop()