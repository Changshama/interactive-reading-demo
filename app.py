import os
import functools
import wave
from flask import Flask, views, request, flash, redirect, Response, render_template, Blueprint, current_app, session, url_for
from sqlalchemy import Table
from views import bp_nemo,login_required
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.secret_key = "thisisit"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coco.db'
db = SQLAlchemy(app)


class User(db.Model):
    __table__ = Table('user', db.metadata,
                    autoload=True, autoload_with=db.engine)
class Question(db.Model):
    __table__ = Table('question', db.metadata,
                    autoload=True, autoload_with=db.engine)


bp_100 = Blueprint('100_floor', __name__, static_folder='static',
               template_folder='templates')

with open('page_conf.csv') as f:
    page_conf = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
f.close()

@bp_100.route('/landing')
def landing():
    return render_template('100_floor/landing.html', 
                            username =session["username"],
                            question_name = 'landing-question.wav',
                            next_page = 1,
                            ans_path = "static/audio/start-reading.wav",
                            keys=['好了','准备'])

@bp_100.route('/<int:page>')
@login_required
def innerbook(page):
    idx = page -1
    question = db.session.query(Question).filter_by(book_id=1,page_id=page).first()
    que_name = ''
    a_path = ''
    a_keys = []
    if question:
      que_name = question.audio
      a_path = 'static/audio/100/'+question.ans_audio
      a_key = question.ans_keys
      a_keys = a_key.split(';')
    return render_template('100_floor/innerbook.html', 
                        username =session["username"],
                        img_name = page_conf[idx]['img_name'],
                        audio_name = page_conf[idx]['audio_name'],
                        question_name = que_name,
                        next_page=page_conf[idx]['next_page'],
                        ans_path = a_path,  
                        keys=a_keys)

nemo_1_keys = ['Orange', 'Stripe', 'Black', 'White', 'orange', 'white']
nemo_2_keys = ['Forget', 'Remember', 'Memory', 'loss', 'Issue', 'forget', 'remember']

class Main(views.MethodView):
    def get(self):
        return render_template('index.html')
    
    def post(self):
        if 'logout' in request.form:
            session.pop('username', None)
            return redirect(url_for('index'))
        required = ['username', 'passwd']
        for r in required:
            if r not in request.form:
                flash("Error: {0} is required.".format(r))
                return redirect(url_for('index'))
        username = request.form['username']
        passwd = request.form['passwd']
        # check whether user exists in user table
        users = db.session.query(User).filter_by(username=username).first()
        if users and users.pwd == passwd:
            session['username'] = username
        else:
            flash("Username doesn't exist or incorrect password")
        return redirect(url_for('index'))

bp_nemo_1 = Blueprint('nemo_1', __name__, static_folder='static',
               template_folder='templates')
bp_nemo_2 = Blueprint('nemo_2', __name__, static_folder='static',
               template_folder='templates')


@bp_nemo_1.route('/')
def index():
    return render_template('nemo_1/index.html', 
                           ans_path = "static/audio/prompt_answer.wav", 
                           username =session["username"],
                           keys=nemo_1_keys) 

@bp_nemo_2.route('/')
def index():
    return render_template('nemo_2/index.html', 
                           ans_path = "static/audio/prompt-dory-anw.wav", 
                           username =session["username"], 
                           keys=nemo_2_keys)

app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])

app.register_blueprint(bp_nemo_1, url_prefix='/nemo_1')
app.register_blueprint(bp_nemo_2, url_prefix='/nemo_2')
app.register_blueprint(bp_100, url_prefix='/100_floor')
app.register_blueprint(bp_nemo, url_prefix='/nemo')

# with app.app_context():
#     db.create_all()

if __name__ == '__main__': 
    app.run() 
