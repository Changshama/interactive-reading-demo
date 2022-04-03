from flask import Flask, jsonify, views, request, flash, redirect, Response, render_template, Blueprint, current_app, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import csv
import functools
import ast

#login
def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return method(*args, **kwargs)
        else:
            flash("A login is required to see the page!")
            return redirect(url_for('index'))
    return wrapper

def page_config(fname):
  with open(fname) as f:
      page_conf = [{k: v for k, v in row.items()}
          for row in csv.DictReader(f, skipinitialspace=True)]
  f.close()
  return page_conf

def ranking(db, User, uname):
  #questions answered by this user
  this_user = db.session.query(User).filter_by(username = uname).first()
  que_count = len(this_user.que_answered)

  #questions answered by this user's group
  max_question = db.session.query(func.max(User.que_answered)).filter_by(group = this_user.group).scalar()
  
  rank = 1
  if que_count < len(max_question):
    rank = 2
  
  return rank,que_count

def question_conf(db, User, Question, page_conf, uname, bookId, path_dir):
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
        page_conf[page-1]['count_max'] = page_que.count_max

      else:
        page_conf[page-1]['que_audio'] = ''
        page_conf[page-1]['ans_audio'] = ''        
        page_conf[page-1]['ans_keys'] = []
        page_conf[page-1]['que_id'] = 0

    return page_conf

def landing(db, User, Question, img_name, img_format, page_conf, bookid, session, book_title, book_folder, que_name, ans_name):
    uname = session["username"]
    question_conf(db, User, Question, page_conf, uname, bookid, 'https://mltest2823519881.blob.core.windows.net/azureml/audio/'+book_folder+'/')

    return render_template( 'landing.html', 
                            username = uname,
                            question_name = que_name,
                            img_name = img_name,
                            img_format = img_format,
                            next_page = 1,
                            que_id = 0,
                            page_title = book_folder,
                            book_title = book_title,
                            book_folder = book_folder,
                            ans_path = 'static/audio/' + ans_name,
                            keys=['ok','yes','ready','好了','准备'],
                            count_max=0)

def ending(db, User, Question, bookid, session, book_title, book_folder):
    uname = session["username"]
    rank, no_question = ranking(db, User, uname)
    return render_template( 'ending.html', 
                            username = uname,
                            page_title = book_folder,
                            book_title = book_title,
                            rank = rank,
                            questions = no_question)

def process_answer(db, User, session):
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

def innerbook(page, page_conf, img_format, book_title, book_folder, session):
    idx = page - 1    
    return render_template('innerbook.html', 
                        username =session["username"],
                        img_name = page_conf[idx]['img_name'],
                        audio_name = page_conf[idx]['audio_name'],
                        question_name = page_conf[idx]['que_audio'],
                        next_page=page_conf[idx]['next_page'],
                        ans_path = page_conf[idx]['ans_audio'],  
                        keys=page_conf[idx]['ans_keys'],
                        img_format = img_format,
                        page_title = book_folder,
                        book_title = book_title,
                        book_folder = book_folder,
                        count_max=page_conf[idx]['count_max'],
                        que_id = page_conf[idx]['que_id'])
