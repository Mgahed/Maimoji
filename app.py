import sys
import os
from flask_login import logout_user
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import *
from flask_restful import Resource,Api,reqparse
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://awqyourp:Y_E64FBbz-0cmsRjHGLqWPOUZQWwqnFJ@drona.db.elephantsql.com:5432/awqyourp'
#'sqlite:///'+os.path.join(basdir,'DAO/maimoji.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
Migrate(app,db)
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
    def get(self):
        return TODOS

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task')
        args = parser.parse_args()
        TODOS = {'task': args['task']}
        return TODOS, 201
api.add_resource(test, '/test')

@app.route('/')
def index():
    return render_template('index.html')

##################signUp########################
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == "POST":
        fn = request.form['FN']
        ln = request.form['LN']
        mail = request.form['mail']
        number = request.form['snum']
        Password = request.form['spass']
        usersignup = pgdaofact.getuserdao()
        user1=userr(1,fn,ln,mail,number,Password)
        res = usersignup.insertuser(user1)
        if res == True:
            return "Signup success"
        else:
            return "Not Signedup, some info already used"
    else:
        return redirect('/')


##################login########################
@app.route('/login',methods=['GET','POST'])
def NormalLogin():
    if request.method == "POST":
        number = request.form['lnum']
        Password = request.form['lpass']
        userlogin = pgdaofact.getuserdao()
        res = userlogin.logintuser(number,Password)
        # print(res)
        if res[0] == True:
            session['userlogedin'] = res[1]
            return redirect('/home')
        else:
            return "Not logged in"
    else:
        return redirect('/')

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
@app.route('/contacts')
def Contacts():
    aaa  = pgdaofact.getcontactdao()
    bbb = pgdaofact.getuserdao()
    res = aaa.getcontacts(1)
    # print(len(res[1]))
    contact = []
    for i in range(len(res)):
        cont = res[i][0]
        userreturned = bbb.getuserbyid(cont)
        contact.append(userreturned[0])
    # return contact
    if(contact[i] != False):
        try:
            return render_template('contacts.html',contact=contact)
        except:
            return "<center><h1>Error</h1></center>"
    else:
        return "<center><h1>Error</h1></center>"

##################Messsage###################

@app.route('/message',methods=['GET','POST'])
def message():

    sent = ''
    if request.method == "POST":
        text = request.form['txt']
        sent = ftblob(text)
        if sent == '0.5':
            sent = "Nutral"
        elif sent[0] == 0:
            sent = 'Negative'
        else:
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


##############404 not found####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
