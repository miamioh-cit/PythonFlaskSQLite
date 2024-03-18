from datetime import datetime
from flask import Flask, render_template
from . import app
import sqlite3

def processQuery(sql):
    conn = sqlite3.connect('demo.db')
    cursor = conn.execute(sql)

    result = "" 
    for row in cursor:
        result = row[0]

    conn.close()
    return result


@app.route("/")
def home():
    sql = "Select Article \
                from content \
                Where ID = 1;"
    content = processQuery(sql)
    return render_template("home.html", article=content)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
