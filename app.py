from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    note = open("story.txt", "r+", encoding="utf-8")
    story = note.read()
    note.close()
    return render_template("home.html", story=story)

@app.route("/gallery")
def gallery():
    note = open("note.txt", "r+", encoding="utf-8")
    photos = [i for i in note]
    note.close()
    return render_template("gallery.html", photos=photos)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add-ok", methods=["POST"])
def add_photo():
    note = request.form

    note_file = open("note.txt", "a+", encoding="utf-8")
    data_1 = note["url"] + '\n'
    note_file.write(data_1)
    note_file.close()

    story = open("story.txt", "a+", encoding="utf-8")
    data_2 = note["story"] + "\n"
    story.white(data_2)
    story.close()
    return render_template("ok.html")

