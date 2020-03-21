from pgdaofact import *
from contactdao import *
from contact import *

class pgcontactdao(contactdao):


    def addcontact(self,contact:contact,user:userr):
        userID1 = contact.getuserid1()
        userID2 = contact.getuserid2()
        firstName = user.getFN()
        lastName = user.getLN()
        mail = user.getMail()
        WhatsAppNumber = user.getWnum()
        Password = user.getPassword()


        try:
            newcontact= contact(userID1,userID2)
            db.session.add(newcontact)
            db.session.commit()
            print("added")
        except:
            print("An exception occurred")


    # def getcontact(self,usid2):
    #     userid = usid2
    #
    #     try:
    #         getcont = contact.query.filter_by(userID2=usid2).first()
    #         return True,getcont.contactId
    #
    #     except:
    #         return False

         # contact.getuserid2
    def getcontacts(self,userid1,usrid2,choice):
        # usrid = userid1
        # usrr = usrid2

        try:
            if choice == "userID1":
                getcontt = contact.query.filter_by(userID1=userID1).first()
                return True,getcontt.contactID

            else:
                getcontt = contact.query.filter_by(userID2=userID2).first()
                return True,getcontt.contactID

        except:
            return False
