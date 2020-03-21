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

class MSG(db.Model):
    msgID = db.Column(db.Integer,primary_key=True)
    userID1 = db.Column(db.Integer)
    userID2 = db.Column(db.Integer)
    msgContent = db.Column(db.Text)
    msgDate = db.Column(db.Text)

    def __init__(self, userID1, userID2, msgContent, msgDate):
        self.__userID1=userID1
        self.__userID2=userID2
        self.__msgContent=msgContent
        self.__msgDate=msgDate

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
