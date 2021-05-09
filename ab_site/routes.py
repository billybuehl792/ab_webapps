# routes.py - routes to app pages

import json
from flask import flash, url_for, redirect, render_template, request, jsonify
from ab_site import app

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
