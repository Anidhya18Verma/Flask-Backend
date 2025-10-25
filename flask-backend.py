from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to invent it.",
    "Life is what happens when you're busy making other plans.",
    "You miss 100% of the shots you don’t take.",
    "In the middle of every difficulty lies opportunity.",
    "Do one thing every day that scares you."
]

@app.route("/quote", methods=["GET"])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
