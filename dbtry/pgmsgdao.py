from pgdaofact import *
from msgdao import *
from msg import *
class pgmsgdao(msgdao):

    def sendmsg(self,user:userr,msg:MSG):
        firstName = user.getFN()
        lastName = user.getLN()
        mail = user.getMail()
        WhatsAppNumber = user.getWnum()
        Password = user.getPassword()
        userID1 = msg.getsender()
        userID2 = msg.getreceiver()
        msgContent = msg.getcontent()
        msgDate = msg.getdate()

        app = Flask(__name__)
        basdir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basdir,'maimoji.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        Migrate(app,db)

        try:
            newmsg= MSG(userID1,userID2,msgcontent,msgDate)
            db.session.add(newmsg)
            db.session.commit()
            print("added")
        except:
            print("An exception occurred")

    def getmsg(MSG):
        pass
