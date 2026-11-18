import hashlib
import csv
import os

os.makedirs("data", exist_ok=True)

users = [
    ("tamerlan", "123456"),
    ("alisha", "password"),
    ("roman", "qwerty123"),
    ("sara", "Tr0ub4dor&9"),
    ("yerlan", "Horse-Battery-Staple-77"),
]

f1 = open("data/weak_shadow.csv", "w", newline="")
f2 = open("data/weak.hashes", "w")
f3 = open("data/users.txt", "w")

writer = csv.writer(f1)
writer.writerow(["username", "md5_hash"])

for username, password in users:
    h = hashlib.md5(password.encode()).hexdigest()
    writer.writerow([username, h])
    f2.write(h + "\n")
    f3.write(username + ":" + password + "\n")
    print(username, h)

f1.close()
f2.close()
f3.close()
