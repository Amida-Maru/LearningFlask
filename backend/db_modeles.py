from backend import db
from backend import bcrypt
from backend import login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func
# noinspection PyUnresolvedReferences


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=32), nullable=False, unique=True)
    email_address = db.Column(db.String(length=64), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=512), nullable=False)
    notes = db.relationship('Note')



    @property
    def password(self):
        return self.password

    #This setter takes the plain password from a user and using the bcrypt.generate method creates a secure hash
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_login(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    text = db.Column(db.String(128))
    category = db.Column(db.String(32))
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f'User {self.name}'

