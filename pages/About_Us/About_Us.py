from flask import Blueprint, render_template

# About_Us blueprint definition
About_Us = Blueprint('About_Us', __name__, static_folder='static', static_url_path='/About_Us', template_folder='templates')


# Routes
@About_Us.route('/About_Us')
def index():
    return render_template('About_Us.html')
