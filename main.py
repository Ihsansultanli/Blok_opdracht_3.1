from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/test")
def test():
    return " Hello bud!"

@app.route("/login")
def login():
    return "Hello this is login page!"

if __name__ == "__main__":
    app.run(port=8000, debug=True)

