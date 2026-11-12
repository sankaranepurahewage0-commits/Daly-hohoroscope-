from flask import Flask, jsonify, request
import os

from horoscope import get_horoscope
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Daily Horoscope Sinhala SMS",
        "status": "running"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/sms", methods=["POST"])
def receive_sms():
    return jsonify({
        "status": "received"
    }), 200
@app.route("/horoscope/<sign>", methods=["GET"])
def horoscope(sign):
    message = get_horoscope(sign)
    if message is None:
        return jsonify({"error": "Invalid zodiac sign"}), 400
    return jsonify({"sign": sign, "message": message}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
