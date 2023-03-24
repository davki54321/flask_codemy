
from flask import Flask, render_template, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo
import sqlalchemy
from datetime import datetime


# Create flask instance
# This helps flask find files in directory
app = Flask(__name__)

# Creates secret key for CSRF token
app.config['SECRET_KEY'] = "41094a4ad7b210551598a12ee3ae58a9"


# Create form class
class RegisterForm(FlaskForm):

    # first argument (i.e. "Name:") after objects (StringField, etc) is used for label element in html
    # second argument is a list (validators) of classes from wtform.validators
    name = StringField("Name:", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    confirm_pw = PasswordField("Confirm password:", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")


    # Create form class
class LoginForm(FlaskForm):

    # first argument (i.e. "E-mail:") after objects (StringField, etc) is used for label element in html
    # second argument is a list (validators) of classes from wtform.validators
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


# add database
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://users.db"
# TODO


# Create a route decorator
@app.route('/')
def index():
    return render_template("index.html",
                           title="home")


#localhost:5000/users/david
# <var> must be the same as var name entered into function, in this name <name> (line 31) and def user(name) (line 32)
@app.route('/users/<name>')
def user(name):
    return render_template("user.html", 
                            title="User Profile",
                            name=name)


# Invalid URL
@app.errorhandler(404)
# variable "e" is for error
def page_not_found(e):
    # 404 at end of line 40 will get pass to "page_not_found(e)"
    return render_template("404.html", title="Error:404"), 404


# Internal Server Errror
@app.errorhandler(500)
# variable "e" is for error
def page_not_found(e):
    # 500 at end of line 40 will get pass to "page_not_found(e)"
    return render_template("500.html", title="Error:500"), 500


# Registration form
@app.route('/registration', methods=["GET", "POST"])
def register():
    # name set to none so first time page is loaded different message appears (in the jinja code)
    name = None
    form = RegisterForm()
    # Validates form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Account created successfully!", "success")
        return redirect(url_for("index"))

    return render_template("registration.html",
                            title="Registration",
                            name = name,
                            form = form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Logged in successfully!", "success")
        return redirect(url_for("index"))

    return render_template("login.html",
                            title="Login",
                            form = form)    

