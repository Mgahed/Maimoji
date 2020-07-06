import os
from flask import *
from flask_sqlalchemy import *
from flask_migrate import *

basdir = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(1, basdir+'../')
# from app import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://awqyourp:ePCWRA1-5xrGQNBdtNqVZKpQmBE96iaZ@drona.db.elephantsql.com:5432/awqyourp'
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
