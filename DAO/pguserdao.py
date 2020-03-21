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
            newuser = userr(firstName,lastName,mail,WhatsAppNumber,Password)
            db.session.add(newuser)
            db.session.commit()
            return True
        except:
            return False

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
        Whats = wnum
        Password = pas
        # print(Whats)
        # print("########################################")

        try:
            userlgin = userr.query.filter_by(WhatsAppNumber=Whats).filter_by(Password=Password).first()
            # print(userlgin.userID)
            return True,userlgin.userID
            # return True
        except:
            return False
