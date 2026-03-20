import pymongo

# 1. Connect to the local MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Connect to the EmployeeDB and the employee collection
db = client["EmployeeDB"]
collection = db["employee"]

# 3. Create a filter for the employee with LastName "Rose"
filter = {"LastName":"Rose"}

# 4. Create the new values to be updated (Age to 32)
newvalues = { "$set": { "Age": 32 } }

# 5. Call update_one to apply the change
collection.update_one(filter, newvalues)

# 6. Print the entire collection to verify the update
employeeCursor = collection.find()
for employee in employeeCursor:
    print(employee)