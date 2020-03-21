import os
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import *

class DAOFact:

    def __init__(self):
        app = Flask(__name__)
        basdir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basdir,'maimoji.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        Migrate(app,db)

    def getuserdao():
        pass

    def getmsgdao():
        pass

    def getcontactdao():
        pass
