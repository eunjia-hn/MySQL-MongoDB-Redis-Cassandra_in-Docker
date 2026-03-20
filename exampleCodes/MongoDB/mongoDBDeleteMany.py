import pymongo

# 1. Connect to the local MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Connect to the EmployeeDB and the employee collection
db = client["EmployeeDB"]
collection = db["employee"]

# 3. Create a filter for all employees with LastName "Smith"
filter = {"LastName":"Smith"}

# 4. Call the delete_many method to remove all Smiths
collection.delete_many(filter)

# 5. Print the employees collection to verify they are all gone
employeeCursor = collection.find()
for employee in employeeCursor:
    print(employee)