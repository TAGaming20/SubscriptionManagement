from app import db
from app.models import User, Subscription, Plan, Platform, Access
from datetime import datetime, timedelta

def create_user(email, password, role):
    """Create a new user"""
    user = User(email=email, password=password, role=role)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    """Get a user by email"""
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id):
    """Get a user by id"""
    return User.query.get(user_id)

def create_subscription(user, username, plan_name, start_date, end_date, payment_status, payment_transaction_id):
    """Create a new subscription"""
    plan = Plan.query.filter_by(name=plan_name).first()
    subscription = Subscription(username=username, plan=plan_name, start_date=start_date, end_date=end_date,
        payment_status=payment_status, payment_transaction_id=payment_transaction_id, user=user)
    db.session.add(subscription)
    db.session.commit()
    return subscription

def get_subscription_by_id(subscription_id):
    """Get a subscription by id"""
    return Subscription.query.get(subscription_id)

def get_subscription_by_username(username):
    """Get a subscription by username"""
    return Subscription.query.filter_by(username=username).first()

def get_active_subscriptions():
    """Get all active subscriptions"""
    return Subscription.query.filter(Subscription.end_date > datetime.utcnow(), Subscription.payment_status == 'paid').all()

def get_expired_subscriptions():
    """Get all expired subscriptions"""
    return Subscription.query.filter(Subscription.end_date < datetime.utcnow()).all()

def get_subscription_metrics():
    """Get subscription metrics"""
    active_subscriptions = get_active_subscriptions()
    expired_subscriptions = get_expired_subscriptions()
    subscriber_count = len(active_subscriptions)
    churn_rate = len(expired_subscriptions) / (len(active_subscriptions) + len(expired_subscriptions))
    revenue = sum([s.plan.price for s in active_subscriptions])
    return subscriber_count, churn_rate, revenue

def create_plan(name, price, platforms):
    """Create a new plan"""
    plan = Plan(name=name, price=price)
    for platform in platforms:
        plan_platform = Platform(name=platform, plan=plan)
        db.session.add(plan_platform)
    db.session.add(plan)
    db.session.commit()
    return plan

def get_plan_by_name(name):
    """Get a plan by name"""
    return Plan.query.filter_by(name=name).first()

def create_access(subscription, platform, tier=None):
    """Create a new access"""
    access = Access(subscription=subscription, platform=platform, tier=tier)
    db.session.add(access)
    db.session.commit()
    return access

def revoke_access(subscription, platform):
    """Revoke access"""
    access = Access.query.filter_by(subscription=subscription, platform=platform).first()
    db.session.delete(access)
    db.session.commit()

def get_accesses_by_subscription(subscription):
    """Get all accesses for a subscription"""
    return Access.query.filter_by(subscription=subscription).all()