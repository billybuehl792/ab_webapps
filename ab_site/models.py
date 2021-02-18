# models.py - database structure

from ab_site import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'User("{self.username}", "{self.email}")'


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    f_name = db.Column(db.String(32), nullable=False)
    m_name = db.Column(db.String(32), nullable=False)
    l_name = db.Column(db.String(32), nullable=False, index=True)
    phone_0 = db.Column(db.Integer, nullable=False)
    phone_1 = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(128), nullable=True)
    address = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(32), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(2), nullable=False)
    jobs = db.relationship('Job', backref='customer')

    def __repr__(self):
        return f'Customer("{self.f_name}", "{self.m_name}", "{self.l_name}", "{self.phone_0}")'


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    contract_type = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(32), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(2), nullable=False)
    work_address = db.Column(db.String(128), nullable=True)
    work_city = db.Column(db.String(32), nullable=True)
    work_zip = db.Column(db.Integer, nullable=True)
    work_state = db.Column(db.String(2), nullable=True)
    work_architect = db.Column(db.String(32), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Unicode, nullable=False)
    warranty = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Float, nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    completion_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'Job("{self.id}", "{self.public_id}")'
