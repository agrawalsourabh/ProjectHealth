from flask import Blueprint, render_template
from project.Clients.forms  import AddClient

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/addclient', methods=['GET', 'POST'])
def client_index():
    form = AddClient()

    if form.validate_on_submit():
        return "Client added"
    
    return render_template('clients/addClient.html', form=form)


@client_bp.route('/')
def client_base():
    return render_template('clients/clients.html')