import sqlite3
import os

if os.path.exists("students.db"):
    os.remove("students.db")

conn = sqlite3.connect("students.db")
conn.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)")

students = [
    ("tamerlan", "tamerlancud@ac.ae", "pass123"),
    ("alisha", "alishacud@ac.ae", "alisha2024"),
    ("roman", "romancud@ac.ae", "romanR!99"),
]

conn.executemany("INSERT INTO students (name, email, password) VALUES (?, ?, ?)", students)
conn.commit()
conn.close()

print("students.db created")
