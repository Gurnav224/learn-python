import sqlite3
import os
import json

connection = sqlite3.connect("student.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

# Get database name dynamically
db_path = connection.execute("PRAGMA database_list").fetchone()
db_name = os.path.basename(db_path[2])  # Extract just the filename
print(f"Successfully connected to the {db_name} database")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        class TEXT NOT NULL
    )
    """
)

print("Student table created")


# Get all tables with their details
cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("All Tables in Database:")
print("=" * 50)

for table in tables:
    table_name = table[0]
    table_sql = table[1]
    
    print(f"\nTable: {table_name}")
    
    
insert_students_query = """--sql
INSERT INTO students (name, age, class)
VALUES (? , ? , ?)
"""

student_data_to_insert = ('aman',22,'12th')

cursor.execute(insert_students_query, student_data_to_insert)
connection.commit()

print("data inserted successfully")

fetch_all_students_query = """--sql 
SELECT  * FROM students
"""
cursor.execute(fetch_all_students_query)
inserted_record = cursor.fetchone()

print(f"ID: {inserted_record[0]}, Name: {inserted_record[1]}, Age: {inserted_record[2]}, Class: {inserted_record[3]}")

connection.close()