from pgdaofact import *
from contactdao import *
from contact import *

class pgcontactdao(contactdao):


    def addcontact(self,cont:contact):
        userID1 = cont.getuserid1()
        userID2 = cont.getuserid2()
        try:
            lastID = db.session.query(contact.contactID).all()
            contactID = lastID[len(lastID)-1][0]+1
        except:
            contactID = 1
        # try:
        db.session.remove()
        newcontact= contact(contactID,userID1,userID2)
        db.session.add(newcontact)
        db.session.commit()
        db.session.remove()
        return("added")
        # except:
            # print("An exception occurred")


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
