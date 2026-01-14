import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users (
    id INT,
    email VARCHAR(100),
    password_hash VARCHAR(255)
)
""")

cursor.execute("INSERT INTO users (id, email, password_hash) VALUES (?, ?, ?)", (1, "example@email.com", "password hash"))

connection.commit()

cursor.execute("SELECT * FROM users")
for x in cursor:
    print(x)
