from backend import app
from flask import Blueprint,render_template,request,redirect,flash,url_for
from flask import render_template
from backend.db_modeles import User, Note
from backend import db
from backend.forms import RegisterForm
from backend.forms import LoginForm
from flask import redirect, request, session, current_app
from flask import url_for
from flask import flash  # This is needed to display error msgs to the end-users
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user
from datetime import timedelta
from backend.db_modeles import Note

views = Blueprint('views',__name__)

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


@app.route('/account.html',methods=['GET','POST'])
@login_required
def account_page():
    form = LoginForm()
    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short, please write in detail !!!', category="error")
        else:
            new_note = Note(title=title, text=note, user_id=current_user.id)

            db.session.add(new_note)
            db.session.commit()
            flash(' your note is added', category='success')
            print("Note added")
    return render_template('account.html', form=form)



@views.route("/all-users")
@login_required
def allUsers():
    all_users=User.query.all()
    var=[]
    for user in all_users:
        notes=Note.query.filter_by(user_id=user.id).all()
        if len(notes)>0:
            var.append(len(notes))
        else:
            var.append(0)
    zipped=zip(all_users,var)


    return render_template("showusers.html",all_users=zipped,user=current_user)


@views.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def deleteNote(id):
    note = Note.query.filter_by(id=id).first()
    if note:
        db.session.delete(note)
        db.session.commit()
        flash("your note is successfully deleted", category="success")
    return render_template("index.html",user=current_user)

@views.route('/update/<int:id>',methods=['GET','POST'])
@login_required
def updateNote(id):
    if request.method == 'POST':
        title=request.form['title']
        text=request.form['note']
        note = Note.query.filter_by(id=id).first()
        note.title=title
        note.text=text
        db.session.add(note)
        db.session.commit()
        return render_template("index.html",user=current_user)

    note_update = Note.query.filter_by(id=id).first()
    return render_template("update.html",nu=note_update,user=current_user)

@views.route("/details/<int:id>",methods=['GET','POST'])
@login_required
def details(id):
    note_update = Note.query.filter_by(id=id).first()
    return render_template("details.html",nu=note_update,user=current_user)



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