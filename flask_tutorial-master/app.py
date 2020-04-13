from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pastes.db'
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Pastes = Base.classes.Pastes


@app.route('/')
def index():
    result = db.session.query(Pastes).all()
    return render_template('base.html', result=result)


if __name__ == '__main__':
    app.run()
