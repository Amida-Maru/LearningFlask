from backend import app
from flask import render_template
from backend.db_modeles import Item
from backend.forms import  RegisterForm
from backend.forms import LoginForm


@app.route("/home")
@app.route("/")

def home_page():
    return render_template('home.html')


@app.route("/shop")
def shop_page():
    # This provides data from the database
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
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route("/login")
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)
