import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="adarsh02022004",
    database="practice_db",
)

print("Connection successful")

cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO students (id, name, age)
    VALUES
    (78, 'adarsh', 19),
    (75, 'vedant', 20)
    """
)

conn.commit()

print("Data inserted successfully")

conn.close()
