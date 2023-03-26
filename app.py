from flask import Flask, render_template, request, redirect, url_for, flash
from models import User, Subscription, SubscriptionTier, Platform, Access
from database import init_app, create_tables

from config import Config

app = Flask(__name__, static_url_path='/static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config.from_object(Config)

# Initialize the database
init_app(app)

# Create the database tables
# create_tables()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # TODO: Implement authentication logic
        return redirect(url_for('dashboard'))
    return render_template('login.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    # TODO: Implement dashboard logic
    return render_template('dashboard.html')

# Subscription page
@app.route('/subscriptions')
def subscriptions():
    # TODO: Implement subscriptions logic
    return render_template('subscriptions.html')
  
# Profile page
@app.route('/profile')
def profile():
    # TODO: Implement profile logic
    return render_template('profile.html')

# Settings page
@app.route('/settings')
def settings():
    # TODO: Implement settings logic
    return render_template('settings.html')

# Logout functionality
@app.route('/logout')
def logout():
    # TODO: Implement logout logic
    return redirect(url_for('index.html'))
  
# Register page
@app.route('/register')
def register():
    # TODO: Implement register logic
    return render_template('register.html')
  
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
      # Create the database tables
      create_tables()
    app.run(debug=True)
    # app.run(host='0.0.0.0', port='5000', debug=True)
