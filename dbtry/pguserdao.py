from pgdaofact import *
from userdao import *
from userr import *
class pguserdao(userdao):

    def insertuser(self,user:userr):
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
            newuser = userr(firstName,lastName,mail,WhatsAppNumber,Password)
            db.session.add(newuser)
            db.session.commit()
            print("added")
        except:
            print("An exception occurred")


    def getuser(userr):
        pass

    def logintuser(userr):
        pass
