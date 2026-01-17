from flask import Flask, send_from_directory, jsonify, request
import sqlite3, bcrypt

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
    password_hash = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())

    conn = sqlite3.connect("users.db")
    conn.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (data["username"], data["email"], password_hash)
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
