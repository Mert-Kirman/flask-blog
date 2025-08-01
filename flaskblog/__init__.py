from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ddfddb28228b3c27a28ccb091828b419'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # type: ignore
login_manager.login_message_category = 'info'

# Import routes after initializing the app and db to avoid circular imports.
# Importing routes here allows the app to be aware of the routes defined in routes.py.
from flaskblog import routes