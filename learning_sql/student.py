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


cursor.execute("""--sql 
               create table if not exists employees (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     position TEXT NOT NULL,
                     salary REAL NOT NULL
                )
               
               """)

print("Employees table created or already exists")

# insert data into employees table

insert_employees_query = """--sql
INSERT INTO employees (name, position, salary)
VALUES (? , ? , ?)
"""

employee_data_to_insert = [
    ('John Doe', 'Software Engineer', 75000.00),
    ('Jane Smith', 'Data Scientist', 80000.00),
    ('Alice Johnson', 'Project Manager', 90000.00),
    ('Bob Brown', 'UX Designer', 70000.00),
    ('Charlie White', 'DevOps Engineer', 85000.00),
    ('Diana Prince', 'Systems Analyst', 95000.00),
    ('Bruce Wayne', 'Security Specialist', 100000.00),
    ('Clark Kent', 'Database Administrator', 78000.00),
    ('Peter Parker', 'Web Developer', 72000.00),
    ('Tony Stark', 'AI Engineer', 120000.00)
]

cursor.executemany(insert_employees_query, employee_data_to_insert)
connection.commit()

print("Employee data inserted successfully")

# Fetch all employees
fetch_all_employees_query = """--sql
SELECT * FROM employees
"""
cursor.execute(fetch_all_employees_query)
all_employees = cursor.fetchall()

for employee in all_employees:
    print(json.dumps(dict(employee), indent=4))
    
print("\n" + "=" * 50)

connection.close()

