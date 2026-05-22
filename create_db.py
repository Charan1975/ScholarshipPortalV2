import sqlite3

# Connect database
conn = sqlite3.connect('scholarship.db')

cursor = conn.cursor()

# Create Scholarships table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Scholarships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scholarship_name TEXT,
    min_cgpa REAL,
    max_income REAL,
    amount TEXT,
    official_link TEXT
)
''')

# Insert scholarship data
# Insert scholarship data

scholarships = [

(
'National Scholarship Portal',
7.0,
300000,
'₹50,000 per year',
'https://scholarships.gov.in/'
),

(
'AICTE Pragati Scholarship',
8.0,
500000,
'₹50,000 per year',
'https://www.aicte-india.org/schemes/students-development-schemes'
),

(
'Central Sector Scholarship',
7.5,
400000,
'₹20,000 per year',
'https://scholarships.gov.in/'
),

(
'Post Matric Scholarship',
6.5,
250000,
'₹15,000 per year',
'https://scholarships.gov.in/'
),

(
'Merit Cum Means Scholarship',
8.5,
600000,
'₹60,000 per year',
'https://scholarships.gov.in/'
)

]

cursor.executemany('''
INSERT INTO Scholarships
(scholarship_name, min_cgpa, max_income, amount, official_link)

VALUES (?, ?, ?, ?, ?)
''', scholarships)

conn.commit()

print("Database Created Successfully!")