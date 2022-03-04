from flask import Flask, Blueprint, flash, url_for, redirect, session, render_template
import functools
import csv

bp_100 = Blueprint('100_floor', __name__, static_folder='static',
               template_folder='templates')

with open('page_conf.csv') as f:
    page_conf = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return method(*args, **kwargs)
        else:
            flash("A login is required to see the page!")
            return redirect(url_for('index'))
    return wrapper

@bp_100.route('/landing')
def landing():
    return render_template('100_floor/landing.html', 
                            username =session["username"],
                            question_name = 'landing-question.wav',
                            next_url =page_conf[24]['next_url'],
                            ans_path = "static/audio/start-reading.wav",
                            keys=page_conf[0]['ans_path'])

@bp_100.route('/page1')
@login_required
def page1():
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[0]['img_name'],
                           audio_name = page_conf[0]['audio_name'],
                           question_name = page_conf[0]['question_name'],
                           next_url=page_conf[0]['next_url'],
                           ans_path = page_conf[0]['ans_path'],  
                           keys=page_conf[0]['ans_path'])

@bp_100.route('/page2')
@login_required
def page2():
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[1]['img_name'],
                           audio_name = page_conf[1]['audio_name'],
                           question_name = page_conf[1]['question_name'],
                           next_url=page_conf[1]['next_url'],
                           ans_path = page_conf[1]['ans_path'],  
                           keys=page_conf[1]['ans_path'])

@bp_100.route('/page3')
@login_required
def page3():
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[2]['img_name'],
                           audio_name = page_conf[2]['audio_name'],
                           question_name = page_conf[2]['question_name'],
                           next_url=page_conf[2]['next_url'],
                           ans_path = page_conf[2]['ans_path'],  
                           keys=page_conf[2]['ans_path'])
@bp_100.route('/page4')
@login_required
def page4():
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[3]['img_name'],
                           audio_name = page_conf[3]['audio_name'],
                           question_name = page_conf[3]['question_name'],
                           next_url=page_conf[3]['next_url'],
                           ans_path = page_conf[3]['ans_path'],  
                           keys=page_conf[3]['ans_path'])

@bp_100.route('/page5')
@login_required
def page5():
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[4]['img_name'],
                           audio_name = page_conf[4]['audio_name'],
                           question_name = page_conf[4]['question_name'],
                           next_url=page_conf[4]['next_url'],
                           ans_path = page_conf[4]['ans_path'],  
                           keys=page_conf[4]['ans_path'])

@bp_100.route('/page6')
@login_required
def page6():
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[5]['img_name'],
                           audio_name = page_conf[5]['audio_name'],
                           question_name = page_conf[5]['question_name'],
                           next_url=page_conf[5]['next_url'],
                           ans_path = page_conf[5]['ans_path'],  
                           keys=page_conf[5]['ans_path'])

@bp_100.route('/page7')
@login_required
def page7():
    i = 6
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])
                      

@bp_100.route('/page8')
@login_required
def page8():
    i = 7
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path']) 
@bp_100.route('/page9')
@login_required
def page9():
    i = 8
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])
                      

@bp_100.route('/page10')
@login_required
def page10():
    i = 9
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])                            


@bp_100.route('/page11')
@login_required
def page11():
    i = 10
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page12')
@login_required
def page12():
    i = 11
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page13')
@login_required
def page13():
    i = 12
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])
@bp_100.route('/page14')
@login_required
def page14():
    i = 13
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page15')
@login_required
def page15():
    i = 14
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page16')
@login_required
def page16():
    i = 15
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page17')
@login_required
def page17():
    i = 16
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])
                      

@bp_100.route('/page18')
@login_required
def page18():
    i = 17
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path']) 
@bp_100.route('/page19')
@login_required
def page19():
    i = 18
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])
@bp_100.route('/page20')
@login_required
def page20():
    i = 19
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])   

@bp_100.route('/page21')
@login_required
def page21():
    i = 20
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page22')
@login_required
def page22():
    i = 21
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page23')
@login_required
def page23():
    i = 22
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])
@bp_100.route('/page24')
@login_required
def page24():
    i = 23
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])

@bp_100.route('/page25')
@login_required
def page25():
    i = 24
    return render_template('100_floor/page5.html', 
                           username =session["username"],
                           img_name = page_conf[i]['img_name'],
                           audio_name = page_conf[i]['audio_name'],
                           question_name = page_conf[i]['question_name'],
                           next_url=page_conf[i]['next_url'],
                           ans_path = page_conf[i]['ans_path'],  
                           keys=page_conf[i]['ans_path'])                                            