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
        return connection
    except pymongo.errors.ConnectionFailure as e:
        print("ERROR: Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5 Exit")

    option = input("Enter option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        document = collection.find_one({ "first": first.lower(), "last": last.lower() }) 
    except:
        print("ERROR: Error accessing the database")

    if not document:
        print("")
        print("WARNING: No results found!")

    return document


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occcupation > ")
    nationality = input("Enter nationality > ")

    new_document = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender.lower(),
        "hair_color": hair_color.lower(),
        "occupation": occupation.lower(),
        "nationality": nationality.lower()
    }

    try:
        collection.insert_one(new_document)
        print("")
        print("INFO: Document inserted")
    except:
        print("ERROR: Error accessing the database")


def find_record():
    document = get_record()
    if document:
        print("")
        for key, value in document.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())


def edit_record():
    document = get_record()
    if document:
        update_document = {}
        print("")
        for key, value in document.items():
            if key != "_id":
                update_document[key] = input(key.capitalize() + " [" + value + "] > ")

                if update_document[key] == "":
                    update_document[key] = value
        
        try:
            collection.update_one(document, {"$set": update_document})
            print("")
            print("INFO: Document updated")
        except:
            print("ERROR: Error accessing the database")


def delete_record():
    document = get_record()
    if document:
        print("")
        for key, value in document.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())

    print("")
    confirmation = input("Is this the document you want to delete?\nY or N > ")
    print("")

    if confirmation.lower() == "y":
        try:
            collection.delete_one(document)
            print("INFO: Document deleted")
        except:
            print("ERROR: Error accessing the database")
    else:
        print("INFO: Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()       
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            connection.close()
            break
        else:
            print("Invalid option")
        print("")


connection = mongo_connect(MONGO_URI)
collection = connection[DATABASE][COLLECTION]
main_loop()
