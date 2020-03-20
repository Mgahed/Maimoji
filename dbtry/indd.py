from pgdaofact import *

app = Flask(__name__)

aaa = pgdaofact.getuserdao()

# fn = input("firstName ")
# ln = input("lastName ")
# mail = input("mail ")
number = input("number ")
Password = input("pass ")
# user1=userr(fn,ln,mail,number,Password)

# res = aaa.insertuser(user1)
res = aaa.logintuser(number,Password)


print(res)
