from urllib import request

from flask import Flask, render_template, redirect
import mysql.connector
###### App setup
app = Flask(__name__)

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',user='root',PASSWORD='1234',database='group11')
    cursor =connection.cursor(named_tuple=True)
    cursor.execute(query)#Query operations

    if query_type == 'commit':
        #use for selet add update
        connection.commit()
        return_value =True

    if query_type == 'fetch':
        query_resulte =cursor.fetchall()
        return_value =query_resulte

    connection.close()
    cursor.close()
    return return_value



@app.route('/')
def hello_home():
    return render_template('Home page.html')

@app.route('/About Us')
def AboutUs():
    return render_template('About Us.html')

@app.route('/activity')
def activity():
    return render_template('activity.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/Contact us')
def Contactus():
    return render_template('Contact us.html')

@app.route('/credit_card')
def credit_card():
    return render_template('credit_card.html')

@app.route('/Donators')
def Donators():
    return render_template('Donators.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/Hot activities')
def Hotactivities():
    return render_template('Hot activities.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/Officials')
def Officials():
    return render_template('Officials.html')

@app.route('/Our Volunteers')
def OurVolunteers():
    return render_template('Our Volunteers.html')

@app.route('/Reports')
def Reports():
    return render_template('Reports.html')

@app.route('/timer')
def timer():
    return render_template('timer.html')

@app.route('/To Volunteer')
def ToVolunteer():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastName = request.form['lastName']
        email = request.form['email']
        subject = request.form['subject']
        phone = request.form['phone']
        start = request.form['start']
        gender = request.form['gender']
        question = request.form['question']
        message = request.form['message']
        query = "INSERT INTO users(firstname,lastName ,email,subject,phone,start,gender,question,message) VALUSE('%s','%s','%s','%s','%s','%s','%s','%s','%s') " %(firstname,lastName ,email,subject,phone,start,gender,question,message)
        interact_db(query=query,query_type='commit')

    return render_template('To Volunteer.html',req_method=request.method)

@app.route('/delete_user',methods=['GET','POST'])
def delete_user():
    if request.method =='GET' :
        email =request.args['email']
        query = "DELETE FROM  users WHERE  email ='%s';" % email
        interact_db(query=query,query_type='commit')
        return redirect('/To Volunteer')






@app.route('/allusers')
def allusers():

    query ="select * from users"
    query_result =interact_db(query,query_type='fetch')
    return render_template('To Volunteer.html' ,users=query_result)

if __name__ == '__main__':
    app.run()


