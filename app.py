
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create form class
class NameForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create flask instance
# This helps flask find files in directory
app = Flask(__name__)
# Creates secret key
app.config['SECRET_KEY'] = "somethingsomething"

# Create a route decorator
@app.route('/')
# def index():
#     return "<h1>hello world!!!</h1>"

def index():
    return render_template("index.html")


#localhost:5000/users/david
# <var> must be the same as var name entered into function
@app.route('/users/<name>')
def user(name):
    return render_template("user.html", name=name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Errror
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Name form
@app.route('/name_form', methods=["GET", "POST"])
def name_form():
    name = None
    form = NameForm()
    # Validates form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""

    return render_template("name_form.html",
                            name = name,
                            form = form)
