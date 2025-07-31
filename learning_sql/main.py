import sqlite3
import json

# Connect to database
connection = sqlite3.connect('my_database.db')
connection.row_factory = sqlite3.Row  # Set this BEFORE any operations
cursor = connection.cursor()


# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS job_applications(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    position_applied VARCHAR(100),
    experience_years INT,
    status VARCHAR(20),
    location VARCHAR(100),
    application_date DATE
)
''')

# Insert data (same as before)
insert_multi_query = """ 
INSERT INTO job_applications (name, email, position_applied, experience_years, status, location, application_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

multi_applicant = [
('Ankita Sharma', 'ankita.sharma@gmail.com', 'Frontend Developer', 2, 'Pending', 'Bangalore', '2024-12-01'),
('Rohit Verma', 'rohit.verma@yahoo.com', 'Backend Developer', 3, 'Interviewed', 'Delhi', '2024-12-05'),
('Neha Iyer', 'neha.iyer@outlook.com', 'Full Stack Developer', 1, 'Rejected', 'Chennai', '2024-12-07'),
('Amit Tiwari', 'amit.tiwari@gmail.com', 'Backend Developer', 4, 'Selected', 'Pune', '2024-12-10'),
('Pooja Nair', 'pooja.nair@gmail.com', 'Data Analyst', 2, 'Pending', 'Hyderabad', '2024-12-15'),
('Sahil Mehta', 'sahil.mehta@gmail.com', 'Frontend Developer', 0, 'Rejected', 'Gurgaon', '2024-12-17'),
('Swati Agarwal', 'swati.agarwal@gmail.com', 'UI/UX Designer', 3, 'Interviewed', 'Mumbai', '2024-12-20'),
('Karan Sethi', 'karan.sethi@gmail.com', 'Full Stack Developer', 2, 'Selected', 'Ahmedabad', '2024-12-21'),
('Priya Deshmukh', 'priya.deshmukh@gmail.com', 'Data Analyst', 1, 'Pending', 'Nagpur', '2024-12-22'),
('Nikhil Rao', 'nikhil.rao@gmail.com', 'Backend Developer', 5, 'Rejected', 'Bangalore', '2024-12-23'),
('Divya Kapoor', 'divya.kapoor@gmail.com', 'Frontend Developer', 2, 'Interviewed', 'Noida', '2024-12-24'),
('Arjun Malhotra', 'arjun.malhotra@gmail.com', 'DevOps Engineer', 3, 'Selected', 'Chandigarh', '2024-12-25'),
('Meena Joshi', 'meena.joshi@gmail.com', 'Product Manager', 6, 'Interviewed', 'Jaipur', '2024-12-26'),
('Ritesh Kumar', 'ritesh.kumar@gmail.com', 'Full Stack Developer', 1, 'Pending', 'Lucknow', '2024-12-27'),
('Sneha Patil', 'sneha.patil@gmail.com', 'UI/UX Designer', 2, 'Rejected', 'Pune', '2024-12-28'),
('Manish Dubey', 'manish.dubey@gmail.com', 'Frontend Developer', 4, 'Selected', 'Indore', '2024-12-29'),
('Ishita Roy', 'ishita.roy@gmail.com', 'Backend Developer', 2, 'Pending', 'Kolkata', '2024-12-30'),
('Rajiv Sinha', 'rajiv.sinha@gmail.com', 'Data Analyst', 3, 'Interviewed', 'Delhi', '2024-12-31'),
('Tanya Jain', 'tanya.jain@gmail.com', 'Full Stack Developer', 1, 'Selected', 'Mumbai', '2025-01-01'),
('Vikram Reddy', 'vikram.reddy@gmail.com', 'Frontend Developer', 2, 'Rejected', 'Hyderabad', '2025-01-02')
]

# cursor.executemany(insert_multi_query, multi_applicant)
connection.commit()

# Now query and convert to JSON
cursor.execute("SELECT * FROM job_applications")
all_applicants = cursor.fetchall()

# Convert to JSON
applicants_json = [dict(applicant) for applicant in all_applicants]
print(json.dumps(applicants_json, indent=2))

connection.close()
