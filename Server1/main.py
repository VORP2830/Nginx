from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    ip_address = request.headers.get("X-Forwarded-For")
    return jsonify({"message": "Bem vindo ao servidor 1", "ip_address": ip_address})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)