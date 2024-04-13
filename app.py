from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
conn =sqlite3.connect('questions.db', check_same_thread= False)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

@app.route("/", methods =['GET', 'POST'])
def SignInPage():
    if request.method == 'POST':
        print('POST')
        username = request.form['username']
        password = request.form['password']
        print(('signing in ... username:' + username + ', password: ' + password))

        query = "SELECT * FROM users WHERE username== '" + username + "' AND password== '" + password + "'"
        cursor.execute(query)

        user = cursor.fetchall()
        if (len(user) > 0):
            print("Sign in successful")
            return redirect(url_for('ProductPage'))
        else:
            print("No user found")

    return render_template('signin.html')


@app.route("/products")
def ProductPage ():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')

    rows = cursor.fetchall()
    print("Rows", rows)

    return render_template('ProductPage.html', rows= rows)

@app.route("/categories")
def CategoryPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categories')

    rows = cursor.fetchall()
    print("Rows", rows)

    return render_template('CategoriesPage.html', rows= rows)

@app.route("/users")
def UserPage():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')

    rows = cursor.fetchall()
    print("Rows", rows)

    return render_template('UserPage.html', rows= rows)



@app.route("/products/delete/<id>")
def deleteEntry(id):
    print('delete:' + id)
    query = 'DELETE FROM products WHERE id ==' + id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('ProductPage'))

@app.route("/categories/delete/<id>")
def deleteCategory(id):  
    print('delete:' + id)
    query = 'DELETE FROM categories WHERE id ==' + id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('CategoryPage'))

@app.route("/users/delete/<id>")
def deleteUser(id):  
    print('delete:' + id)
    query = 'DELETE FROM users WHERE id ==' + id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('UserPage'))



@app.route("/products/edit/<id>", methods = ['GET', 'POST'])
def EditProductPage(id):
    # query = 'SELECT * FROM products WHERE id == ' + id
    # cursor.execute(query)
    # product = cursor.fetchall()[0]
    # conn.commit()

    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantities']

        query = 'UPDATE products SET name="' + name + '", price=' + price + ", quantities=" + quantity + " WHERE id==" + id

        print("---------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("ProductPage"))

    return render_template('EditProductPage.html', id = id)

@app.route("/categories/edit/<id>", methods = ['GET', 'POST'])
def EditCategoriesPage(id):

    if request.method == "POST":
        name = request.form['name']

        query = 'UPDATE categories SET name="' + name + '" WHERE id==' + id

        print("---------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("CategoryPage"))

    return render_template('EditCategoriesPage.html', id = id)

@app.route("/users/edit/<id>/<type>", methods = ['GET', 'POST'])
def EditUser(id, type):
    if request.method == "POST":
        if type == 'USERNAME':
            username = request.form['username']
            query = 'UPDATE users SET username="' + username + '" WHERE id==' + id

        elif type == 'PASSWORD':
            password = request.form['password']
            query = 'UPDATE users SET password="' + password + '" WHERE id==' + id

        print("---------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("UserPage"))

    return render_template('EditUserPage.html', id = id, type = type)



@app.route("/products/add", methods = ['GET', 'POST'])
def AddProductPage():  
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantities']

        query = 'INSERT INTO products (name, price, quantities) VALUES ("' + name + '", ' + quantity + ', ' + price + ')'

        print("---------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("ProductPage"))

    return render_template('EditProductPage.html')

@app.route("/categories/add", methods = ['GET', 'POST'])
def AddCategoryPage():  
    if request.method == "POST":
        name = request.form['name']

        query = 'INSERT INTO categories (name) VALUES ("' + name + '")'

        print("---------QUERY:"+query)
        cursor.execute(query)
        conn.commit()
        return redirect(url_for("CategoryPage"))

    return render_template('EditCategoriesPage.html')