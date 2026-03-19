# Types-of-databases-and-Database-containerization
The base codes for mySql, mongoDB, and more




## MySQL
Relational (functionality/structure)

## MongoDB
Document (flexibility)

### 📌 Query‑Driven Schema Design
Shape schemas around read patterns, not relational structure. \
Embed for bounded, co‑accessed data \
Reference for large or shared data \
Bucket for logs/time‑series 

### 🗂️ 2. Data Modeling Patterns
📦 Embedding Use for: profiles, product attributes, small nested data. \
🔗 Referencing Use for: reusable entities, large subdocs, many‑to‑many. \
🪣 Bucketing Use for: IoT, logs, metrics. 


## Redis
Key-value (Speed
- Speed
- Implementations

## Cassandra
Scalability



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
