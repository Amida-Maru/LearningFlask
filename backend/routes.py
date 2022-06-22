from backend import app
from flask import render_template


@app.route("/home")
@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/about_game.html")
def about_game():
    return render_template('about_game.html')


@app.route("/about_esports.html")
def about_esports():
    return render_template('about_esports.html')


@app.route("/useful_websites.html")
def useful_websites():
    return render_template('useful_websites.html')


@app.route("/account.html")
def account_page():
    return render_template('account.html')


@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('wrong_url.html'), 404
