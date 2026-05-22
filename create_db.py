import sqlite3

# Connect database
conn = sqlite3.connect('scholarship.db')

cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Scholarships (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    scholarship_name TEXT,

    min_cgpa REAL,

    max_income REAL,

    category TEXT,

    amount TEXT,

    official_link TEXT
)
''')

# Scholarship data
scholarships = [

(
'National Scholarship Portal',
7.0,
300000,
'General',
'₹50,000 per year',
'https://scholarships.gov.in/'
),

(
'Post Matric Scholarship',
6.5,
250000,
'SC',
'₹15,000 per year',
'https://socialjustice.gov.in/schemes/25'
),

(
'Minority Scholarship',
7.5,
400000,
'Minority',
'₹30,000 per year',
'https://www.minorityaffairs.gov.in/'
),

(
'AICTE Pragati Scholarship',
8.0,
500000,
'OBC',
'₹50,000 per year',
'https://www.aicte-india.org/schemes/students-development-schemes'
),

(
'Central Sector Scholarship',
8.0,
450000,
'General',
'₹20,000 per year',
'https://www.education.gov.in/scholarships-education-loan-4'
),

(
'Merit Cum Means Scholarship',
8.5,
600000,
'General',
'₹60,000 per year',
'https://www.minorityaffairs.gov.in/'
)

]
cursor.executemany('''
INSERT INTO Scholarships
(scholarship_name, min_cgpa, max_income, category, amount, official_link)

VALUES (?, ?, ?, ?, ?, ?)
''', scholarships)

conn.commit()

conn.close()

print("Database Created Successfully!")