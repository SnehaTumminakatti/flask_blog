from flask import FlaskForm
from wtforms import StringFeild,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringFeild('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringFeild('Email',validators=[DataRequired(),Email()])
    password = StringFeild('Password',validators = [DataRequired()])
    confirm_password = StringFeild('Confirm Password',validators =[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringFeild('Email',validators=[DataRequired(),Email()])
    password = StringFeild('Password',validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')