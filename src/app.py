from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

app.run(debug=True)
