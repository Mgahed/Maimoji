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
        try:
            lastID = db.session.query(userr.userID).all()
            userID = lastID[len(tryy)-1][0]+1
        except:
            userID = 1

        # try:
        newuser = userr(userID,firstName,lastName,mail,WhatsAppNumber,Password)
        db.session.add(newuser)
        db.session.commit()
        return True
        # except:
        #     return False

    def getuser(self,usertext,choice):
        try:
            if choice == "mail":
                getauser = userr.query.filter_by(mail=usertext).first()
                # print(userlgin.userID)
                return True,getauser.userID
            else:
                getauser = userr.query.filter_by(WhatsAppNumber=usertext).first()
                # print(userlgin.userID)
                return True,getauser.userID
        except:
            return False

    def logintuser(self,wnum,pas):
        print(wnum)
        print(pas)
        # print("########################################")
        try:
            userlgin = userr.query.filter_by(WhatsAppNumber=wnum).filter_by(Password=pas).first()
        # print(userlgin.userID)
            return True,userlgin.firstName
        except:
            return False,False
