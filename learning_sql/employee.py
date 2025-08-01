
import json
import sqlite3
import logging


def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect('employee.db')
        logging.info("Connection established.")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
    return conn

def close_connection(conn):
    """Close the database connection."""
    if conn:
        conn.close()
        logging.info("Connection closed.")

def create_table(conn):
    """Create the employee table if it does not exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                department TEXT NOT NULL
            )
        ''')
        conn.commit()
        logging.info("Table created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error creating table: {e}")

def insert_employee(conn, name, age, department):
    """Insert a new employee into the employee table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employee (name, age, department)
            VALUES (?, ?, ?)
        ''', (name, age, department))
        conn.commit()
        logging.info("Employee inserted successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error inserting employee: {e}")

def print_employees(conn):
    """Print all employees in the employee table."""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee')
        rows = cursor.fetchall()
        for row in rows:
            logging.info(json.dumps({
                'id': row[0],
                'name': row[1],
                'age': row[2],
                'department': row[3]
            }, indent=4))
    except sqlite3.Error as e:
        logging.error(f"Error fetching employees: {e}")

def main():
    """Main function to demonstrate database operations."""
    logging.basicConfig(level=logging.INFO)
    if conn := create_connection():
        create_table(conn)
        insert_employee(conn, 'John Doe', 30, 'Engineering')
        insert_employee(conn, 'Jane Smith', 25, 'Marketing')
        print_employees(conn)
        close_connection(conn)

if __name__ == "__main__":
    main()


