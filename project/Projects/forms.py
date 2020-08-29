from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField


class AddProject(FlaskForm):

    
    STATUS_CHOICES = [('in_progress', 'In Progress'), ('completed', 'Completed')]

    clientId = StringField(label="Client Id")

    projectId = StringField(label="Project Id")
    projectName = StringField(label="Project Name")
    projectStartDate = DateField(label='Start Date')
    projectEndDate = DateField(label="End Date")
    projectSponser = StringField(label="Project Sponser")
    userEmpId = StringField(label="User Employee Id")
    projectManager = StringField(label="Project Manager")
    mileStoneName = StringField(label="Mile Stone Name")
    mileStoneStartDate = DateField(label="Mile Stone Start Date")
    mileStoneEndDate = DateField(label="Mile Stone End Date")
    mileStoneComments = StringField(label="Comments")
    mileStoneStatus = SelectField(label="Status", choices=STATUS_CHOICES )

    submit = SubmitField(label='Submit')