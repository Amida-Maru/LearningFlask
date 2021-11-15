from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

# location of the template folder and the static path for images
app = Flask(__name__, template_folder='templates', static_folder='images')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from backend import routes