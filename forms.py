from flask_wtf import Form
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please enter your first name")])
	last_name = StringField('Last Name', validators=[DataRequired("Please enter your last name")])
	email = StringField('Email', validators=[DataRequired("Please enter your email address"),Email("Please use a valid email format")])
	password = PasswordField('Password', validators=[DataRequired("Please choose a password"),Length(min=6, message="Password too short")])
	submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("Please enter email"),Email("Please enter valid email")])
	password = PasswordField('Password',validators=[DataRequired("Please enter password")])
	submit = SubmitField("Sign in")

class AddressForm(Form):
	address = StringField('Address', validators=[DataRequired("Please enter an address.")])
	submit = SubmitField("Search")
	