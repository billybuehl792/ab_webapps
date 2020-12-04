# models.py - database structure

from ab_site import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'User("{self.username}", "{self.email}")'


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), unique=True, nullable=False)
    lname = db.Column(db.String(20), nullable=False, index=True)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.Integer)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    jobs = db.relationship('Job', backref='customer')

    def __repr__(self):
        return f'Customer("{self.fname}", "{self.lname}", "{self.address}")'


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    contract_type = db.Column(db.String(6), nullable=False)
    work_address = db.Column(db.String(40), nullable=False)
    work_city = db.Column(db.String(20), nullable=False)
    work_state = db.Column(db.String(2), nullable=False)
    work_architect = db.Column(db.String(40), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Unicode, nullable=False)
    warranty = db.Column(db.Float)
    duration = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date)
    completion_date = db.Column(db.Date)

    def __repr__(self):
        return f'Job("{self.name}", "{self.address}", \
                          "{self.address}", "{self.date_created}")'
