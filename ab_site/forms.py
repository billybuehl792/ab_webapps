# forms.py - frontend web forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, \
                    SubmitField, IntegerField, DateField, FloatField, \
                    TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange, \
                               Optional, Regexp


class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')


class CustomerForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[('OH', 'Ohio')])
    zip_code = IntegerField('Zip Code', validators=[Optional()])
    email = StringField('Email', validators=[Optional(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp(r'\d?\d{3}-?\d{3}-?\d{4}')])
    submit = SubmitField('Export Customer')


class JobForm(FlaskForm):
    customer_search = StringField('Customer Search', validators=[Optional()])
    contract_type = SelectField('Estimate Type', choices=[('roof', 'Roof'), ('siding', 'Siding'), ('paint', 'Painting')])
    work_option = BooleanField('Separate work location')
    work_address = StringField('Work Address', validators=[Optional()])
    work_city = StringField('Work City', validators=[Optional()])
    work_state = SelectField('Work State', choices=[('OH', 'Ohio')])
    work_architect = StringField('Work Architect', validators=[Optional()])
    amount = FloatField('Job Amount($)', validators=[DataRequired(), NumberRange(min=0, max=100_000)])
    description = TextAreaField('Job Description', validators=[DataRequired()])
    warranty = FloatField('Job Warranty (years)', validators=[DataRequired(), NumberRange(min=0, max=25)])
    time_type = BooleanField('Specify Start/ Completion')
    duration = FloatField('Job Duration (days)', validators=[Optional(), NumberRange(min=0, max=500)])
    start_date = StringField("Start Date", validators=[Optional()])
    completion_date = StringField("End Date", validators=[Optional()])
    submit = SubmitField('Export Job')
