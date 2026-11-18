import sqlite3
import os
import bcrypt

os.makedirs("data", exist_ok=True)

if os.path.exists("data/secure_users.db"):
    os.remove("data/secure_users.db")

conn = sqlite3.connect("data/secure_users.db")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT)")

users = [
    ("tamerlan", "123456"),
    ("alisha", "password"),
    ("roman", "qwerty123"),
    ("sara", "Tr0ub4dor&9"),
    ("yerlan", "Horse-Battery-Staple-77"),
]

for username, password in users:
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed.decode()))
    print(username, hashed.decode())

conn.commit()
conn.close()

h1 = bcrypt.hashpw(b"123456", bcrypt.gensalt())
h2 = bcrypt.hashpw(b"123456", bcrypt.gensalt())
print("same password, different hash:", h1 != h2)
print("check correct password:", bcrypt.checkpw(b"123456", h1))
print("check wrong password:", bcrypt.checkpw(b"wrongpassword", h1))
