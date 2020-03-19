import os
from flask import *
from flask_sqlalchemy import *
from flask_migrate import *

db = SQLAlchemy()
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
        return self.userID1 = userID1

    def setreceiver(self):
        return self.userID2 = userID2

    def setmsgcontent(self):
        return self.msgContent = msgContent

    def setmsgdate(self):
        return self.msgDate = msgDate
