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

    def getmsg(self,userID1,userID2):
        try:
            msglist = []
            datelist = []
            senderlist = []
            reclist = []
            getms = msg.query.filter(or_(msg.userID1==userID1,msg.userID1==userID2)).filter(or_(msg.userID2==userID1,msg.userID2==userID2)).all()
            for value in getms:
                # print(value)
                msglist.append(value.msgContent)
                datelist.append(value.msgDate)
                senderlist.append(value.userID1)
                reclist.append(value.userID2)
            return msglist, datelist, senderlist, reclist

        except:
            return False
