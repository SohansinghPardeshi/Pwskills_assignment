'''
Q1. What is a database? Differentiate between SQL and NoSQL databases.

A database is a collection of organized data that is stored and accessed electronically. Databases are designed to handle large amounts of data and to provide efficient and reliable storage and retrieval of data.

SQL and NoSQL are two different types of databases that differ in their data models and querying languages. Here's a brief overview of the differences between SQL and NoSQL databases:

SQL databases:

Use a structured data model that consists of tables with predefined columns and data types.
Use the SQL (Structured Query Language) to interact with the database and manipulate data.
Are typically used for applications that require a high degree of data consistency and ACID (Atomicity, Consistency, Isolation, Durability) transactions.
Are vertically scalable, meaning they can handle more traffic and data by adding more resources to a single server.
Examples include MySQL, PostgreSQL, Oracle, and Microsoft SQL Server.
NoSQL databases:

Use a non-structured data model that can be either document-based, key-value, column-family, or graph-based.
Use their own query languages that are optimized for the specific data model, such as MongoDB's query language for document-based databases.
Are typically used for applications that require high scalability and availability, and can sacrifice some data consistency for performance.
Are horizontally scalable, meaning they can handle more traffic and data by adding more servers to a cluster.
Examples include MongoDB, Cassandra, DynamoDB, and Redis.
In summary, SQL databases are good for applications that require a high degree of data consistency and structured data, while NoSQL databases are good for applications that require high scalability, performance, and flexibility in data modeling.
'''
# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

# DDL stands for Data Definition Language, which is a set of SQL commands used to define and modify the structure of database objects such as tables, indexes, views, and procedures. 

# CREATE: The CREATE command is used to create a new database object such as a table, view, or procedure. 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test")
mycursor.execute("CREATE TABLE if not exists test.users ( id INT PRIMARY KEY, name VARCHAR(50), email VARCHAR(100));")




# ALTER: The ALTER command is used to modify the structure of an existing database object such as a table or view. 
# mycursor.execute("ALTER TABLE test.users ADD COLUMN phone VARCHAR(20);")

mycursor.execute("insert into test.users values(666 , 'sohan'  ,'pardeshi@gmail.com','9098789900')")
mydb.commit()



# TRUNCATE: The TRUNCATE command is used to delete all data from a table, but keep the structure of the table intact
mycursor.execute("TRUNCATE TABLE test.users;")



# DROP: The DROP command is used to delete an existing database object such as a table or view
# mycursor.execute("DROP TABLE test.users;")


# Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
# DML stands for Data Manipulation Language. It is a subset of SQL (Structured Query Language) that is used to modify data in a database. DML commands include INSERT, UPDATE, and DELETE.

# INSERT: INSERT command is used to insert new rows into a table.

mycursor.execute("insert into test.users values(667 , 'sohan'  ,'pardeshi@gmail.com','9098789900')")
mycursor.execute("insert into test.users values(668 , 'sohan'  ,'pardeshi@gmail.com','9098789900')")
mydb.commit()

# UPDATE: UPDATE command is used to modify existing rows in a table. The syntax for the UPDATE command is:
mycursor.execute("UPDATE test.users SET phone = '9098789901' WHERE id = 667;")
mydb.commit()



# DELETE: DELETE command is used to delete existing rows from a table. 
mycursor.execute("DELETE FROM test.users WHERE id = 668;")
mydb.commit()

# Q4. What is DQL? Explain SELECT with an example.

# DQL stands for Data Query Language. It is a subset of SQL (Structured Query Language) used to retrieve data from one or more tables in a database.
# SELECT is the most commonly used command in DQL, which allows you to select data from a table

mycursor.execute("select *  from test.users ")
for i in mycursor:
  print(i)


# Q5. Explain Primary Key and Foreign Key.
'''
Primary key and foreign key are two important concepts in database design that are used to establish relationships between tables.

Primary Key: A primary key is a column or a combination of columns in a table that uniquely identifies each row in the table. 
It must have a unique value for each row and cannot contain null values.
By defining a primary key on a table, you can ensure data integrity and prevent duplicate rows from being inserted into the table.

Foreign Key: A foreign key is a column or a combination of columns in a table that refers to the primary key of another table. 
It is used to establish a relationship between two tables, where the foreign key column(s) in one table refers to the primary key column(s) in another table.
By defining a foreign key constraint, you can enforce referential integrity between the two tables, which ensures that the data in the tables is consistent and accurate.
'''

# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
# cursor() method:
# The cursor() method is used to create a cursor object, which is used to execute SQL statements and retrieve data from the database. 
# The cursor object provides methods for executing SQL statements, fetching data from the result set, and iterating over the result set.

# The execute() method is used to execute a SQL statement on the database.

# Q7. Give the order of execution of SQL clauses in an SQL query.
'''
FROM: This clause specifies the table or tables from which the data is to be selected.

JOIN: If the query includes one or more join operations, they are executed after the FROM clause.

WHERE: This clause is used to filter the data based on a specific condition or set of conditions.

GROUP BY: This clause is used to group the data based on one or more columns.

HAVING: This clause is used to filter the grouped data based on a specific condition or set of conditions.

SELECT: This clause is used to select the columns to be included in the result set.

DISTINCT: This clause is used to eliminate duplicate rows from the result set.

ORDER BY: This clause is used to sort the result set based on one or more columns.

LIMIT: This clause is used to limit the number of rows returned by the query.
'''