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

@app.route("/products/delete/<id>")
def deleteEntry(id):
    print('delete:' + id)
    query = 'DELETE FROM products WHERE id ==' + id
    cursor.execute(query)
    conn.commit()
    return redirect(url_for('ProductPage'))

@app.route("/categories")
def CategoryPage ():

    return render_template('CategoriesPage.html')