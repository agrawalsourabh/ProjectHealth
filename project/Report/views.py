from flask import Blueprint, render_template

report_bp = Blueprint('report_bp', __name__)

@report_bp.route('/', methods=['GET', 'POST'])
def report_base():
    return render_template('reports/reports.html')