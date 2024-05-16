from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    ip_address = request.remote_addr
    return f"Bem vindo ao servidor 1 e o IP de quem entrou é: {ip_address}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
