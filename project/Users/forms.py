from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField


class AddUser(FlaskForm):

    
    ONSITE_CHOICES = [('onsite', 'Onsite'), ('offshore', 'Offshore')]
    VISA_CHOICES = [('b1', 'B1'), ('l1', 'L1'), ('h1', 'H1'), ('no', 'NA')]
    ROLE_CHOICES = [('user', 'User'), ('admin', 'Admin'), ('supervisor', 'Supervisor'), ('manager', 'Manager')]


    userEmpId = StringField(label="User Employee Id")
    userName = StringField(label="User Name")
    userTitle = StringField(label="User Title")
    userCompanyStartDate = DateField(label='Start Date')
    userCompanyEndDate = DateField(label="End Date")
    userSupervisor = StringField(label="User Supervisior")
    userEmailID = StringField(label="User Employee Id")
    userOnsite = SelectField(label="Onsite", choices=ONSITE_CHOICES )
    userLocation = StringField(label="Location")
    userVisaAvailable = SelectField(label="Visa Available", choices=VISA_CHOICES )
    assignSystemRole = SelectField(label="System Role", choices=ROLE_CHOICES )
    

    submit = SubmitField(label='Submit')