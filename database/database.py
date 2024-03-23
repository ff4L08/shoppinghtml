import sqlite3

conn =  sqlite3.connect('questions.db')
cursor = conn.cursor()


query = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)'
cursor.execute(query)

# create table categories ( )
query = 'CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)'
cursor.execute(query)

# create products ( )
query = '''CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY NOT NULL, 
name TEXT NOT NULL, 
quantities TEXT NOT NULL,
price INTEGER,
categoriesID INTEGER,
FOREIGN KEY (categoriesID) REFERENCES categories(id)
)'''
cursor.execute(query)




#add user
query = '''INSERT INTO users VALUES (001, "Testuser", "123456"),
(002, "jene", "2"),
(003, "jester", "51"),
(004, "jenny", "234"),
(005, "june", "245")
'''
cursor.execute(query)

#add categories
query = '''INSERT INTO categories VALUES (001, "Clothes"),
(002, "Electronics")
'''
cursor.execute(query)

#add products
query = '''INSERT INTO products VALUES (001, "Apple tv", "2", 3333, 002),
(002, "Black hoddies", "5", 29, 001)
'''
cursor.execute(query)




#get all data
cursor.execute('SELECT * FROM users')
data = cursor.fetchall()
print("data:", data)

#get data to match conditions
query = 'SELECT * FROM users WHERE USERNAME == "Testuser"'
cursor.execute(query)
data = cursor.fetchall()
print("data:", data)

#to update
query = 'UPDATE users SET username = "tonton", password = "1212" WHERE id == 001'
cursor.execute(query)

#delete
query = 'DELETE FROM users WHERE id == 001'
cursor.execute(query)

#get all data
cursor.execute('SELECT * FROM users')
data = cursor.fetchall()
print("data:", data)


#join table and print out all data from both table
query = 'SELECT p.name, p.price, c.name FROM products p LEFT JOIN categories c ON p.categoriesID = c.id'
cursor.execute(query)
data = cursor.fetchall()
print('product with category:', data)