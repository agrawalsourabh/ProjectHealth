from flask import Blueprint, render_template
from project.Project_Mapping.forms import ProjectMapping

project_mapping_bp = Blueprint('project_mapping_bp', __name__)

@project_mapping_bp.route('/', methods=['GET', 'POST'])
def mapping_index():
    form = ProjectMapping()

    if form.validate_on_submit():
        return "Project added"
    
    return render_template('projects_mapping/projectMapping.html', form=form)