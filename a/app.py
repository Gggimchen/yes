from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def SignInPage():
    return render_template("sumthing.html")

@app.route("/productpage")
def ProductPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory=sqlite3.Row

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM product")

    rows=cursor.fetchall()
    print("Rows:", rows)

    return render_template("productpage.html", rows = rows)

@app.route("/categories")
def CategoryPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory=sqlite3.Row

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM categories")

    rows=cursor.fetchall()
    print("Rows:", rows)

    return render_template("categories.html", rows = rows)
