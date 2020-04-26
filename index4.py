import sys
import os
basdir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, basdir+'/DAO')

from pgdaofact import *

app = Flask(__name__)

# aaa = pgdaofact.getmsgdao()
aaa  = pgdaofact.getcontactdao()

# fn = input("firstName ")
# ln = input("lastName ")
number = input("enter the user ID ")
# Date = input("text")
# Password = input("pass ")
# user1=userr(fn,ln,mail,number,Password)

# res = aaa.insertuser(user1)
res = aaa.getcontacts(number)

# choice = "mail"
# choice = 'Date'
# res = aaa.getmsg(number)
cont = []
bbb = pgdaofact.getuserdao()
print(len(res))
for i in range(len(res)):
    cont = res[i][0]
    print(cont)



# print(cont)
