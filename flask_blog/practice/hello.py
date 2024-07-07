from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "<h1>Hello World<h1>"

@app.route("/<name>")
def hello(name):
    return f"Hello,{escape(name)}!"

@app.route("/about")
def about():
    return "<p>I am Sneha<p>"



@app.route("/about/profile")
def profile():
    return "<p>I am a Computer Scientist<p>"



@app.route("/user/<username>")
def showprofile(username):
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def showPost(post_id):
    return f"post{post_id}"
