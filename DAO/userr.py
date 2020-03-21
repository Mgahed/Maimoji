import os
from flask import *
from flask_sqlalchemy import *
from flask_migrate import *

app = Flask(__name__)
basdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basdir,'maimoji.db')
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

    def __init__(self, firstName, lastName, mail, WhatsAppNumber, Password):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.WhatsAppNumber = WhatsAppNumber
        self.Password = Password


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
