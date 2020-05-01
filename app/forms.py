from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
	username = StringField(u'Username', validators=[DataRequired()])
	#email =  StringField(u'Email', validators=[DataRequired()])
	password = StringField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
	
	username =  StringField(u' Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Register')


	def validate_first_name(self,frist_name):
		name = User.query.filter_by(first_name= firstname.data).first()
		if name is not None:
			raise ValidationError('Please use s different first_name') 
    
	def validate_second_name(self,second_name):
		name = User.query.filter_by(second_name= secondname.data).first()
		if name is not None:
			raise ValidationError('Please use s different second_name')     


	def validate_email(self,email):
		name = User.query.filter_by(email= email.data).first()
		if name is not None:
			raise ValidationError('Please use s different email id') 