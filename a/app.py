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
    print("----------------Rows:", rows)

    return render_template('productpage.html', rows=rows)

@app.route("/productpage/delete/<id>")
def deleteEntry(id):
    query = 'DELETE FROM product WHERE id ==' +id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('ProductPage'))

@app.route('/productpage/edit/<id>', methods = ['GET', 'POST'])
def EditProductPage(id):
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        categoryID = request.form['categoryID']

        query = 'UPDATE product SET name ="'+name+'", price='+ price+', categoryID ='+categoryID+' WHERE id =='+id

        print("-----------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("ProductPage"))
    return render_template('EditProductPage.html', id=id)
    
@app.route("/productpage/add", methods = ['GET', 'POST'])
def AddProductPage():
    if request.method =='POST':
        name = request.form['name']
        price = request.form['price']
        categoryID = request.form['categoryID']

        query = 'INSERT INTO product (name, price, categoryID) VALUES ("'+name+'",'+price+','+categoryID+')'
        print('---------QUERY:' +query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("ProductPage"))
    return render_template('EditProductPage.html')

@app.route("/categories")
def CategoryPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory=sqlite3.Row

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM categories")

    rows=cursor.fetchall()
    print("Rows:", rows)

    return render_template("categories.html", rows = rows)

@app.route("/categories/delete/<id>")
def deleteEntryCategory(id):
    query = 'DELETE FROM categories WHERE id ==' +id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('CategoryPage'))

@app.route('/categories/edit/<id>', methods = ['GET', 'POST'])
def EditCategoryPage(id):
    if request.method == "POST":
        name = request.form['name']

        query = 'UPDATE categories SET name ="'+name+'" WHERE id =='+id

        print("-----------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("CategoryPage"))
    return render_template('EditCategoryPage.html', id=id)
    
@app.route("/categories/add", methods = ['GET', 'POST'])
def AddCategoryPage():
    if request.method =='POST':
        name = request.form['name']

        query = 'INSERT INTO categories (name) VALUES ("'+name+'")'
        print('---------QUERY:' +query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("CategoryPage"))
    return render_template('EditCategoryPage.html')

@app.route("/users")
def UserPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory=sqlite3.Row

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")

    rows=cursor.fetchall()
    print("Rows:", rows)

    return render_template("users.html", rows = rows)

@app.route("/users/delete/<id>")
def deleteEntryUser(id):
    query = 'DELETE FROM users WHERE id ==' +id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('UserPage'))

@app.route('/users/edit/<id>', methods = ['GET', 'POST'])
def EditUserPage(id):
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        query = 'UPDATE users SET username ="'+username+'", password ="'+password+'" WHERE id =='+id

        print("-----------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("UserPage"))
    return render_template('EditUserPage.html', id=id)
    
@app.route("/users/add", methods = ['GET', 'POST'])
def AddUserPage():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']

        query = 'INSERT INTO users (username, password) VALUES ("'+username+'", "'+password+'")'
        print('---------QUERY:' +query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("UserPage"))
    return render_template('EditUserPage.html')