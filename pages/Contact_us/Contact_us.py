
from flask import Flask, redirect, url_for, render_template, request, Blueprint, session

from utilities.db.db_manager import DBManager



# Contact_us blueprint definition
Contactus = Blueprint('Contact_us', __name__, static_folder='static', static_url_path='/Contact_us', template_folder='templates')

newemail=''
# Routes
@Contactus.route('/Contact_us')
def index():
    return render_template('Contact_us.html')

@Contactus.route('/inserts', methods=['GET','POST'])
def inserts():
    global newemail
    if request.method == 'POST':
     if request.args.get("insert")!= None:
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      email = request.form['email']
      subject = request.form['subject']
      phone = request.form['phone']
      query = "INSERT INTO connact_us(Email,first_Name,last_name ,phone_number,Text_message) values ('%s','%s','%s','%s','%s') " % (email,first_name,last_name ,phone,subject)
      db_manager = DBManager()
      newemail = email
      print(email)
      db_manager.commit(query=query)
      return redirect('/Contact_us')
     else:
      # this_email= email1
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      subject = request.form['subject']
      phone = request.form['phone']
      query = "UPDATE connact_us set first_Name=('%s') WHERE Email=(%s)" % (first_name, newemail)
      query1 = "UPDATE connact_us set list_name=('%s') WHERE Email=(%s)" % (last_name, newemail)
      query2 = "UPDATE connact_us set subject=('%s') WHERE Email=(%s)" % (subject, newemail)
      query3 = "UPDATE connact_us set phone=('%s') WHERE Email=(%s)" % (phone, newemail)
      db_manager = DBManager()
      db_manager.commit(query=query)
      db_manager.commit(query=query1)
      db_manager.commit(query=query2)
      db_manager.commit(query=query3)
      return redirect('Contact_us')

