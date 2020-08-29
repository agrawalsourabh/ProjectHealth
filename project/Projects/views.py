from flask import Blueprint, render_template
from project.Projects.forms import AddProject

project_bp = Blueprint('project_bp', __name__)

@project_bp.route('/addproject', methods=['GET', 'POST'])
def project_add():
    form = AddProject()

    if form.validate_on_submit():
        return "Project added"
    
    return render_template('projects/addProject.html', form=form)

@project_bp.route('/')
def project_home():
    
    return render_template('projects/projects.html')