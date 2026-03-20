import pymongo

# 1. Connect to your local MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Connect to the EmployeeDB and the employee collection
db = client["EmployeeDB"]
collection = db["employee"]

# 3. Use find_one to search for the record with LastName "Rigby"
employee = collection.find_one({"LastName":"Rigby"})

# 4. Print the result
print(employee)