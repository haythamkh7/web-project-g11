from flask import request

from flask import Blueprint, render_template, redirect, session

# To_Volunteer blueprint definition
from utilities.db.db_manager import DBManager

ToVolunteer = Blueprint('To_Volunteer', __name__, static_folder='static', static_url_path='/To_Volunteer', template_folder='templates')


# Routes
@ToVolunteer.route('/To_Volunteer')
def index():
    return render_template('To_Volunteer.html')

@ToVolunteer.route('/get', methods=['GET','POST'])
def get():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        start = request.form['start']
        question = "**"
        gender = "f"
        comment = request.form['subject']
        query = "INSERT INTO to_volunteer(Email,first_Name,last_name ,phone_number,Dob,Gender,past_experience,Text_message) values ('%s','%s','%s','%s','%s','%s','%s','%s') " % (email,first_name,last_name ,phone,start,gender,question,comment)
        db_manager = DBManager()
        db_manager.commit(query=query)
        session['username'] = email
        return redirect('/To_Volunteer')
    return 'Somthing went Wrong'

