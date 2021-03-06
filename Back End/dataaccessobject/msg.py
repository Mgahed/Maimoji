import os
from flask import *
from flask_sqlalchemy import *
from sqlalchemy import or_
# from flask_migrate import *

basdir = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(1, basdir+'../')
# from app import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://awqyourp:ePCWRA1-5xrGQNBdtNqVZKpQmBE96iaZ@drona.db.elephantsql.com:5432/awqyourp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Migrate(app,db)


class msg(db.Model):
    msgID = db.Column(db.Integer,primary_key=True)
    userID1 = db.Column(db.Integer)
    userID2 = db.Column(db.Integer)
    msgContent = db.Column(db.Text)
    msgDate = db.Column(db.Text)

    def __init__(self, msgID, userID1, userID2, msgContent, msgDate):
        self.msgID=msgID
        self.userID1=userID1
        self.userID2=userID2
        self.msgContent=msgContent
        self.msgDate=msgDate

############################################
    def getsender(self):
        return self.userID1

    def getreceiver(self):
        return self.userID2

    def getmsgcontent(self):
        return self.msgContent

    def getmsgdate(self):
        return self.msgDate
##########################################
    def setsender(self):
        self.userID1 = userID1

    def setreceiver(self):
        self.userID2 = userID2

    def setmsgcontent(self):
        self.msgContent = msgContent

    def setmsgdate(self):
        self.msgDate = msgDate
