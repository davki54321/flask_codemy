
from flask import Flask, render_template

# Create flask instance
# This helps flask find files in directory
app = Flask(__name__)

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