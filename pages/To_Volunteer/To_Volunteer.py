
from flask import  redirect, render_template, request, Blueprint, session

from utilities.db.db_manager import DBManager


ToVolunteer = Blueprint('To_Volunteer', __name__, static_folder='static', static_url_path='/To_Volunteer', template_folder='templates')


# Routes
@ToVolunteer.route('/To_Volunteer')
def index():
    return render_template('To_Volunteer.html')

@ToVolunteer.route('/get', methods=['GET','POST'])
def get():
    if request.method == 'POST':
      if request.form.get("Insert") != None:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        start = request.form['start']
        question = request.form['question']
        gender = request.form['gender']
        query = "INSERT INTO to_volunteer(Email,first_Name,last_name ,phone_number,Dob,Gender,past_experience) values ('%s','%s','%s','%s','%s','%s','%s') " % (email , first_name,last_name ,phone,start,gender,question)
        db_manager = DBManager()
        db_manager.commit(query=query)
        session['username'] = email
        return redirect('/To_Volunteer')
    return 'Somthing went Wrong'

@ToVolunteer.route('/Delete', methods=['GET','POST'])
def Delete():
  myemail = session['username']
  if (myemail != ''):
   query1 = "Delete from to_volunteer where Email = '%s'" % (myemail)
   db_manager = DBManager()
   db_manager.commit(query=query1)
  return redirect('/To_Volunteer')