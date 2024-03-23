import sqlite3

conn = sqlite3.connect("questions.db")
cursor= conn.cursor()

# query = 'DROP TABLE IF EXISTS users'
# cursor.execute(query)

# query = 'DROP TABLE IF EXISTS categories'
# cursor.execute(query)

# query = 'DROP TABLE IF EXISTS product'
# cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)'
cursor.execute(query)


query = 'CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY NOT NULL, image TEXT NOT NULL, name TEXT NOT NULL, price NUMBER NOT NULL, categoryID INTERGER, FOREIGN KEY (categoryID) REFERENCES categories(ID))'
cursor.execute(query)

query = 'INSERT INTO users VALUES (1, "TestUser", "123456"), (2, "tennis", "3423"), (3, "Football", "654321"), (4, "Jaden", "489382"), (5, "William", "538482")'
cursor.execute(query)

query = 'INSERT INTO categories VALUES (1, "Laptop"), (2, "TV")'
cursor.execute(query)

query = 'INSERT INTO product VALUES (1, "https://images.pexels.com/photos/20440051/pexels-photo-20440051/free-photo-of-a-woman-leaning-against-a-railing-with-her-hand-on-her-chin.jpeg", "HP360", 341412, 1)'
cursor.execute(query)

cursor.execute('SELECT * FROM users')
data = cursor.fetchall()
print("data:",data)

query = 'UPDATE users SET username = "TonTon", password ="22222" WHERE id == 1'
cursor.execute(query)

cursor.execute('SELECT * FROM users')
data = cursor.fetchall()
print("data:",data)

# query = 'DELETE FROM users WHERE id ==1'
# cursor.execute(query)

cursor.execute('SELECT * FROM users WHERE PASSWORD == "123456"')
data = cursor.fetchall()
print("After delete:",data)

query = 'SELECT * FROM product WHERE categoryID == 1'
cursor.execute(query)

query = 'SELECT p.name, p.price, c.name FROM product p LEFT JOIN categories c ON p.categoryID ==c.id'
cursor.execute(query)

conn.commit()