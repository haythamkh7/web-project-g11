from flask import Blueprint, render_template

# Reports blueprint definition
Reports = Blueprint('Reports', __name__, static_folder='static', static_url_path='/Reports', template_folder='templates')


# Routes
@Reports.route('/Reports')
def index():
    return render_template('Reports.html')
