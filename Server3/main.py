from flask import Flask, request, jsonify

app = Flask(__name__)

server_number = 3

@app.route("/api", methods=["GET"])
def functionApi():
    return jsonify({"message": f"API do servidor {server_number}"})

@app.route("/api/welcome", methods=["GET"])
def functionWelcome():
    ip_address = request.headers.get("X-Forwarded-For")
    return jsonify({"message": f"Bem vindo ao servidor {server_number}", "ip_address": ip_address})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
