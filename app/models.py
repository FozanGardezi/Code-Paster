from app import db
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager

class Code(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	code = db.Column(db.String(1000))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


	def __init__(self,code,user_id):
		self.code = code
		self.user_id = user_id


class User(UserMixin,db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer,primary_key=True)
	Username = db.Column(db.String(64),index=True,unique=True)
	email = db.Column(db.String(64),index=True,unique=True)
	password_hash = db.Column(db.String(128))
	codes = db.relationship('Code',backref='owner',lazy='dynamic') 

	def set_password(self,password):
		self.password_hash = generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self.password_hash,password)


	

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))