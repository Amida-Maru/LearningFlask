from backend import app
from flask import render_template
from backend.db_modeles import User
from backend import db
from backend.forms import RegisterForm
from backend.forms import LoginForm
from flask import redirect, request, session, current_app
from flask import url_for
from flask import flash  # This is needed to display error msgs to the end-users
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from datetime import timedelta


@app.route("/")
@app.route("/landing_page")
def landing_page():
    return render_template('landing_page.html')


@app.route("/home")
def home_page():
    return render_template('index.html')


@app.route("/about_game.html")
def about_game():
    return render_template('about_game.html')


@app.route("/game_glossary.html")
def game_glossary():
    return render_template('game_glossary.html')


@app.route("/about_esports.html")
def about_esports():
    return render_template('about_esports.html')


@app.route("/esports_glossary.html")
def esports_glossary():
    return render_template('esports_glossary.html')


@app.route("/useful_websites.html")
def useful_websites():
    return render_template('useful_websites.html')

@app.route("/lolfandom.html")
def lolfandom():
    return render_template('lolfandom.html')

@app.route("/lolesports.html")
def lolesports():
    return render_template('lolesports.html')

@app.route("/lolpros.html")
def lolpros():
    return render_template('lolpros.html')




@app.route("/account.html")
@login_required
def account_page():
    form = LoginForm()
    return render_template('account.html', form=form)


@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('wrong_url.html'), 404


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_login(attempted_password=form.password.data):
            login_user(attempted_user, remember=True, duration=timedelta(seconds=300))
            flash(f"You are logged in as: {attempted_user.username}", category="success")
            return redirect(url_for("account_page"))
        else:
            flash('The entered credentials seem incorrect, please try again', category="danger")
    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # This takes the data provided in the form and adds it to the database
        add_new_user = User(username=form.username.data, email_address=form.email_address.data,
                            password=form.password.data)
        db.session.add(add_new_user)
        db.session.commit()
        login_user(add_new_user, remember=True, duration=timedelta(seconds=300))
        flash(f"Account has been created, you are now logged in as: {add_new_user.username}", category="success")
        return redirect(url_for('account_page'))
    if form.errors != {}:  # If there are errors from validation
        for error in form.errors.values():
            flash(f'There was an error:  {error}', category="danger")
    return render_template('register.html', form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))