from flask import Flask
import socket

app = Flask(__name__);

@app.route("/")
def index():
    return f"This is a flask app serving from : {socket.gethostname()}";

@app.route("/home")
def home():
    return f"Home Page serving from : {socket.gethostname()}";

if __name__ == "__main__":
    app.run(debug=True);
