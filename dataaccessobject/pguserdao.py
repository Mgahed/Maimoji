from pgdaofact import *
from userdao import *
from userr import *
from sqlalchemy import or_
class pguserdao(userdao):

    def insertuser(self,user:userr):
        firstName = user.getFN()
        lastName = user.getLN()
        mail = user.getMail()
        WhatsAppNumber = user.getWnum()
        Password = user.getPassword()
        try:
            lastID = db.session.query(userr.userID).all()
            userID = lastID[len(lastID)-1][0]+1
        except:
            userID = 1
        try:
            db.session.remove()
            newuser = userr(userID,firstName,lastName,mail,WhatsAppNumber,Password)
            db.session.add(newuser)
            db.session.commit()
            db.session.remove()
            return True
        except:
            return False

    def getuser(self,usertext):
        try:
            getauser = userr.query.filter(or_(userr.WhatsAppNumber==usertext,userr.mail==usertext)).first()
            # print(userlgin.userID)
            db.session.remove()
            name = getauser.firstName + " " + getauser.lastName
            return True,getauser.userID, name
        except:
            return False

    def getuserbyid(self,idd):
        try:
            getauserbyid = userr.query.filter_by(userID=idd).first()
            # print(userlgin.userID)
            name = getauserbyid.firstName + " " + getauserbyid.lastName
            number = getauserbyid.WhatsAppNumber
            mail = getauserbyid.mail
            db.session.remove()
            return name, number, mail
        except:
            return False

    def logintuser(self,wnum,pas):
        # print(wnum)
        # print(pas)
        # print("########################################")
        try:
            userlgin = userr.query.filter_by(WhatsAppNumber=wnum).filter_by(Password=pas).first()
        # print(userlgin.userID)
            db.session.remove()
            name = userlgin.firstName + " " + userlgin.lastName
            return True,userlgin.userID,name,userlgin.mail
        except:
            return False,False
