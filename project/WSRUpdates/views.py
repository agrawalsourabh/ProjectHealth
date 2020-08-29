from flask import Blueprint, render_template
from project.WSRUpdates.forms import WSRForm

wsr_bp = Blueprint('wsr_bp', __name__)

@wsr_bp.route('/', methods=['GET', 'POST'])
def wsr_index():
    form = WSRForm()

    if form.validate_on_submit():
        return "User added"
    
    return render_template('wsr/wsrform.html', form=form)