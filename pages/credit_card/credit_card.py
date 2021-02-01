
from flask import Blueprint, render_template, redirect, request, session

# credit_card blueprint definition
from utilities.db.db_manager import DBManager

credit_card = Blueprint('credit_card', __name__, static_folder='static', static_url_path='/credit_card', template_folder='templates')
cost1=0;
id1 =0;
# Routes
@credit_card.route('/credit_card')
def index():
    return render_template('credit_card.html')
#
@credit_card.route('/credit_card/<id>/<int:cost>')
def indexs(id,cost):
    global id1
    global cost1
    id1 =id
    cost1=cost
    return render_template('credit_card.html')

@credit_card.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        donation_type ='dd'
        cost = request.form['cost']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        myname = request.form['myname']
        creditcard = request.form['creditcard']
        expiration_year = '2222'
        expiration_month = '3'
        ccv = request.form['ccv']
        id = request.form['id']
        query2 = "INSERT INTO credit_card(Id,Email,first_Name,last_name,phone_number,amount,donation_type,cerdit_holder_name,card_number,expiration_year,expiration_month,ccv) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " % (id,email,first_name,last_name,phone,cost,donation_type,myname,creditcard,expiration_year,expiration_month,ccv)
        dbManger= DBManager()
        dbManger.commit(query=query2)

        total=cost1-int(cost ,base=10)
        if(total <= 0 ):
         query1 = "UPDATE timers set amount=('%s') WHERE random_Id=(%s)" % (0, id1)
        else:
            query1 = "UPDATE timers set amount=('%s') WHERE random_Id=(%s)" % (total, id1)

        dbManger.commit(query=query1)
        return redirect('/Hot_activities')

