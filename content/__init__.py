from flask import Flask
from flask_mail import Mail
from pymongo import MongoClient
import os
import ssl


# Instantiate Flask
app = Flask(__name__)


# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = str(os.environ.get('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.environ.get('MAIL_PASSWORD'))
app.config['MAIL_MAX_EMAILS'] = None

mail = Mail(app)

# Config and Instantiate Mongo
user = str(os.environ.get('MONGODB_USERNAME'))
pswd = str(os.environ.get('MONGODB_PASSWORD'))
uri = f"mongodb+srv://{user}:{pswd}@example.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# Instantiate mongodb into app
dB = client.get_database(name='Database_Name')
mongo = dB.get_collection(name='Collection_Name')

from content import routes
from content import admin
