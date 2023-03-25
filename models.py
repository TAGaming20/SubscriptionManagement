from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import db

class User(db):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship('Subscription', back_populates='users')
    accesses = relationship('Access', back_populates='user')

class Subscription(db):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)
    duration = Column(String)
    tiers = relationship('SubscriptionTier', back_populates='subscription')
    users = relationship('User', back_populates='subscription')

class SubscriptionTier(db):
    __tablename__ = 'subscription_tiers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    duration = Column(String)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship('Subscription', back_populates='tiers')
    accesses = relationship('Access', back_populates='tier')

class Platform(db):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    accesses = relationship('Access', back_populates='platform')

class Access(db):
    __tablename__ = 'accesses'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='accesses')
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    platform = relationship('Platform', back_populates='accesses')
    tier_id = Column(Integer, ForeignKey('subscription_tiers.id'))
    tier = relationship('SubscriptionTier', back_populates='accesses')
    lifetime_access = Column(Boolean)