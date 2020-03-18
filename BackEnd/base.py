import os
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import *

# p=rint(basdir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

########################
###db section###########
########################
basdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basdir,'maimoji.db')
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


@app.route('/home')
def add_pupp():
    active = 'home'
    return render_template('home.html',active=active)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)
