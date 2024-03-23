from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def HomePage ():

    return render_template('signin.html')

@app.route("/products")
def ProductPage ():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')

    rows = cursor.fetchall()
    print("Rows", rows)

    return render_template('ProductPage.html', row = rows)

@app.route("/categories")
def CategoryPage ():

    return render_template('CategoriesPage.html')