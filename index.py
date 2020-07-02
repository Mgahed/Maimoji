import json
import sys
import os
basdir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, basdir+'/DAO')


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

usersignup = pgdaofact.getuserdao()
user1=userr(1,"firstname","lastname","mail35","number351","Password")
res = usersignup.insertuser(user1)
print(res)
db.session.close_all()
# db.session.dispose()
print(db)
