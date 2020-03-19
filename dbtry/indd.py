from pgdaofact import *

app = Flask(__name__)

aaa = pgdaofact.getuserdao()

fn = input("firstName ")
ln = input("lastName ")
mail = input("mail ")
number = input("number ")
Password = input("pass ")

userrr = userr(fn,ln,mail,number,Password)

res = aaa.insertuser(userrr)

print(res)
