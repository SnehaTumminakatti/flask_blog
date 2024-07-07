from flask import *
app = Flask(__name__)
from forms import RegistrationForm,LoginForm

app.config['secret'] = '613f383654f1c681c84966f1c369f3da'

posts = [
    {
        'author':'Sneha Tumminakatti',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'July 7 2024'
    },
    {
        'author':'sneha Tumminakatti',
        'title':'Blog Post 2',
        'content':'First post content',
        'date_posted':'July 8 2024'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts,title='1')

@app.route('/about')
def about():
    return render_template("about.html",title='about')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html",title='register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html",title='login',form=form)


if __name__ == '__main__':
    app.run(debug = True)