







#This version works without structure


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import app 
from backend.db_models import Item



app = Flask(__name__, template_folder='templates', static_folder='images')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





#First decorator

@app.route("/home")
@app.route("/")
def home_page():
    return render_template('home.html')


@app.route("/shop")
def shop_page():
    items = Item.query.all()
    return render_template('shop.html', items=items)


@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route("/account")
def account_page():
    return render_template('account.html')


@app.route("/register")
def register_page():
    return render_template('register.html')


@app.route("/login")
def login_page():
    return render_template('login.html')


