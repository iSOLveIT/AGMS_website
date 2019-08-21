"""This file configures:
    1- Flask
    2- Flask Mail
    And it also links the routes to the Flask app instance.
NB: The flask app was created as a package hence the app is run from the ``run.py`` file
"""

from flask import Flask
from flask_mail import Mail


app = Flask(__name__)



# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "email_address"
app.config['MAIL_PASSWORD'] = "password"
app.config['MAIL_MAX_EMAILS'] = None

mail = Mail(app)




from content import routes
from content import admin
    