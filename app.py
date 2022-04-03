import os
import functools
import wave
from flask import Flask, jsonify, views, request, flash, redirect, Response, render_template, Blueprint, current_app, session, url_for
from sqlalchemy import Table
from utils import page_config, question_conf, login_required
from utils import landing as land
from utils import process_answer as process
from utils import innerbook as inner
from utils import profile as user_profile
from views import bp_r, bp_ic, bp_pipi
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

bp_green = Blueprint('green', __name__, static_folder='static',
               template_folder='templates')

page_conf_green = page_config('page_conf_worm.csv')

bp_bushop = Blueprint('bushop', __name__, static_folder='static',
               template_folder='templates')

page_conf_bushop = page_config('page_conf_bushop.csv')

bp_sally = Blueprint('sally', __name__, static_folder='static',
               template_folder='templates')
page_conf_sally = page_config('page_conf_worm.csv')

bp_100 = Blueprint('100', __name__, static_folder='static',
               template_folder='templates')

page_conf = page_config('page_conf.csv')

bp_ft = Blueprint('firetruck', __name__, static_folder='static',
               template_folder='templates')

page_conf_firetruck = page_config('page_conf_firetruck.csv')

bp_pigeon = Blueprint('pigeon', __name__, static_folder='static',
               template_folder='templates')

page_conf_pigeon = page_config('page_conf_pigeon.csv')

bp_nemo = Blueprint('nemo', __name__, static_folder='static',
               template_folder='templates')

page_conf_nemo = page_config('page_conf_nemo.csv')

bp_baba = Blueprint('baba', __name__, static_folder='static',
               template_folder='templates')

page_conf_baba = page_config('page_conf_baba.csv')

# @bp_ft.route('/landing')
# @login_required
# def landing():
#   return land(db, User, Question, 'p0.png', 'imgHDetails', page_conf_firetruck, 4, session, '快跑，云梯消防车！', 'firetruck', 'landing-question.wav', "start-reading.wav")

# @bp_ft.route('/process_answer', methods=['POST', 'GET'])
# def process_answer():
#   return process(db, User, session)

# @bp_ft.route('/<int:page>')
# @login_required
# def innerbook(page):
#   return inner(page, page_conf_firetruck, 'imgHDetails', '快跑，云梯消防车！', 'firetruck', session)

# @bp_baba.route('/landing')
# @login_required
# def landing():
#   return land(db, User, Question, 'barbabravo.gif', 'imgHDetails', page_conf_baba, 3, session, '巴巴布拉伯怕海藻', 'baba', 'landing-question.wav', "landing-baba.wav")

# @bp_baba.route('/process_answer', methods=['POST', 'GET'])
# def process_answer():
#   return process(db, User, session)

# @bp_baba.route('/<int:page>')
# @login_required
# def innerbook(page):
#     return inner(page, page_conf_baba, 'imgHDetails', '巴巴布拉伯怕海藻', 'baba', session)

# @bp_100.route('/landing')
# @login_required
# def landing(): 
#   return land(db, User, Question, 'page0.png', 'imgDetails', page_conf, 1, session, '100层的房子', '100', 'landing-question.wav', "start-reading.wav")

# @bp_100.route('/process_answer', methods=['POST', 'GET'])
# def process_answer():
#   return process(db, User, session)

# @bp_100.route('/<int:page>')
# @login_required
# def innerbook(page):
#   return inner(page, page_conf, 'imgDetails', '100层的房子', '100', session)

@bp_pigeon.route('/landing')
@login_required
def landing():
  return land(db, User, Question, 'p0.png', 'imgHDetails', page_conf_pigeon, 5, session, 'The Pigeon Has to Go to School', 'pigeon', 'landing-que-eng.wav', "start-reading-eng.wav")

@bp_pigeon.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  return process(db, User, session)

@bp_pigeon.route('/<int:page>')
@login_required
def innerbook(page):
  return inner(db, User, page, page_conf_pigeon, 'imgLDetails', 'The Pigeon Has to Go to School', 'pigeon', session)

@bp_nemo.route('/landing')
@login_required
def landing():
    return land(db, User, db, User, Question, 'page0.png', 'imgHDetails', page_conf_nemo, 2, session, 'Finding Nemo', 'nemo', 'landing-que-eng.wav', "start-reading-eng.wav")

@bp_nemo.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  return process(db, User, session)

@bp_nemo.route('/<int:page>')
@login_required
def innerbook(page):
  return inner(db, User, page, page_conf_nemo, 'imgHDetails', 'Finding Nemo', 'nemo', session)


@bp_green.route('/landing')
@login_required
def landing(): 
  return land(db, User, Question, 'p0.png', 'imgDetails', page_conf_green, 7, session, 'The Gril With Green Eyes', 'green', 'landing-que-eng.wav', "start-reading-eng.wav")

@bp_green.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  return process(db, User, session)

@bp_green.route('/<int:page>')
@login_required
def innerbook(page):
  return inner(db, User, page, page_conf_green, 'imgSDetails', 'The Gril With Green Eyes', 'green', session)

@bp_sally.route('/landing')
@login_required
def landing(): 
  return land(db, User, Question, 'p0.png', 'imgDetails', page_conf_sally, 6, session, 'Sally\'s Phone', 'sally', 'landing-que-eng.wav', "start-reading-eng.wav")

@bp_sally.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  return process(db, User, session)

@bp_sally.route('/<int:page>')
@login_required
def innerbook(page):
  return inner(db, User, page, page_conf_sally, 'imgSDetails', 'Sally\'s Phone', 'sally', session)

@bp_bushop.route('/landing')
@login_required
def landing(): 
  return land(db, User, Question, 'p0.png', 'imgDetails', page_conf_bushop, 8, session, 'The Magic School Bus Hops Home', 'bushop', 'landing-que-eng.wav', "start-reading-eng.wav")

@bp_bushop.route('/process_answer', methods=['POST', 'GET'])
def process_answer():
  return process(db, User, session)

@bp_bushop.route('/<int:page>')
@login_required
def innerbook(page):
  return inner(db, User, page, page_conf_bushop, 'imgLDetails', 'The Magic School Bus Hops Home', 'bushop', session)


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

app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])
                 
@app.route('/profile', methods=['POST', 'GET'])
def profile():
  return user_profile(db, User, session);
# app.register_blueprint(bp_100, url_prefix='/100_floor')
# app.register_blueprint(bp_baba, url_prefix='/baba')
# app.register_blueprint(bp_ft, url_prefix='/firetruck')
# app.register_blueprint(bp_r, url_prefix='/resources')
# app.register_blueprint(bp_pipi, url_prefix='/pipi')

app.register_blueprint(bp_green, url_prefix='/green')
app.register_blueprint(bp_sally, url_prefix='/sally')
app.register_blueprint(bp_bushop, url_prefix='/bushop')
app.register_blueprint(bp_nemo, url_prefix='/nemo')
app.register_blueprint(bp_pigeon, url_prefix='/pigeon')

app.register_blueprint(bp_ic, url_prefix='/ic')
# with app.app_context():
#     db.create_all()

if __name__ == '__main__': 
    app.run() 
