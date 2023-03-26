# from app import app
from flask_sqlalchemy import SQLAlchemy
from config import Config

debug = False
if debug: print("database.py: SQLAlchemy imported.")

db = SQLAlchemy()

def init_app(app):
    if debug: print("database.py: Initializing database...")
    db.init_app(app)
    if debug: print("database.py: Database initialized.")


def create_tables(app):
    if debug: print("database.py: Creating database tables...")
    # with app.app_context():
    db.create_all()
    if debug: print("database.py: Database tables created.")

# from models import User
# # Create a new user
# username = "Corey"
# password = "0000"
# user = User(username=username, password_hash=password)
# db.session.add(user)
# db.session.commit()