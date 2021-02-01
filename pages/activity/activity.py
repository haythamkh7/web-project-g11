from flask import Blueprint, render_template

# activity blueprint definition
activity = Blueprint('activity', __name__, static_folder='static', static_url_path='/activity', template_folder='templates')


# Routes
@activity.route('/activity')
def index():
    return render_template('activity.html')
