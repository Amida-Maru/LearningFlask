from backend import app
from flask import render_template
from backend.db_modeles import Item
from backend.forms import  RegisterForm
from backend.forms import LoginForm
from backend.db_modeles import User
from backend import db
from flask import redirect
from flask import url_for
from flask import flash #This is needed to display error msgs to the end-users


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


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        #This takes the data provided in the form and adds it to the database
        add_new_user = User(username=form.username.data,
                                   email_address=form.email_address.data,
                                   password=form.password.data)
        db.session.add(add_new_user)
        db.session.commit()
        return redirect(url_for('shop_page'))
    if form.errors != {}: #If there are errors from validation
        for error in form.errors.values():
           flash(f'There was an error:  {error}', category="danger")
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)
