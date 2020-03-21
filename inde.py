import sys
sys.path.insert(1, 'D:/aastproject/Maimoji/dbtry')

from pgdaofact import *

app = Flask(__name__)

aaa = pgdaofact.getuserdao()

# fn = input("firstName ")
# ln = input("lastName ")
# mail = input("mail ")
number = input("number ")
# Password = input("pass ")
# user1=userr(fn,ln,mail,number,Password)

# res = aaa.insertuser(user1)
res = aaa.getcontact(number)

# choice = "mail"
choice = 'number'
res = aaa.getcontact(number,choice)

print(res)
