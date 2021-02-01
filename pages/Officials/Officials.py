from flask import Blueprint, render_template

# Officials blueprint definition
Officials = Blueprint('Officials', __name__, static_folder='static', static_url_path='/Officials', template_folder='templates')


# Routes
@Officials.route('/Officials')
def index():
    return render_template('Officials.html')
