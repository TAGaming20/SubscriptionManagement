from flask import Flask
# from flask_login import LoginManager
from config import Config

debug = False

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI


# Database
from database import init_app, create_tables    
    
# Initialize the database
init_app(app)

with app.app_context():
  # Create the database tables
  create_tables(app)


from routes import *


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port='5000', debug=True)
    if debug: print("app.py: App running.")

