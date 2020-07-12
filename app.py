from datetime import datetime
import pytz
import smtplib
import sys
import os
from flask_login import logout_user
from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_migrate import *
from flask_restful import Resource,Api,reqparse
from flask_cors import CORS
from flask_dance.contrib.google import make_google_blueprint, google
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

basdirr = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, basdirr+'/dataaccessobject')
from pgdaofact import *

sys.path.insert(1, basdirr+'/MLUpload')
from sentimentmodel import *

# sys.path.insert(1, basdirr+'/facerecognition')
# from facerecognition.Test import *


app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'mykey'

########################
###db section###########
########################
basdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://awqyourp:ePCWRA1-5xrGQNBdtNqVZKpQmBE96iaZ@drona.db.elephantsql.com:5432/awqyourp'
#'sqlite:///'+os.path.join(basdir,'DAO/maimoji.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
Migrate(app,db)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
####################################


blueprint = make_google_blueprint(
    client_id="363930748063-th4rn1gu8o4h5ubbcinhejdbr55vlcrf.apps.googleusercontent.com",
    client_secret="4fmpuVshFiMS6KqUrx94jcax",
    offline=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

####################################
### views functions and routing ###
###################################

class test(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        args = parser.parse_args()
        final = int(args["title"])*2
        somedict = {
                        "number" : final
                   }
        return somedict

    # def get(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('title')
    #     args = parser.parse_args()
    #     return args

api.add_resource(test, '/api/test')

@app.route('/')
def index():
    return "<center><h1>Hello This is Mgahed</h1></center>"
    # if google.authorized:
    #     resp = google.get("/oauth2/v2/userinfo")
    #     assert resp.ok, resp.text
    #     fn = resp.json()["given_name"]
    #     ln = resp.json()["family_name"]
    #     mail = resp.json()["email"]
    #     id = resp.json()["id"]
    #     pas = "authentt"
    #     usersignup = pgdaofact.getuserdao()
    #     user1=userr(1,fn,ln,mail,id,pas)
    #     res = usersignup.insertuser(user1)
    #     if res == True:
    #         return resp.json()
    #     x = "alreadysignedup"
    #     return resp.json()

##################signUp########################
class signup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('FN')
        parser.add_argument('LN')
        parser.add_argument('mail')
        parser.add_argument('snum')
        parser.add_argument('spass')
        args = parser.parse_args()
        firstname = args["FN"]
        lastname = args["LN"]
        mail = args["mail"]
        number = args["snum"]
        Password = args["spass"]
        usersignup = pgdaofact.getuserdao()
        user1=userr(1,firstname,lastname,mail,number,Password)
        res = usersignup.insertuser(user1)
        db.session.close_all()
        if res == True:
            somedict = {
                            "boolean" : "True"
                       }
        else:
            somedict = {
                            "boolean" : "False"
                       }
        return somedict
api.add_resource(signup, '/api/signup')

##################login########################
class login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('number')
        parser.add_argument('pass')
        args = parser.parse_args()
        number = args["number"]
        Password = args["pass"]
        userlogin = pgdaofact.getuserdao()
        res = userlogin.logintuser(number,Password)
        # print(res)
        if res[0] == True:
            id = res[1]
            name = res[2]
            mail = res[3]
            somedict = {
                            "boolean" : "True",
                            "id": id,
                            "name" : name,
                            "mail" : mail,
                            "number" : number

                       }
            return somedict
        else:
            somedict = {
                            "boolean" : "False"

                       }
            return somedict
api.add_resource(login, '/api/login')
#####################Gmail######################
@app.route('/login/google')
def GmailLogin():
    if not google.authorized:
        return  render_template(url_for("google.login"))


##############home####################
@app.route('/home')
def home():
    return "hh"

##################Contacts###################
class contacts(Resource):
    def post(self):
        try:
            loop = 0
            parser = reqparse.RequestParser()
            parser.add_argument('id')
            args = parser.parse_args()
            sessionid = args["id"]
            aaa  = pgdaofact.getcontactdao()
            bbb = pgdaofact.getuserdao()
            res = aaa.getcontacts(sessionid)
            print(sessionid)
            print(res)
            contact = []
            for i in range(len(res)):
                cont = res[i]
                userreturned = bbb.getuserbyid(cont)
                print(contact)
                print(userreturned)
                contact.append(userreturned[0])
                loop = i+1
            if(contact[i] != False):
                somedict = {
                                "boolean" : "True",
                                "contactid" : res,
                                "contactname" : contact,
                                "loop" : loop
                           }
        except:
            somedict = {
                            "boolean" : "False"
                       }

        return somedict
api.add_resource(contacts, '/api/contacts')

##################facerec###################
# @app.route('/facerecognition',methods=['GET','POST'])
# def facerecognition():
#
#         state = facerec()
#         return state


##################Messsage###################

class message(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('msg')
        parser.add_argument('sender')
        parser.add_argument('reciver')
        args = parser.parse_args()
        mesg = args["msg"]
        mesgg = mesg
        sender = args["sender"]
        reciver = args["reciver"]
        tz_NY = pytz.timezone('Africa/Cairo')
        now = datetime.now(tz_NY)
        datime = now.strftime("%d/%m/%Y %H:%M")
        sent = ''
        try:
            sent = ftblob(mesg)
            if sent == 0.5:
                sent = "Nutral"
                mesg = mesg + " \U0001F610"
                mesgg += " :|"
            elif sent == 0:
                sent = 'Negative'
                mesg = mesg + " \U0001F641"
                mesgg += " :("
            elif sent == 1:
                sent = 'Positive'
                mesg = mesg + " \U0001f600"
                mesgg += " :)"
            getmsgdao = pgdaofact.getmsgdao()
            msg1=msg(1,sender,reciver,mesg,datime)
            resmsg = getmsgdao.sendmsg(msg1)
#########################sender w recinfo#################################
            bbb = pgdaofact.getuserdao()
            senderreturn = bbb.getuserbyid(sender)
            sendername = senderreturn[0]

            reciverreturn = bbb.getuserbyid(reciver)
            recivernumber = reciverreturn[1]
            recivermail = reciverreturn[2]
            recivernumber = "+2" + recivernumber
#########################mai w whatsapp#################################
            def send_email(subject, mesag, sendername):
                try:
                    fromm = sendername
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login("maimojiapp@gmail.com", "MaimojiApp.com")
                    message = 'Subject: {}\nFrom: {}\n\n{}'.format(subject,fromm, mesag)
                    server.sendmail("maimojiapp@gmail.com", "abdelrhmanmgahed131@gmail.com ", message)
                    server.quit()
                    print("Success: Email sent!")
                except:
                    print("Email failed to send.")

            subject = "From MaiMoji App"
            mesag = mesgg
            mesag = mesag + "\n\n\n\n\nNote: \nThis mail sent from MaiMoji App\nYou cant reply here use the App"
            send_email(subject, mesag, sendername)
            phone = "+201100479096"
            # phone = recivernumber
            print(phone)
            txt = mesg
            whatsapp = "https://api.whatsapp.com/send?phone={}&text={}".format(phone,txt)
            print(whatsapp)
##########################################################
            somedict = {

                            "boolean" : "True",
                            "message" : mesg,
                            "state" : sent,
                            "whatsapp": whatsapp

                       }
            return somedict
        except:
            somedict = {
                            "boolean" : "False",
                            "message" : mesg,
                            "state" : sent,
                            "sender" : sender,
                            "rec" : reciver

                       }
            return somedict

api.add_resource(message, '/api/message')

##############send msg####################
# @app.route('/sendmessage',methods=['GET','POST'])
# def sendmessage():
#     getmsgdao = pgdaofact.getmsgdao()
#     sender = "1"
#     reciver = "2"
#     msg1=msg(1,sender,reciver,"try","2020")
#     resmsg = getmsgdao.sendmsg(msg1)
#     if resmsg:
#         return "Done"
#     else:
#         return "Somethig Wrong"

##############user profile####################
# @app.route('/userprofile',methods=['GET','POST'])
# def userprofile():
#     userid = session['userlogedin']
#     bbb = pgdaofact.getuserdao()
#     userinfo = bbb.getuserbyid(userid)
#     username = userinfo[0]
#     usernumber = userinfo[1]
#     usermail = userinfo[2]
#     # return render_template('profileinfo.html',username=username,usernumber=usernumber,usermail=usermail)
#     return "userprofile endpoint"
################chathistory###########
class chathistory(Resource):
    def post(self):
        loop = 0
        parser = reqparse.RequestParser()
        parser.add_argument('sender')
        parser.add_argument('reciver')
        args = parser.parse_args()
        sender = args["sender"]
        reciver = args["reciver"]
        try:
            bbb = pgdaofact.getmsgdao()
            resmsg = bbb.getmsg(sender,reciver)
            loop = len(resmsg[0])
            bbb = pgdaofact.getuserdao()
            contact = []
            for i in range(loop):
                userreturned = bbb.getuserbyid(resmsg[2][i])
                contact.append(userreturned[0])
            # print(contact)
            somedict = {
                            "boolean" : "True",
                            "msg"  : [ x for x in resmsg[0] ],
                            "date"  : [ x for x in resmsg[1] ],
                            "sender"  : contact,
                            "recivers" : [ x for x in resmsg[3] ],
                            "currentuser" : sender,
                            "reciever" : reciver,
                            "looping" : loop
                       }
            return somedict
        except:
            somedict = {
                            "boolean" : "False"
                       }
            return somedict

api.add_resource(chathistory, '/api/chathistory')

#################add contact####################
class addcontact(Resource):
    def post(self):
        typo = "This Is Flag"
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('mailornum')
        parser.add_argument('typo')
        args = parser.parse_args()
        sessios = args["id"]
        mailornum = args["mailornum"]
        typo = args["typo"]
        try:
            bbb = pgdaofact.getuserdao()
            userreturned = bbb.getuser(mailornum)
            name = userreturned[2]
            id = userreturned[1]
            if typo != "typo":
                somedict = {
                                "boolean" : "True",
                                "name" : name,
                                "mailornumber" : mailornum

                           }
                return somedict
            elif typo == "typo":
                bbb = pgdaofact.getcontactdao()
                cont=contact(1,sessios,id)
                userreturned = bbb.addcontact(cont)
                somedict = {
                                "boolean" : "True"

                           }
                return somedict
        except:
            somedict = {
                            "boolean" : "False"
                       }
            return somedict

api.add_resource(addcontact, '/api/addcontact')


##############404 not found####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
