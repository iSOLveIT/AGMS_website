from flask import Flask
from flask_mail import Mail
#from flask_pymongo import PyMongo
import urllib
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Instantiate Flask
app = Flask(__name__)


# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
app.config['MAIL_MAX_EMAILS'] = None

mail = Mail(app)

# Config and Instantiate Mongo
#Username = urllib.parse.quote_plus(str(os.getenv('MONGODB_USERNAME')))
#Password = urllib.parse.quote_plus(str(os.getenv('MONGODB_PASSWORD')))

#app.config['MONGO_URI'] = "mongodb+srv://%s:%s@website-dambo.mongodb.net/ADMIN_DB" % (Username, Password)
#app.config['MONGO_DB'] = "ADMIN_DB"

# connect to MongoDB with school_DB
#mongo = PyMongo(app)


from content import routes
from content import admin
