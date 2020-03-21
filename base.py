import sys
import os
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import *

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




####################################
### views functions and routing ###
###################################

@app.route('/')
def index():
    return render_template('index.html')


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

def GmailLogin():
    active = 'home'

    return render_template('home.html')


##############404 not found####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
