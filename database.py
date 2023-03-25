from flask_sqlalchemy import SQLAlchemy
from flask import current_app

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    
def create_tables():
    from .models import User, Subscription, SubscriptionTier, Platform, Access
    db.create_all()

def drop_tables():
    from .models import User, Subscription, SubscriptionTier, Platform, Access
    db.drop_all()