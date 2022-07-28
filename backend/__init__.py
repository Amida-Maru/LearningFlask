from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# location of the template folder and the static path for images
# ../ that means that I go to the previous directory so from back end to NippsProject
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_users.db'
app.config['SECRET_KEY'] = 'dcb9e4c5437c6fe45a21a96bba02e3550971477f924a32d984e3f5c6cc73a1e9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# login_manager.session_protection = "strong"
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from backend import routes
