from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.fields.html5 import DateField


class ProjectMapping(FlaskForm):

    STATUS_CHOICES = [('in_progress', 'In Progress'), ('completed', 'Completed')]
    BILLABLE_CHOICES = [('yes', 'Yes'), ('no', 'No')]

    MILSTATUS_CHOICES = [('in_progress', 'In Progress'), ('completed', 'Completed')]

    projectId = StringField(label="Project Id")
    userProjectName = StringField(label="Employee Name")
    userProjectStartDate = DateField(label='Start Date')
    userProjectEndDate = DateField(label="End Date")
    billableYesNo = RadioField(label="Billable", choices=BILLABLE_CHOICES)
    billableStartDate = DateField(label='Billable Start Date')
    billableEndDate = DateField(label="Billable End Date")
    allocationPercentage = StringField(label="Allocation Percentage")
    mileStoneName = StringField(label="Mile Stone Name")
    mileStoneStartDate = DateField(label="Mile Stone Start Date")
    mileStoneEndDate = DateField(label="Mile Stone End Date")
    mileStoneComments = StringField(label="Comments")
    mileStoneStatus = SelectField(label="Status", choices=MILSTATUS_CHOICES )

    submit = SubmitField(label='Submit')