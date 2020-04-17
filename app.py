from flask import Flask, render_template, request
from web_fun import save_data, read_data

app = Flask(__name__)

@app.route("/")
def home():
    posts = read_data('text')
    return render_template("home.html", posts=posts)

@app.route("/gallery")
def gallery():
    urls = read_data('url')
    return render_template("gallery.html", urls=urls)

@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/add-ok", methods=["POST"])
def add_ok():
    data = request.form
    if save_data(data['text'], data['url']):
        return render_template("ok.html")
    else:
        return render_template("error.html")