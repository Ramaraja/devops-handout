# Webapp - interacts with database

1. Create container for webapp - Dockerfile (webapp image) - <docker build -t <imagename> .>
2. Create DB container Mysql



-> get into the mysql prompt 
> docker exec -it <id/name> bash
> mysql -uuser -puserpassword

> show databases;

> use exampledb;

> show tables;

>

CREATE TABLE exampledb.users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);



curl -X POST http://localhost:9000/add -H "Content-Type: application/json" -d '{"name": "Ramaraja}'