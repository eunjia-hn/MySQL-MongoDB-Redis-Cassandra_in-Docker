# Types-of-databases-and-Database-containerization
The base codes for mySql, mongoDB, and more

Initialize the driver (mySql): 
```
pip3 install mysql-connector-python
```

## MySQL
Relational (functionality/structure)


## Document Databases (MongoDB): Flexibility for Complex Profiles
Document databases store data in a non-relational format, typically using JSON-like documents where related information is kept together rather than split across tables. The primary advantage of this structure is schema flexibility; developers can add new fields to a record without needing to redefine the entire database. However, this flexibility can lead to data redundancy and is less efficient for applications requiring complex mathematical joins between different data sets.
**Real-Life Use Case:**  
Think of a Social Media User Profile. Your profile might include basic text, a list of hobbies, and a gallery of photos, while a professional's profile might include job history and certifications. Because every user has a different "shape" of data, a document database like MongoDB allows the platform to store these varied profiles in one place without forcing everyone to have the exact same fields.
🗂️**Data Modeling Patterns**
📦 Embedding Use for: profiles, product attributes, small nested data.
🔗 Referencing Use for: reusable entities, large subdocs, many‑to‑many.
🪣 Bucketing Use for: IoT, logs, metrics. 


## Key-Value Databases (Redis): Speed for Instant Access
Key-value databases are the simplest form of NoSQL, storing data as a collection of unique keys paired with specific values. This "dictionary" structure allows for unparalleled speed and low latency, as the system does not need to search through a complex index to find a record. The trade-off is that they lack advanced querying capabilities; you can usually only retrieve data if you have the specific key.
**Real-Life Use Case:**  
Consider Login Session Management. When you log into an app, the system needs to remember you are "authenticated" as you click from page to page. By storing your "Session ID" as the Key and your "Login Status" as the Value in a key-value store like Redis, the app can verify your identity in milliseconds, ensuring your experience remains fast and seamless.


## Distributed Scalable Databases (Cassandra): Reliability for Global Traffic
Distributed scalable databases are designed to manage massive amounts of data across many different servers (nodes). Their greatest strength is "High Availability," meaning that if one server fails, the rest of the system keeps running without losing data. The complexity of managing these distributed nodes is their main weakness, often requiring specialized expertise to maintain.
**Real-Life Use Case:**  
Think of a Global Weather Application. Millions of people around the world check the weather simultaneously, and sensors are constantly uploading new temperature data from every continent. A distributed database like Cassandra allows the app to scale horizontally—simply adding more servers as the number of users grows—ensuring that the app never crashes, even during a major global storm when traffic spikes.



## Docker
mongoDB
```
docker run -p 27017:27017 --name some-mongo -d mongo
```
redis
```
docker run -p 6379:6379 --name some-redis -d redis
```
Cassandra
```
docker run -p 9042:9042 --name some-cassandra -d cassandra
```
