# main.py

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('my_database.db')

# You can now interact with the database using the 'connection' object
# For example, create a cursor and execute SQL commands
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT)''')


connection.commit()

print("SQLite database created or connected successfully!")

print("Table 'users' created or connected successfully!")






# --- Inserting a single user ---
insert_single_user_query = """
INSERT INTO users (name, email)
VALUES (?, ?);
"""

single_user_data = ('Eve', 'eve@example.com')
cursor.execute(insert_single_user_query, single_user_data)
connection.commit()
print(f"Inserted single user: {single_user_data[0]} with ID: {cursor.lastrowid}")



# Close the connection when you're done
connection.close()