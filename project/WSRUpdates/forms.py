from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField


class WSRForm(FlaskForm):


    projectId = StringField(label="Project Id")
    activitiesCompleted = StringField(label="Activities Completed")
    activitiesCompletedStatus = StringField(label="Activities Completed Status")
    activitiesPlanned = StringField(label="Activities Planned")
    activitiesPlannedStatus = StringField(label="Activities Planned Status")
    updatesComments = StringField(label="Comments")
    risks = StringField(label="Risks")
    riskProbabilitySeverity = StringField(label="Risk Severity")
    riskMitigation = StringField(label="Risk Mitigation")
    achievements = StringField(label="Achivements")
    

    submit = SubmitField(label='Submit')