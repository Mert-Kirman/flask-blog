from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ddfddb28228b3c27a28ccb091828b419'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.app_context().push()  # Ensure the app context is pushed for database operations

db = SQLAlchemy(app)
from flaskblog.models import User, Post # Import models to ensure they are registered with SQLAlchemy
db.create_all()  # Create database tables if they do not exist

# Import routes after initializing the app and db to avoid circular imports.
# Importing routes here allows the app to be aware of the routes defined in routes.py.
from flaskblog import routes