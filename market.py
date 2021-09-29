from flask import Flask, render_template

app = Flask(__name__)

#First decorator this will s
@app.route("/home")
@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/register")
def register_page():
    return render_template('register.html')

@app.route("/login")
def login_page():
    return render_template('login.html')
