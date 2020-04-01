from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SaveCodeForm(FlaskForm):
	code = StringField('Code', validators=[DataRequired()])
