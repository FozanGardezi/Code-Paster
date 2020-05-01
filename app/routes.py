from app import app,db
from flask import render_template, redirect, request, url_for, g, flash, session
from app.forms import LoginForm, RegistrationForm
from app.models import Code,User
from flask_login import current_user , login_user, login_required
from sqlalchemy import text



@app.route('/')
@app.route('/index')
# @login_required
def index():
	if "email" in session:

		user = {'username': 'Miguel'}
		posts = [
	        {
	            'author': {'username': 'John'},
	            'body': 'Beautiful day in Portland!'
	        },
	        {
	            'author': {'username': 'Susan'},
	            'body': 'The Avengers movie was so cool!'
	        }
	    ]
		#print("hello")
		return render_template('index.html',title='home',user=user,posts=posts, code = Code.query.all())
	else:
		return redirect(url_for('login'))

@app.route('/savecode',methods=['POST'])
def	savecode():
	code_recieved = request.form["code"]
	print(code_recieved)
	userid = session['id']
	cd = Code(code_recieved,user_id=userid)
	print(cd)
	db.session.add(cd)
	db.session.commit()
	return redirect(url_for('index'))
	#return redirect(url_for("user",cd = code))
		
@app.route('/renderSaveCode', methods=['GET'])
# @login_required
def renderSaveCode():
	if "email" in session:
		return render_template("savecode.html")
	return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['psw']
		usr = User(Username = username,email = email)
		usr.set_password(password)
		
		db.session.add(usr)
		db.session.commit()
		return redirect(url_for('login'))
	else:
		return render_template('register.html',title= 'Register')

@app.route('/login',methods=['GET','POST'])
def login():

	if "email" in session:
		return redirect(url_for('index'))

	if request.method == 'POST':
		email = request.form["email"]
		password =  request.form["psw"]
		print(email,password)
		
		#mail = User.query.get(email)
		#psw = User.query.get(password)
		#get = User.query.get(1)
		the_mail= User.query.filter_by(email=email).first()
		pas = User.query.filter_by(password_hash=password)
		#mail = db.session.query(User).filter(text(email)).all()
		#psw = db.session.query(User).filter(text(password))

		'''
		for mail in the_mail:
			print(mail)
			if mail.email == email:
		 		email_found = mail.email
		 		print(email_found)
		

		for p in pas:
			print(p)
			if p.password_hash == the_mail.check_password(password):
		 		password_found = password
		 		print(password_found)
		#print(str(mail),str(psw),str(the_mail))
		if email == email_found and password == password_found:
			return redirect(url_for('index'))
		else:
			print("hello")
			flash('invlaid username or password')
			return redirect(url_for('login'))

		'''
		print(the_mail.email)
		print(the_mail.password_hash)
		if the_mail is None or not the_mail.check_password(password):
			print('invlaid')
			flash('invlaid username or password')
			return redirect(url_for('login'))
		session['email'] = request.form["email"]
		session['id'] = the_mail.id
		next_arg = request.args.get('next')
		if not next_arg or url_parse(next_arg).netloc != '':
			next_arg = url_for('index')
		return redirect(next_arg)
	else:
		return render_template('login.html',title="Login")

@app.route('/logout')
def logout():
	#Slogout_user()
	session.pop('email',None)
	return redirect(url_for('login'))

@app.route('/wtforms-login', methods=['GET','POST'])
def wtformlogin():
	form = LoginForm()
	
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if form.validate_on_submit():
		user = User.query.filter_by(Username=form.username.data).first()
		print(user)
		if user is None or not user.check_password(form.password.data):
			flash('invlaid username or password')
			redirect(url_for('wtforms-login'))
		login_user(user)
		next_arg = request.args.get('next')
		if not next_arg or url_parse(next_arg).netloc != '':
			next_arg = url_for('index')
		return redirect(url_for(next_arg))
	print('hello')
	return render_template('wtforms-login.html',title='Sign In',form= form)

@app.route('/wtforms-register',methods=['GET','POST'])
def wtformregister():
	form = RegistrationForm()
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	if form.validate_on_submit():
		user = User(Username=form.username.data,email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Great! you are our new user')
		return redirect(url_for('login'))

	return render_template('wtforms-register.html',title= 'Register',form=form)

