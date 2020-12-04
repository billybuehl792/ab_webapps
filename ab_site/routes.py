# routes.py - routes to app pages

import json
import re
from flask import flash, url_for, redirect, render_template, request
from ab_site import app, db, bcrypt
from ab_site.forms import LoginForm, CustomerForm, JobForm
from ab_site.models import User, Customer, Job


@app.route('/')
def dashboard():
    return render_template('dashboard.html',
                           title='Dashboard')


@app.route('/calculator/')
def calculator():
    with open('ab_site/config/calcConfig.json', 'r') as f:
        data = json.load(f)
    items = data['items']
    tax = data['tax']
    return render_template('calculator.html',
                           title='Calculator',
                           items=items,
                           tax=tax)


@app.route('/customer/', methods=['GET', 'POST'])
def customer():
    form = CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # create customer object from user input data
            customer = Customer(
                                fname=str(form.fname.data).lower().replace(" ", ""),
                                lname=str(form.lname.data).lower().replace(" ", ""),
                                address=str(form.address.data).lower().replace(" ", ""),
                                city=str(form.city.data).lower().replace(" ", ""),
                                state=form.state.data,
                                zip_code=form.zip_code.data,
                                phone=re.sub("[^0-9]", "", form.phone.data),
                                email=form.email.data)

            db.session.add(customer)
            db.session.commit()
            flash('Customer Added to Database!', 'success')
            # redirect to print form
            return redirect(url_for('job'))
        else:
            flash('Customer Export Failure', 'failure')

    return render_template('customer.html', title='Customer', form=form)


@app.route('/customers/')
def customers():
    return "hey customers!"


@app.route('/job/', methods=['GET', 'POST'])
def job():
    form = JobForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(request.form)
            for i in request.form:
                print(f'{i}: {request.form[i]}')
            # add data to database
            flash('Job Submit Success!', 'success')
            # redirect to print form
            return redirect(url_for('contract'))
        else:
            flash('Job Submit Failure!', 'failure')

    return render_template('job.html', title='Job', form=form)


@app.route('/jobs/')
def jobs():
    return '<h1>Hello Jobs</h1>'


@app.route('/settings/')
def settings():
    return render_template('settings.html', title='Settings')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print('Success!')

        flash('Email or password incorrect', 'danger')

    return render_template('login.html', title='login', form=form)
