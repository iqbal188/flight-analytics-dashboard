import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="indigo"
    )
    mycursor = conn.cursor()
    print('connect success')
except:
    print('connect fail')

# Create a Database on db server
#mycursor.execute('CREATE DATABASE indigo')
#conn.commit()

# Create a Table
#mycursor.execute("""
#CREATE TABLE airport(
#airport_id INTEGER PRIMARY KEY,
#code VARCHAR(10) NOT NULL,
#city VARCHAR(50) NOT NULL,
#name VARCHAR(100) NOT NULL
#)

#""")
#conn.commit()

# Insert data into a table
#mycursor.execute("""
    #INSERT INTO airport VALUES
    #(1,'DEL','New Delhi','Indira Gandhi International Airport'),
    #(2,'BLR','Bangalore ','Kempegowda International Airport'),
    #(3,'BOM','Mumbai','Chhatrapati Shivaji Maharaj International Airport (CSMIA)')
#""")
#conn.commit()

# Search/Retrive
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)

# UPDATE
mycursor.execute("""
UPDATE airport 
SET city='Bombay'
WHERE airport_id = 3
""")

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("""
DELETE FROM airport
WHERE airport_id = 3""")

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)


