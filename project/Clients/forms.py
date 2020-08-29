from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField


class AddClient(FlaskForm):
    clientId = StringField(label="Client Id")
    clientName = StringField(label="Client Name")
    clientStartDate = DateField(label='Start Date')
    clientEndDate = DateField(label="End Date")

    submit = SubmitField(label='Submit')