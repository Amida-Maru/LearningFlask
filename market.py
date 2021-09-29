from flask import Flask, render_template

app = Flask(__name__)

#First decorator this will s
@app.route("/home")
@app.route("/")

def hello_page():
    return render_template('home.html')


