from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    def __repr__(self):
        return f'<User {self.username}>'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password) 
      
    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True


class Customer(db.Model):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True)
    name_first = Column(String)
    name_Last = Column(String)
    email = Column(String, unique=True, index=True)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship('Subscription', back_populates='customers')
    accesses = relationship('Access', back_populates='customer')
    
    def __repr__(self):
        return f'<Customer {self.email}>'

class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)
    duration = Column(String)
    tiers = relationship('SubscriptionTier', back_populates='subscription')
    customers = relationship('Customer', back_populates='subscription')

    def __repr__(self):
        return f'<Subscription {self.name}>'

class SubscriptionTier(db.Model):
    __tablename__ = 'subscription_tiers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    duration = Column(String)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship('Subscription', back_populates='tiers')
    accesses = relationship('Access', back_populates='tier')

    def __repr__(self):
        return f'<Subscription Tier {self.name}>'

class Platform(db.Model):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    accesses = relationship('Access', back_populates='platform')

    def __repr__(self):
        return f'<Platform {self.name}>'

class Access(db.Model):
    __tablename__ = 'accesses'
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='accesses')
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    platform = relationship('Platform', back_populates='accesses')
    tier_id = Column(Integer, ForeignKey('subscription_tiers.id'))
    tier = relationship('SubscriptionTier', back_populates='accesses')
    lifetime_access = Column(Boolean)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, default=datetime.utcnow() + timedelta(days=30))
    
    def __repr__(self):
        return f'<Access {self.platform}>'
