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
sys.path.insert(1, basdirr+'/DAO')
from  pgdaofact import *

sys.path.insert(1, basdirr+'/MLUpload')
from sentimentmodel import *


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
    client_secret="7Bb1mp4Y80i1qoXsX9P6zfQf",
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
    return render_template('index.html')

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
            session['userlogedin'] = res[1]
            name = res[2]
            mail = res[3]
            somedict = {
                            "boolean" : "True",
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
@app.route('/GmailLogin')
def GmailLogin():
    if not google.authorized:
        return redirect(url_for("google.login"))
    if google.authorized:
        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok
        userloginn = pgdaofact.getuserdao()
        id = resp.json()["id"]
        pas = "authentt"
        res2 = userloginn.logintuser(id,pas)
        # print(res)
        # print(id)
        # print(pas)
        if res2[0] == True:
            session['userlogedin'] = res2[1]
            return redirect('/home')
        else:
            fn = resp.json()["given_name"]
            ln = resp.json()["family_name"]
            mail = resp.json()["email"]
            id = resp.json()["id"]
            pas = "authentt"
            usersignup = pgdaofact.getuserdao()
            user1=userr(1,fn,ln,mail,id,pas)
            res = usersignup.insertuser(user1)
            if res == True:
                return redirect('/GmailLogin')

            return "<center><h1>Something Wrong</h1></center>"

##############home####################
@app.route('/home')
def home():
    active = 'home'
    return render_template('home.html',active=active)

##################Contacts###################
class contacts(Resource):
    def post(self):
        try:
            sessionid = session['userlogedin']
            aaa  = pgdaofact.getcontactdao()
            bbb = pgdaofact.getuserdao()
            res = aaa.getcontacts(sessionid)
            print(sessionid)
            contact = []
            for i in range(len(res)):
                cont = res[i]
                userreturned = bbb.getuserbyid(cont)
                contact.append(userreturned[0])
            if(contact[i] != False):
                somedict = {
                                "boolean" : "True",
                                "contactid" : res,
                                "contactname" : contact
                           }
        except:
            somedict = {
                            "boolean" : "False"
                       }

        return somedict
api.add_resource(contacts, '/api/contacts')


##################Messsage###################

@app.route('/message',methods=['GET','POST'])
def message():

    sent = ''
    if request.method == "POST":
        text = request.form['txt']
        sent = ftblob(text)
        if sent == 0.5:
            sent = "Nutral"
        elif sent == 0:
            sent = 'Negative'
        elif sent == 1:
            sent = 'Positive'
    return render_template('message.html',sent=sent)

##############send msg####################
@app.route('/sendmessage',methods=['GET','POST'])
def sendmessage():
    getmsgdao = pgdaofact.getmsgdao()
    sender = session['userlogedin']
    msg1=msg(1,sender,2,"try","2020")
    resmsg = getmsgdao.sendmsg(msg1)
    if resmsg:
        return "Done"
    else:
        return "Somethig Wrong"

##############user profile####################
@app.route('/userprofile',methods=['GET','POST'])
def userprofile():
    userid = session['userlogedin']
    bbb = pgdaofact.getuserdao()
    userinfo = bbb.getuserbyid(userid)
    username = userinfo[0]
    usernumber = userinfo[1]
    usermail = userinfo[2]
    return render_template('profileinfo.html',username=username,usernumber=usernumber,usermail=usermail)

################chathistory###########
class chathistory(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sender')
        parser.add_argument('reciver')
        args = parser.parse_args()
        sender = args["sender"]
        reciver = args["reciver"]
        bbb = pgdaofact.getmsgdao()
        resmsg = bbb.getmsg(sender,reciver)
        somedict = {
                        "msg"  : [ x for x in resmsg[0] ],
                        "date"  : [ x for x in resmsg[1] ],
                        "sender"  : [ x for x in resmsg[2] ],
                        "recivers" : [ x for x in resmsg[3] ],
                        "current user" : sender
                   }
        return somedict

api.add_resource(chathistory, '/api/chathistory')


##############404 not found####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
