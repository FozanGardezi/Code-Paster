from app import app,db
from flask import render_template, redirect, request, url_for
from app.forms import SaveCodeForm
from app.models import Code




@app.route('/')
@app.route('/index')
def index():
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
	return render_template('index.html',title='home',user=user,posts=posts, code = Code.query.all())

@app.route('/savecode',methods=['POST','GET'])
def	savecode():
	form = SaveCodeForm()
	if request.method == "POST":
		code_recieved = request.form["code"]
		print(code_recieved)
		cd = Code(code = code_recieved)
		
		db.session.add(cd)
		db.session.commit()
		return redirect(url_for('index'))
		#return redirect(url_for("user",cd = code))
	else:
		return render_template("savecode.html")
	'''
	if form.validate_n_submit():
		flash('code save from user'.format(
			form.code.data))
		return redirect('/index')
	'''
	#return render_template('savecode.html',title='Save Code',form =form)
