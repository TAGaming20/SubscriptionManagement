from flask import render_template, request, redirect, url_for, flash
from models import User, Customer, Subscription, SubscriptionTier, Platform, Access
from app import app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

debug = False
if debug: print("route.py: Routes imported.")

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Redirect to login page if not logged in
@app.before_request
def require_login():
    protected_routes = ['dashboard', 'subscriptions', 'profile', 'settings', 'logout', 'home']
    if request.endpoint in protected_routes and not current_user.is_authenticated:
        return redirect(url_for('login'))
      
    if request.endpoint == 'login' and current_user.is_authenticated:
        return redirect(url_for('home'))

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))

    return render_template('login.html')

# Index page
@app.route('/')
def index():
    # print("index.html")
    return render_template('index.html')

# Home page
@app.route('/home')
@login_required
def home():
    # print("home.html")
    return render_template('home.html')

# Dashboard page
@app.route('/dashboard')
@login_required
def dashboard():
    # TODO: Implement dashboard logic
    return render_template('dashboard.html')

# Subscription page
@app.route('/subscriptions')
@login_required
def subscriptions():
    # TODO: Implement subscriptions logic
    return render_template('subscriptions.html')
  
# Profile page
@app.route('/profile')
@login_required
def profile():
    # TODO: Implement profile logic
    return render_template('profile.html')

# Settings page
@app.route('/settings')
@login_required
def settings():
    print("settings.html")
    # TODO: Implement settings logic
    return render_template('settings.html')

# Logout functionality
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    # TODO: Implement logout logic
    return redirect(url_for('index'))
  
@app.errorhandler(404)
def page_not_found(e):
    return render_template(url_for('404')), 404