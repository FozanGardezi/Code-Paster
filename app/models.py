from app import db

class Code(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	code = db.Column(db.String(1000),index = True)

	def __repr__(self):
		return '<Code {}>'.format(self.code)

	def __init__(self,code):
		self.the_code = code