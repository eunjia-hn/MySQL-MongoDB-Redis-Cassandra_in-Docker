import pymongo

# 1. Connect to your local MongoDB database
# Standard connection string for a local MongoDB on port 27017
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Connect to the EmployeeDB 
# MongoDB creates the DB and Collection automatically if they don't exist
db = client["EmployeeDB"]
collection = db["employee"]

# 3. The employeeCollection list in JSON format
employeeCollection = [
    {"FirstName":"John", "LastName":"Smith", "Age":25},
    {"FirstName":"Peter", "LastName":"Smith", "Age":26},
    {"FirstName":"Gabriel", "LastName":"Smith", "Age":28},
    {"FirstName":"Penny", "LastName":"Lane", "Age":22},
    {"FirstName":"Eleanor", "LastName":"Rigby", "Age":23},
    {"FirstName":"Helen", "LastName":"Rose", "Age":23}
]

# Insert the list into the collection
result = collection.insert_many(employeeCollection)

# 4. Verify that the database and collection have been created
if "EmployeeDB" in client.list_database_names():
    print("Employee database created!")
    
# Print the ObjectIds of the inserted documents
print(result.inserted_ids)