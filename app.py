from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(msg= "Hello, backend! 🚀")

if __name__ == "__main__":
    app.run(debug=True)