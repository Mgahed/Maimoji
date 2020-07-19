import json
import sys
import os
from sqlalchemy import or_
basdir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, basdir+'/dataaccessobject')


from pgdaofact import *

app = Flask(__name__)

# aaa = pgdaofact.getuserdao()

# fn = input("firstName ")
# ln = input("lastName ")
# mail = input("mail ")
# number = input("number ")
# Password = input("pass ")
# user1=userr(fn,ln,mail,number,Password)

# res = aaa.insertuser(user1)
# res = aaa.logintuser(number,Password)
# tryy=db.session.query(userr.userID).all()
# print(tryy[len(tryy)-1][0])
# print(tryy[0]+5)

# choice = "mail"
# choice = 'number'
# res = aaa.getuser(number,choice)
# res = aaa.getuserbyid(1)
# print(res)


#############msg####################
# bbb = pgdaofact.getmsgdao()
# msg1=msg(1,1,2,"try","2020")
# resmsg = bbb.sendmsg(msg1)
# print(resmsg)
####
# bbb = pgdaofact.getmsgdao()
# resmsg = bbb.getmsg(1,2)
# print(resmsg)
# somedict = {
#                 "msg"  : [ x for x in resmsg[0] ],
#                 "date"  : [ x for x in resmsg[1] ],
#                 "sender"  : [ x for x in resmsg[2] ],
#                 "recivers" : [ x for x in resmsg[3] ]
#            }
# print(somedict)
# x = len(resmsg[0])
# print(x)
# for value in resmsg:
#     print(value)

# usersignup = pgdaofact.getuserdao()
# user1=userr(1,"firstname","lastname","mail35","number351","Password")
# res = usersignup.insertuser(user1)
# print(res)
bbb = pgdaofact.getuserdao()
userreturned = bbb.getuser("07775000")
print(userreturned)
# db.session.close_all()
# # db.session.dispose()
# print(db)
# aaa  = pgdaofact.getcontactdao()
# bbb = pgdaofact.getcontactdao()
# res = aaa.getcontacts(1)
# print(res)
# contact = []
# for i in range(len(res)):
#     cont = res[i]
# cont = input("Enter name or number")
# cont=contact(1,2,3)
# userreturned = bbb.addcontact(cont)
    # contact.append(userreturned[0])
# print(userreturned)
