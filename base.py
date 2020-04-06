import sys
import os
from flask_login import logout_user
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import *
from flask_dance.contrib.google import make_google_blueprint, google
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

basdirr = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, basdirr+'/DAO')
from  pgdaofact import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

########################
###db section###########
########################
basdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basdir,'DAO/maimoji.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
        user1=userr(fn,ln,mail,number,Password)
        res = usersignup.insertuser(user1)
        if res == True:
            return "Signup success"
        else:
            return "Not Signedup, some info already used"
    else:
        return redirect('/')


##################home after login########################
@app.route('/home',methods=['GET','POST'])
def NormalLogin():
    active = 'home'
    if request.method == "POST":
        number = request.form['lnum']
        Password = request.form['lpass']
        userlogin = pgdaofact.getuserdao()
        res = userlogin.logintuser(number,Password)
        # print(res)
        if res[0] == True:
            session['userlogedin'] = res[1]
            return render_template('home.html',active=active)
        else:
            return "Not logged in"
    else:
        return redirect('/')

#####################Gmail######################
@app.route('/homee')
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
            return render_template('home.html')
        else:
            fn = resp.json()["given_name"]
            ln = resp.json()["family_name"]
            mail = resp.json()["email"]
            id = resp.json()["id"]
            pas = "authentt"
            usersignup = pgdaofact.getuserdao()
            user1=userr(fn,ln,mail,id,pas)
            res = usersignup.insertuser(user1)
            if res == True:
                return redirect('/homee')

            return "<center><h1>Something Wrong</h1></center>"


##############404 not found####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
