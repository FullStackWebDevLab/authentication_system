from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    print(data)

    return jsonify(["Success"])

app.run(debug=True)
