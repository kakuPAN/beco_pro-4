from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("page1.html")

@app.route("/two")
def hello_two():
    return render_template("page2.html")

if __name__ == '__main__':
    app.run()