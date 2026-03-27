
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)
seats = {"S"+str(i): None for i in range(1, 101)}
lock = threading.Lock()

@app.route("/book", methods=["POST"])
def book():
    user = request.json.get("user")
    with lock:
        for seat, val in seats.items():
            if val is None:
                seats[seat] = user
                return jsonify({"seat": seat, "user": user})
    return jsonify({"error": "No seats available"}), 400

@app.route("/status")
def status():
    return jsonify(seats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
