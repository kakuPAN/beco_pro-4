from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "デプロイ成功"
