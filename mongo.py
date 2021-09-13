import os
import pymongo
if os.path.exists("env.py"):
    import env


# static variables
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        connection = pymongo.MongoClient(url)
        print("Mongo is connected")
        return connection
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


connection = mongo_connect(MONGO_URI)

collection = connection[DATABASE][COLLECTION]

new_document = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "gender": "m", "hair_color": "grey", "occupation": "writer", "nationality": "british"}

collection.insert(new_document)

documents = collection.find()

for document in documents:
    print(document)
