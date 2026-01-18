from flask import Flask, send_from_directory, jsonify, request
import sqlite3, bcrypt

# Constants
USERS_DATABASE = "users.db"

app = Flask(__name__, static_folder="static", static_url_path="")

def init_db():
    """
    Create the database and the 'users' table if they don't exist.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            email TEXT,
            password_hash TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]

    # Check if username or email exists.
    conn = sqlite3.connect(USERS_DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return "Username already exists."

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    if cursor.fetchone():
        conn.close()
        return "Email already exists."

    # Add user.
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    conn.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (username, email, password_hash)
    )
    conn.commit()
    conn.close()

    return "Success"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    password = data["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (data["username"],)
    )
    
    try:
        password_hash = cursor.fetchone()[0]
    except TypeError:
        return "Incorrect username."

    if bcrypt.checkpw(password.encode("utf-8"), password_hash):
        return "Successfull login."

    else: return "Incorrect password."


app.run(debug=True)
