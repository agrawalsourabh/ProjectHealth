from flask import Blueprint, render_template
from project.Users.forms import AddUser

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/adduser', methods=['GET', 'POST'])
def user_add():
    form = AddUser()

    if form.validate_on_submit():
        return "User added"
    
    return render_template('users/addUser.html', form=form)

@user_bp.route('/')
def user_index():

    
    return render_template('users/users.html')