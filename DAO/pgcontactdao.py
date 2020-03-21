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


    def getcontact(contact):
        pass

         # contact.getuserid2
    def getcontacts(contact):
        pass
