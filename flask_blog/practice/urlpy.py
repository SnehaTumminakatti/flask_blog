from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f"{username}\s Profile"

# @app.route("/<name>")
# def hello(name):
#     return f"Hello,{escape(name)}!"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='sneha'))
if __name__ == '__main__':
    app.run(debug=True)
