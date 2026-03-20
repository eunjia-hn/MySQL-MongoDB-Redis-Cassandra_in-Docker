import pymongo

# 1. Connect to the local MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Connect to the EmployeeDB and the employee collection
db = client["EmployeeDB"]
collection = db["employee"]

# 3. Create a filter for the employee with LastName "Rose"
filter = {"LastName":"Rose"}

# 4. Call the delete_one method to remove the record
collection.delete_one(filter)

# 5. Print the employees collection to verify deletion
employeeCursor = collection.find()
for employee in employeeCursor:
    print(employee)