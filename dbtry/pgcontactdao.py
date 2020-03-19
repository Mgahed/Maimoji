from pgdaofact import *
from contactdao import *
from contact import *
class pgcontactdao(contactdao):


    def addcontact(self,contact:contact,User:userr):
        userID1 = contact.getuserid1()
        userID2 = contact.getuserid2()
        firstName = user.getFN()
        lastName = user.getLN()
        mail = user.getMail()
        WhatsAppNumber = user.getWnum()
        Password = user.getPassword()



        app = Flask(__name__)
        basdir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basdir,'maimoji.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        Migrate(app,db)

        try:
            newcontact= contact(userID1,userID2)
            db.session.add(newcontact)
            db.session.commit()
            print("added")
        except:
            print("An exception occurred")


    def getcontact(contact):
        pass

    def getcontacts(contact):
        pass
