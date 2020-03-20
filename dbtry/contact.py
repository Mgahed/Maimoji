import os
from flask import *
from flask_sqlalchemy import *

app = Flask(__name__)
basdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basdir,'maimoji.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

class contact(db.Model):

    contactID = db.Column(db.Integer,primary_key=True)

    userID1 = db.Column(db.Integer)
    userID2 = db.Column(db.Integer)

    def __init__(self, userID1, userID2):
        self.__userID1=userID1
        self.__userID2=userID2

############################################

    def getuserid1(self):
        return self.userID1

    def getuserid2(self):
        return self.userID2


##########################################

    def setuserid1(self):
        self.userID1 = userID1

    def setuserid2(self):
        self.userID2 = userID2
