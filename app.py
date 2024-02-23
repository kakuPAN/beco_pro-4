from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("page1.html")

@app.route("/two")
def hello_two():
    return render_template("two.html")

if __name__ == '__main__':
    app.run