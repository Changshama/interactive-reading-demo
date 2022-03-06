import os
import functools
import wave
from flask import Flask, views, request, flash, redirect, Response, render_template, Blueprint, current_app, session, url_for
import floor

app = Flask(__name__)
app.secret_key = "thisisit"

users = {'Jimmy':'lovecoco','Peter':'lovecocotoo'}
bp = floor.bp_100
bp_nemo = floor.bp_nemo

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
        if username in users and users[username] == passwd:
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
app.register_blueprint(bp, url_prefix='/100_floor')
app.register_blueprint(bp_nemo, url_prefix='/nemo')
if __name__ == '__main__': 
    app.run() 
