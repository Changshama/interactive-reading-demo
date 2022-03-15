import os
import functools
import wave
from flask import Flask, jsonify, views, request, flash, redirect, Response, render_template, Blueprint, current_app, session, url_for
from sqlalchemy import Table
from views import login_required,page_config
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

def question_conf(page_conf, uname, bookId, path_dir):
    # filter out questions answered (correctly) by this user
    user = db.session.query(User).filter_by(username = uname).first()
    que_answered = []
    if len(user.que_answered) > 0:
      que_answered = list(map(int, user.que_answered.split(';')))
      print('answered questions include the following:')
      print(que_answered)
      print('------------------------------------------')
    question = db.session.query(Question).filter(~Question.id.in_(que_answered))

    # create question for all pages
    for page in range(1, len(page_conf)+1):
      page_que = question.filter_by(book_id=bookId,level=user.level, page_id=page).first()
      if page_que:
        page_conf[page-1]['que_audio'] = page_que.audio
        page_conf[page-1]['ans_audio'] = path_dir+page_que.ans_audio
        page_conf[page-1]['ans_keys'] = page_que.ans_keys.split(';')
        page_conf[page-1]['que_id'] = page_que.id

      else:
        page_conf[page-1]['que_audio'] = ''
        page_conf[page-1]['ans_audio'] = ''        
        page_conf[page-1]['ans_keys'] = []
        page_conf[page-1]['que_id'] = 0

    return page_conf


bp_100 = Blueprint('100_floor', __name__, static_folder='static',
               template_folder='templates')

page_conf = page_config('page_conf.csv')

bp_ft = Blueprint('firetruck', __name__, static_folder='static',
               template_folder='templates')

page_conf_firetruck = page_config('page_conf_firetruck.csv')

bp_nemo = Blueprint('nemo', __name__, static_folder='static',
               template_folder='templates')

page_conf_nemo = page_config('page_conf_nemo.csv')

bp_baba = Blueprint('baba', __name__, static_folder='static',
               template_folder='templates')

page_conf_baba = page_config('page_conf_baba.csv')

@bp_ft.route('/landing')
@login_required
def landing():
    uname = session["username"]
    question_conf(page_conf_firetruck, uname, 4, 'static/audio/firetruck/')

    return render_template('firetruck/landing.html', 
                            username =session["username"],
                            question_name = 'landing-question.wav',
                            next_page = 1,
                            que_id = 0,
                            ans_path = "static/audio/start-reading.wav",
                            keys=['ok','yes','ready','好了','准备'])

@bp_ft.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  if request.method == "POST":
    ans_data = request.get_json()
    user = db.session.query(User).filter_by(username = session["username"]).first()
    que_answered_before = user.que_answered

    print(ans_data[0]['question'],ans_data[1]['result'])

    # update que answered for the session user
    if ans_data[0]['question'] > 0 and ans_data[1]['result']:
      if que_answered_before:
        user.que_answered += ';'+ str(ans_data[0]['question'])
      else:
        user.que_answered += str(ans_data[0]['question'])
      db.session.commit()
      print('db updated!')
    
    return 'ok'

@bp_ft.route('/<int:page>')
@login_required
def innerbook(page):
    idx = page - 1    
    return render_template('firetruck/innerbook.html', 
                        username =session["username"],
                        img_name = page_conf_firetruck[idx]['img_name'],
                        audio_name = page_conf_firetruck[idx]['audio_name'],
                        question_name = page_conf_firetruck[idx]['que_audio'],
                        next_page=page_conf_firetruck[idx]['next_page'],
                        ans_path = page_conf_firetruck[idx]['ans_audio'],  
                        keys=page_conf_firetruck[idx]['ans_keys'],
                        count_max=page_conf_firetruck[idx]['count_max'],
                        que_id = page_conf_firetruck[idx]['que_id'])


@bp_baba.route('/landing')
@login_required
def landing():
    uname = session["username"]
    question_conf(page_conf_baba, uname, 3, 'static/audio/baba/')

    return render_template('baba/landing.html', 
                            username =session["username"],
                            question_name = 'landing-question.wav',
                            next_page = 1,
                            que_id = 0,
                            ans_path = "static/audio/landing-baba.wav",
                            keys=['ok','yes','ready','好了','准备'])

@bp_baba.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  if request.method == "POST":
    ans_data = request.get_json()
    user = db.session.query(User).filter_by(username = session["username"]).first()
    que_answered_before = user.que_answered

    print(ans_data[0]['question'],ans_data[1]['result'])

    # update que answered for the session user
    if ans_data[0]['question'] > 0 and ans_data[1]['result']:
      if que_answered_before:
        user.que_answered += ';'+ str(ans_data[0]['question'])
      else:
        user.que_answered += str(ans_data[0]['question'])
      db.session.commit()
      print('db updated!')
    
    return 'ok'

@bp_baba.route('/<int:page>')
@login_required
def innerbook(page):
    idx = page - 1    
    return render_template('baba/innerbook.html', 
                        username =session["username"],
                        img_name = page_conf_baba[idx]['img_name'],
                        audio_name = page_conf_baba[idx]['audio_name'],
                        question_name = page_conf_baba[idx]['que_audio'],
                        next_page=page_conf_baba[idx]['next_page'],
                        ans_path = page_conf_baba[idx]['ans_audio'],  
                        keys=page_conf_baba[idx]['ans_keys'],
                        que_id = page_conf_baba[idx]['que_id'])

@bp_nemo.route('/landing')
@login_required
def landing():
    uname = session["username"]
    question_conf(page_conf_nemo, uname, 2, 'static/audio/nemo/')

    return render_template('nemo/landing.html', 
                            username =session["username"],
                            question_name = 'landing-question-nemo.wav',
                            next_page = 1,
                            que_id = 0,
                            ans_path = "static/audio/start-reading-nemo.wav",
                            keys=['ok','yes','ready'])

@bp_nemo.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  if request.method == "POST":
    ans_data = request.get_json()
    user = db.session.query(User).filter_by(username = session["username"]).first()
    que_answered_before = user.que_answered

    print(ans_data[0]['question'],ans_data[1]['result'])

    # update que answered for the session user
    if ans_data[0]['question'] > 0 and ans_data[1]['result']:
      if que_answered_before:
        user.que_answered += ';'+ str(ans_data[0]['question'])
      else:
        user.que_answered += str(ans_data[0]['question'])
      db.session.commit()
      print('db updated!')
    
    return 'ok'

@bp_nemo.route('/<int:page>')
@login_required
def innerbook(page):
    idx = page - 1    
    return render_template('nemo/innerbook.html', 
                        username =session["username"],
                        img_name = page_conf_nemo[idx]['img_name'],
                        audio_name = page_conf_nemo[idx]['audio_name'],
                        question_name = page_conf_nemo[idx]['que_audio'],
                        next_page=page_conf_nemo[idx]['next_page'],
                        ans_path = page_conf_nemo[idx]['ans_audio'],  
                        keys=page_conf_nemo[idx]['ans_keys'],
                        que_id = page_conf_nemo[idx]['que_id'])


@bp_100.route('/landing')
@login_required
def landing():
    uname = session["username"]
    question_conf(page_conf, uname, 1, 'static/audio/100/')

    return render_template('100_floor/landing.html', 
                            username =session["username"],
                            question_name = 'landing-question.wav',
                            next_page = 1,
                            que_id = 0,
                            ans_path = "static/audio/start-reading.wav",
                            keys=['好了','准备'])

@bp_100.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  if request.method == "POST":
    ans_data = request.get_json()
    user = db.session.query(User).filter_by(username = session["username"]).first()
    que_answered_before = user.que_answered

    print(ans_data[0]['question'],ans_data[1]['result'])

    # update que answered for the session user
    if ans_data[0]['question'] > 0 and ans_data[1]['result']:
      if que_answered_before:
        user.que_answered += ';'+ str(ans_data[0]['question'])
      else:
        user.que_answered += str(ans_data[0]['question'])
      db.session.commit()
      print('db updated!')
    
    return 'ok'


@bp_100.route('/<int:page>')
@login_required
def innerbook(page):
    idx = page - 1    
    return render_template('100_floor/innerbook.html', 
                        username =session["username"],
                        img_name = page_conf[idx]['img_name'],
                        audio_name = page_conf[idx]['audio_name'],
                        question_name = page_conf[idx]['que_audio'],
                        next_page=page_conf[idx]['next_page'],
                        ans_path = page_conf[idx]['ans_audio'],  
                        keys=page_conf[idx]['ans_keys'],
                        que_id = page_conf[idx]['que_id'])

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

# #obseleted code starts
# nemo_1_keys = ['Orange', 'Stripe', 'Black', 'White', 'orange', 'white']
# nemo_2_keys = ['Forget', 'Remember', 'Memory', 'loss', 'Issue', 'forget', 'remember']

# bp_nemo_1 = Blueprint('nemo_1', __name__, static_folder='static',
#                template_folder='templates')
# bp_nemo_2 = Blueprint('nemo_2', __name__, static_folder='static',
#                template_folder='templates')


# @bp_nemo_1.route('/')
# def index():
#     return render_template('nemo_1/index.html', 
#                            ans_path = "static/audio/prompt_answer.wav", 
#                            username =session["username"],
#                            keys=nemo_1_keys) 

# @bp_nemo_2.route('/')
# def index():
#     return render_template('nemo_2/index.html', 
#                            ans_path = "static/audio/prompt-dory-anw.wav", 
#                            username =session["username"], 
#                            keys=nemo_2_keys)
## obseleted code ends

app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])

# app.register_blueprint(bp_nemo_1, url_prefix='/nemo_1')
# app.register_blueprint(bp_nemo_2, url_prefix='/nemo_2')
app.register_blueprint(bp_100, url_prefix='/100_floor')
app.register_blueprint(bp_nemo, url_prefix='/nemo')
app.register_blueprint(bp_baba, url_prefix='/baba')
app.register_blueprint(bp_ft, url_prefix='/firetruck')
# with app.app_context():
#     db.create_all()

if __name__ == '__main__': 
    app.run() 
