from flask import Blueprint, render_template

# Donators blueprint definition
Donators = Blueprint('Donators', __name__, static_folder='static', static_url_path='/Donators', template_folder='templates')


# Routes
@Donators.route('/Donators')
def index():
    return render_template('Donators.html')
