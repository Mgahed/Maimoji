from pgdaofact import *
from msgdao import *
from msg import *
class pgmsgdao(msgdao):

    def sendmsg(self,msgg:msg):
        userID1 = msgg.getsender()
        userID2 = msgg.getreceiver()
        msgContent = msgg.getmsgcontent()
        msgDate = msgg.getmsgdate()

        try:
            lastID = db.session.query(msg.msgID).all()
            msgID = lastID[len(lastID)-1][0]+1
        except:
            msgID = 1

        try:
            newmsg= msg(msgID,userID1,userID2,msgContent,msgDate)
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
