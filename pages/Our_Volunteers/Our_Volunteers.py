from flask import Blueprint, render_template

# Our_Volunteers blueprint definition
Ourvolunteers = Blueprint('Our_Volunteers', __name__, static_folder='static', static_url_path='/Our_Volunteers', template_folder='templates')


# Routes
@Ourvolunteers.route('/Our_Volunteers')
def index():
    return render_template('Our_Volunteers.html')
