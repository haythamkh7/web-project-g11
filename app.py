from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

if __name__ == '__main__':
    app.run()

###### Pages
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

from pages.activity.activity import activity
app.register_blueprint(activity)

from pages.credit_card.credit_card import credit_card
app.register_blueprint(credit_card)

from pages.Donators.Donators import Donators
app.register_blueprint(Donators)

from pages.gallery.gallery import gallery
app.register_blueprint(gallery)

from pages.map.map import map
app.register_blueprint(map)

from pages.Officials.Officials import Officials
app.register_blueprint(Officials)

from pages.Reports.Reports import Reports
app.register_blueprint(Reports)

from pages.Our_Volunteers.Our_Volunteers import Ourvolunteers
app.register_blueprint(Ourvolunteers)

from pages.About_Us.About_Us import About_Us
app.register_blueprint(About_Us)

from pages.Contact_us.Contact_us import Contactus
app.register_blueprint(Contactus)

from pages.Hot_activities.Hot_activities import Hotactivities
app.register_blueprint(Hotactivities)

from pages.To_Volunteer.To_Volunteer import ToVolunteer
app.register_blueprint(ToVolunteer)

from pages.timer.timer import timer
app.register_blueprint(timer)


from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


