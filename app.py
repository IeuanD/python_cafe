from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3 import Error
DATABASE = "C:/Users/19163/OneDrive - Wellington College/13DTS/Flask Project/Smile/smile.db"
app = Flask(__name__)

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

@app.route('/')
def render_homepage():
    return render_template('home.html')

@app.route('/menu/<cat_id>')
def render_menu_page(cat_id):
    con = create_connection(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products WHERE cat_id =?"
    cur = con.cursor()
    cur.execute(query, (1,))
    product_list = cur.fetchall()
    con.close()
    print(product_list)
    return render_template('menu.html', products=product_list)

@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


@app.route('/login', methods=['POST', 'GET'])
def render_login():
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def render_signup():
    if request.method == 'POST':
        print(request.form)
        fname = request.form.get('fname')
        lname= request.form.get('lname')
        email = request.form.get('email').lower().strip()
        password = request.form.get('password')
        password2 = request.form.get('password2')

    return render_template('signup.html')


app.run(host='0.0.0.0', debug=True)
