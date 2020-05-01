from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
#app.run(debug=True)
login_manager = LoginManager(app)
login_manager.login_message = u'Please log in to access this page'
login_manager.login_view = 'login'
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)



from app import routes, models