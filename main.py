
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Addition API is running!"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send a JSON object"}), 400

    try:
        a = float(data["a"])
        b = float(data["b"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Provide numeric values for a and b"}), 400

    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
