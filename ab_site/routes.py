# routes.py - routes to app pages

import uuid
import json
from flask import flash, url_for, redirect, render_template, request, jsonify
from sqlalchemy import or_
from ab_site import app, db, bcrypt
from ab_site.forms import CustomerForm, JobForm
from ab_site.models import User, Customer, Job


def format_phone(phone_number):
    formatted = ''
    for n in phone_number:
        if n.isdigit():
            formatted += n
    try:
        return int(formatted)
    except ValueError:
        return None

def search_customers(text_string):
    customers = db.session.query(Customer).filter(or_(
            Customer.f_name.startswith(text_string),
            Customer.l_name.startswith(text_string),
            (Customer.f_name + Customer.l_name).startswith(text_string),
            (Customer.f_name + Customer.l_name).startswith(text_string),
            (Customer.f_name + Customer.m_name + Customer.l_name).startswith(text_string)
        )).all()

    customer_list = []
    c = 0
    for customer in customers:
        customer_list.append({
            'public_id': customer.public_id,
            'name': f'{customer.f_name.capitalize()} {customer.m_name.capitalize()} {customer.l_name.capitalize()}',
            'phone': customer.phone_0,
            'address': customer.address
        })
        c += 1
        if c >= 20:
            break
    
    return customer_list

def format_string(text_string):
    return text_string.lower().replace(' ','')

@app.route('/')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


@app.route('/calculator')
def calculator():
    with open('ab_site/config/calcConfig.json', 'r') as f:
        data = json.load(f)
    items = data['items']
    tax = data['tax']

    return render_template('calculator.html', title='Calculator', items=items, tax=tax)


@app.route('/customer/new', methods=['GET', 'POST'])
def new_customer():
    form = CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            customer = Customer(
                public_id=int(uuid.uuid4().time_low),
                f_name=format_string(form.f_name.data),
                m_name=format_string(form.m_name.data),
                l_name=format_string(form.l_name.data),
                phone_0=format_phone(form.phone_0.data),
                phone_1=format_phone(form.phone_1.data),
                email=format_string(form.email.data),
                address=form.address.data,
                city=format_string(form.city.data),
                zip_code=int(form.zip_code.data),
                state=format_string(form.state.data)
            )
            try:
                db.session.add(customer)
                db.session.commit()
                flash(f'{form.f_name.data} {form.m_name.data} {form.l_name.data} added!', 'success')
            except:
                flash('Customer creation failure!', 'danger')
        else:
            flash('Customer creation failure! Please check fields!', 'danger')
    return render_template('customer.html', title='New Customer', form=form)


@app.route('/job/new', methods=['GET', 'POST'])
def new_job():
    form = JobForm()
    if request.method == 'POST':
        customer = Customer.query.filter_by(public_id=form.customer_id.data).first()
        job = Job(
            public_id=int(uuid.uuid4().time_low),
            customer_id=customer.id,
            contract_type=form.contract_type.data,
            address=form.address.data,
            city=format_city(form.city.data),
            zip_code=int(form.zip_code.data),
            state=format_string(form.state.data),
            work_address=form.work_address.data,
            work_city=format_string(form.work_city.data),
            work_state=format_string(form.work_state.data)
        )
        if form.validate_on_submit():
            print('success!')
            flash(f'Success!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(f'error!', 'danger')
    return render_template('job.html', title='New Job', form=form)


@app.route('/customer-search')
def customer_search():
    text_string = request.args.get('text').replace(' ', '').lower()
    customers = []
    if text_string:
        customers = search_customers(text_string)

    return jsonify(customers)
