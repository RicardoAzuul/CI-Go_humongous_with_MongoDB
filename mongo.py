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

# new_document = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "gender": "m", "hair_color": "grey", "occupation": "writer", "nationality": "british"}

# collection.insert(new_document)

# new_documents = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]

# collection.insert_many(new_documents)

# collection.remove({ "first": "douglas"})

# updates the first document it finds
collection.update_one({ "nationality": "american" }, {"$set": {"hair_color": "maroon"}})

# update all documents
collection.update_many({ "nationality": "american" }, {"$set": {"hair_color": "maroon"}})

documents = collection.find({ "nationality": "american"})

for document in documents:
    print(document)
