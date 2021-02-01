from flask import Blueprint, render_template

# map blueprint definition
map = Blueprint('map', __name__, static_folder='static', static_url_path='/map', template_folder='templates')


# Routes
@map.route('/map')
def index():
    return render_template('map.html')
