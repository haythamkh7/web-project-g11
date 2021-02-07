from flask import Blueprint, render_template, session

# timer blueprint definition
timer = Blueprint('timer', __name__, static_folder='static', static_url_path='/timer', template_folder='templates')


# Routes
@timer.route('/timer/<untildate>')
def index(untildate):
    session['untildate'] = untildate
    return render_template('timer.html',untildate=untildate)
