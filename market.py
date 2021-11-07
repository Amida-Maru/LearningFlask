from flask import Flask, render_template


app = Flask(__name__)



items=[
        {'id': 1, 'name': 'Phone', 'barcode': '10', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '11', 'price': 1200},
        {'id': 3, 'name': 'Speaker', 'barcode': '12', 'price': 100},
        {'id': 4, 'name': 'Tablet', 'barcode': '13', 'price': 300}
    ]


#First decorator

@app.route("/home")
@app.route("/")
def home_page():


    return render_template('home.html')


@app.route("/shop")
def shop_page():
    return render_template('shop.html', items=items)


@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route("/account")
def account_page():
    return render_template('account.html')


@app.route("/register")
def register_page():
    return render_template('register.html')


@app.route("/login")
def login_page():
    return render_template('login.html')


