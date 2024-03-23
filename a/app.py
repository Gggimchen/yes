from flask import Flask, render_template, request, redirect, url_for
import sqlite3

conn = sqlite3.connect('questions.db', check_same_thread=False)
conn.row_factory=sqlite3.Row
cursor=conn.cursor()

app = Flask(__name__)

@app.route("/", methods =['GET', 'POST'])
def SignInPage():
    if request.method == 'POST':
        print('POST')
        username = request.form['username']
        password = request.form['password']
        print("signing in ... usernam:"+username+", password=="+password)

        query= "SELECT * FROM users WHERE username=='" + username + "' AND password=='" +password+"'"
        cursor.execute(query)

        users = cursor.fetchall()
        if(len(users) > 0):
            print("Sign in successful")
            return redirect(url_for('ProductPage'))
        else:
            print("No user found")


    return render_template("sumthing.html")

@app.route("/productpage")
def ProductPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory=sqlite3.Row

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM product")

    rows=cursor.fetchall()
    print("Rows:", rows)

    return render_template('productpage.html', rows=rows)

@app.route("/productpage/delete/<id>")
def deleteEntry(id):
    query = 'DELETE FROM product WHERE id ==' +id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('ProductPage'))

@app.route("/categories")
def CategoryPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory=sqlite3.Row

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM categories")

    rows=cursor.fetchall()
    print("Rows:", rows)

    return render_template("categories.html", rows = rows)

@app.route("/users")
def UserPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory=sqlite3.Row

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")

    rows=cursor.fetchall()
    print("Rows:", rows)

    return render_template("users.html", rows = rows)