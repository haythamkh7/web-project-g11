
from flask import  redirect, render_template, request, Blueprint, session

from utilities.db.db_manager import DBManager



Contactus = Blueprint('Contact_us', __name__, static_folder='static', static_url_path='/Contact_us', template_folder='templates')
@Contactus.route('/Contact_us')
def index():
    return render_template('Contact_us.html')

@Contactus.route('/inserts', methods=['GET','POST'])
def inserts():
    global newemail
    if request.method == 'POST':
     if request.form.get("insert")!= None:
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      email = request.form['email']
      subject = request.form['subject']
      phone = request.form['phone']
      query = "INSERT INTO connact_us(Email,first_Name,last_name ,phone_number,Text_message) values ('%s','%s','%s','%s','%s') " % (email,first_name,last_name ,phone,subject)
      db_manager = DBManager()
      db_manager.commit(query=query)
      session['email'] = email
      return redirect('/Contact_us')

     else:
      newemail=session['email']
      first_Name = request.form['first_name']
      last_name = request.form['last_name']
      Text_message = request.form['subject']
      phone_number = request.form['phone']
      if(first_Name != ""):
       query4 = "UPDATE connact_us set first_Name=('%s') WHERE Email=('%s')" % (first_Name, newemail)
      if(last_name != ""):
       query1 = "UPDATE connact_us set last_name=('%s') WHERE Email=('%s')" % (last_name, newemail)
      if (Text_message != ""):
       query2 = "UPDATE connact_us set Text_message=('%s') WHERE Email=('%s')" % (Text_message, newemail)
      if (phone_number != ""):
       query3 = "UPDATE connact_us set phone_number=('%s') WHERE Email=('%s')" % (phone_number, newemail)
      db_manager = DBManager()
      db_manager.commit(query=query4)
      db_manager.commit(query=query1)
      db_manager.commit(query=query2)
      db_manager.commit(query=query3)
      return redirect('Contact_us')

