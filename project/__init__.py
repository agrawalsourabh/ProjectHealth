import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))		

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app=app, db=db)

from project.Clients.views import client_bp
app.register_blueprint(client_bp, url_prefix='/clients')

from project.Projects.views import project_bp
app.register_blueprint(project_bp, url_prefix='/projects')


from project.Report.views import report_bp
app.register_blueprint(report_bp, url_prefix='/reports')


from project.Users.views import user_bp
app.register_blueprint(user_bp, url_prefix='/users')

from project.Project_Mapping.views import project_mapping_bp
app.register_blueprint(project_mapping_bp, url_prefix='/projectmapping')

from project.WSRUpdates.views import wsr_bp
app.register_blueprint(wsr_bp, url_prefix='/wsr')

