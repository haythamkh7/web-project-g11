

from flask import Blueprint, render_template

from utilities.db.db_manager import DBManager

Hotactivities = Blueprint('Hot_activities', __name__, static_folder='static', static_url_path='/Hot_activities', template_folder='templates')


@Hotactivities.route('/Hot_activities')
def index():
    query = "select * from timers"
    db_manager = DBManager()
    query_result= db_manager.fetch(query=query)
    return render_template('Hot_activities.html', timers=query_result)
