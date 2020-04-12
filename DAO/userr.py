import os
from flask import *
from flask_sqlalchemy import *
from flask_migrate import *

basdir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, basdir+'../')
from app import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://awqyourp:Y_E64FBbz-0cmsRjHGLqWPOUZQWwqnFJ@drona.db.elephantsql.com:5432/awqyourp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

class userr(db.Model):

    userID = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    mail = db.Column(db.Text)
    WhatsAppNumber = db.Column(db.Integer)
    Password = db.Column(db.Text)

    def __init__(self, userID, firstName, lastName, mail, WhatsAppNumber, Password):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.WhatsAppNumber = WhatsAppNumber
        self.Password = Password

    def getuserID(self):
        return self.userID

    def getFN(self):
        return self.firstName

    def getLN(self):
        return self.lastName

    def getMail(self):
        return self.mail

    def getWnum(self):
        return self.WhatsAppNumber

    def getPassword(self):
        return self.Password

#setters

    def setFN(self):
        self.firstName = firstName

    def setLN(self):
        self.lastName = lastName

    def setMail(self):
        self.mail = mail

    def setWnum(self):
        self.WhatsAppNumber = WhatsAppNumber

    def setPassword(self):
        self.Password = Password
