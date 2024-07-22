import subprocess

from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__,template_folder='template_files')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, Email, Password, Name):
        self.Name = Name
        self.Email = Email
        self.Password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, Password):
        return bcrypt.checkpw(Password.encode('utf-8'), self.Password.encode('utf-8'))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    if request.method == 'POST':
        email = request.form['Email']
        password = request.form['Password']

        user = User.query.filter_by(Email=email).first()
        if user and user.check_password(password):
            session['Email'] = user.email
            return redirect('/homepage')
        else:
            return render_template('login.html', error='Invalid user')
    return render_template("login.html")
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # # handle request
        # name = request.form['Name']
        # email = request.form['Email']
        # password = request.form['Password']
        # print(name)
        new_user = User(Name="yash", Email="yash123@gmail.com", Password="223")
        db.session.add(new_user)
        db.session.commit()
        return redirect('/home')
    return render_template("register.html")
@app.route('/my-link/')
def my_link():
    return subprocess.run(["python","notepad.py"],capture_output=True,text=True)
@app.route("/")
def close_notepad():
    return render_template('homepage.html')
@app.route("/forgotpass")
def forgotpass():
    return render_template("t.html")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")
@app.route("/img")
def img():
    return render_template("img.html")
if __name__=="__main__":
    app.run(debug=True)

# from flask import Flask, request, render_template, redirect, session
# from flask_sqlalchemy import SQLAlchemy
# import bcrypt
#
# app = Flask(__name__,template_folder='template_files')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)
# app.secret_key = 'secret_key'
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#
#     def __init__(self, Email, Password, Name):
#         self.Name = Name
#         self.Email = Email
#         self.Password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#
#     def check_password(self, Password):
#         return bcrypt.checkpw(Password.encode('utf-8'), self.Password.encode('utf-8'))
#
#
# with app.app_context():
#     db.create_all()
#
#
# @app.route('/')
# def home():
#     return render_template('login.html')
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # handle request
#         name = request.form['Name']
#         email = request.form['Email']
#         password = request.form['Password']
#
#         new_user = User(Name=name, Email=email, Password=password)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect('/login')
#
#     return render_template('register.html')
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['Email']
#         password = request.form['Password']
#
#         user = User.query.filter_by(Email=email).first()
#
#         if user and user.check_password(Password):
#             session['Email'] = user.Email
#             return redirect('/homepage')
#         else:
#             return render_template('login.html', error='Invalid user')
#
#     return render_template('login.html')
# @app.route("/forgotpass")
# def forgotpass():
#     return render_template("t.html")
#
# @app.route('/homepage')
# def homepage():
#     if session['Email']:
#         user = User.query.filter_by(email=session['Email']).first()
#         return render_template('homepage.html', user=user)
#
#     return redirect('/login')
#
# if __name__ == '__main__':
#     app.run(debug=True)