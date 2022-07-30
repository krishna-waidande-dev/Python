from flask import Flask, render_template
from markupsafe import escape
from generateMap import render_map

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1 #to disable cache


@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route("/worldmap")
def worldmap():
    render_map()
    return render_template("latitude-longitute.html", name="worldmap")

