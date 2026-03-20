import pymongo

# 1. Connect to the local MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Connect to the EmployeeDB and the employee collection
db = client["EmployeeDB"]
collection = db["employee"]

# 3. Create a filter for all employees with LastName "Smith"
filter = {"LastName":"Smith"}

# 4. Create newvalues to add the Department attribute
newvalues = { "$set": { "Department": "Computer Science" } }

# 5. Call update_many to apply the change to all Smiths
collection.update_many(filter, newvalues)

# 6. Print the entire collection to verify the new attribute
employeeCursor = collection.find()
for employee in employeeCursor:
    print(employee)