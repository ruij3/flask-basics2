from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chickens")
def chickens():
    return render_template("aboutchicken.html")

@app.route("/pandas")
def pandas():
    return render_template("aboutpandas.html")

if __name__ == "__main__":
    app.run(debug=True, port=12345)
