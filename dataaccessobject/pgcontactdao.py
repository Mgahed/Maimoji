from dataaccessobject.pgdaofact import *
from dataaccessobject.contactdao import *
from dataaccessobject.contact import *

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


    # def getcontact(self,userID1):
    #     userid = usid2
    #
    #     try:
    #         getcont = contact.query.filter_by(userID2=usid2).first()
    #         return True,getcont.userID2
    #
    #     except:
    #         return False

         # contact.getuserid2

    def getcontacts(self,userID1):

        contacts = []
        try:
            getcontt = contact.query.filter_by(userID1=userID1).all()
            db.session.remove()
            for value in getcontt:
                contacts.append(value.userID2)
            return contacts

        except:
            return False
