from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is my first web app deployed using github repo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)  # ✅ Explicitly set port 8080





