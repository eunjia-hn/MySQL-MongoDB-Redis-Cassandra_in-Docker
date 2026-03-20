import pymongo

# 1. Connect to the local MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Connect to the EmployeeDB and the employee collection
db = client["EmployeeDB"]
collection = db["employee"]

# 3. Use the find method to get all employees with LastName "Smith"
# This returns a cursor object containing multiple records
employeeCursor = collection.find({"LastName":"Smith"})

# 4. Loop through the cursor and print each employee
for employee in employeeCursor:
    print(employee)