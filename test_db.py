import os
import functools
import wave
from flask import Flask, views, request, flash, redirect, Response, render_template, Blueprint, current_app, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "thisisit"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocotest5.db'
db = SQLAlchemy(app)

# testing
class Questiontest(db.Model):
    __table__ = Table('question', db.metadata,
                    autoload=True, autoload_with=db.engine)
class Usertest(db.Model):
    __table__ = Table('user', db.metadata,
                    autoload=True, autoload_with=db.engine)    

question = db.session.query(Questiontest).filter_by(book_id=1,page_id=4).first()
user = db.session.query(Usertest).filter_by(username='Jimmy').first()
#change database records
test_que = Questiontest.query.get_or_404(3)
test_que.level = 5
db.session.commit()
#verify
for item in db.session.query(Questiontest.id, Questiontest.level):
    print(item)

question = db.session.query(Questiontest).filter_by(book_id=1,page_id=4).first()
question.audio = 'question-page4.wav'
db.session.commit()