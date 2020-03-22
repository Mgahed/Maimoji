from pgdaofact import *
from msgdao import *
from msg import *
class pgmsgdao(msgdao):

    def sendmsg(self,user:userr,msg:msg):
        userID1 = msg.getsender()
        userID2 = msg.getreceiver()
        msgContent = msg.getcontent()
        msgDate = msg.getdate()

        try:
            newmsg= msg(userID1,userID2,msgcontent,msgDate)
            db.session.add(newmsg)
            db.session.commit()
            return True
        except:
            return False

    def getmsg(self,userID1):
        try:
            getms = msg.query.filter_by(userID1=userID1).with_entities(msg.msgContent,msg.msgDate).all()
            return True,getms

        except:
            return False
