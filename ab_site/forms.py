# forms.py - frontend web forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, \
                    SubmitField, IntegerField, FloatField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, NumberRange, \
                               Optional, Regexp, ValidationError
from ab_site.models import Customer


class CustomerForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired()])
    m_name = StringField('Middle Name', validators=[DataRequired()])
    l_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Optional(), Email()])
    phone_0 = StringField('Phone 1', validators=[DataRequired(), Regexp(r'\d?-?\d{3}-?\d{3}-?\d{4}')])
    phone_1 = StringField('Phone 2', validators=[Optional(), Regexp(r'\d?-?\d{3}-?\d{3}-?\d{4}')])
    address = StringField('Address', validators=[Optional()])
    city = StringField('City', validators=[Optional()])
    zip_code = IntegerField('Zip Code', validators=[Optional()])
    state = SelectField('State', choices=[('oh', 'Ohio')])
    submit = SubmitField('Save Customer')

    def validate_f_name(self, f_name):
        customer_query = Customer.query.filter_by(f_name=f_name.data.lower()).filter_by(l_name=self.l_name.data.lower()).filter_by(m_name=self.m_name.data.lower())
        if customer_query.first():
            raise ValidationError('Customer already exists!')


class JobForm(FlaskForm):
    customer_id = IntegerField('Customer ID', validators=[DataRequired()])
    customer_name = StringField('Customer', validators=[DataRequired()])
    customer_search = StringField('Customer Search', validators=[Optional()])
    contract_type = SelectField('Estimate Type', choices=[('roof', 'Roof'), ('siding', 'Siding'), ('paint', 'Painting')])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zip_code = IntegerField('Zip Code', validators=[DataRequired()])
    state = SelectField('State', choices=[('oh', 'Ohio')])
    work_option = BooleanField('Separate work location')
    work_address = StringField('Work Address', validators=[Optional()])
    work_city = StringField('Work City', validators=[Optional()])
    work_state = SelectField('Work State', choices=[('oh', 'Ohio')], validators=[Optional()])
    work_architect = StringField('Work Architect', validators=[Optional()])
    amount = FloatField('Job Amount($)', validators=[DataRequired(), NumberRange(min=0, max=100_000)])
    description = TextAreaField('Job Description', validators=[DataRequired()])
    warranty = FloatField('Job Warranty (years)', validators=[DataRequired(), NumberRange(min=0, max=25)])
    time_type = BooleanField('Specify Start/ Completion')
    duration = FloatField('Job Duration (days)', validators=[Optional(), NumberRange(min=0, max=500)])
    start_date = DateField("Start Date", validators=[Optional()], format='%Y-%m-%d')
    completion_date = DateField("End Date", validators=[Optional()], format='%Y-%m-%d')
    submit = SubmitField('Export Job')

    def validate_completion_date(self, completion_date):
        if completion_date.data < self.start_date.data:
            raise ValidationError("Completion date must not be earlier than start date.")
        
