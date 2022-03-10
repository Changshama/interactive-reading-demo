from flask import Flask, flash, Blueprint, url_for, redirect, session, render_template
import functools
import csv
import ast

def page_config(fname):
  with open(fname) as f:
      page_conf = [{k: v for k, v in row.items()}
          for row in csv.DictReader(f, skipinitialspace=True)]
  f.close()
  return page_conf

# bp_nemo = Blueprint('nemo', __name__, static_folder='static',
#                template_folder='templates')

# with open('page_conf_nemo.csv') as f:
#     page_conf_nemo = [{k: v for k, v in row.items()}
#         for row in csv.DictReader(f, skipinitialspace=True)]
# f.close()

# # extract list from string
# def liststr_2_listarr(dict, val):
#   liststr = [d[val] for d in dict]
#   return [ast.literal_eval(el_str) for el_str in liststr]

# ans_keys_nemo = liststr_2_listarr(page_conf_nemo, 'ans_key')

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




    # return render_template('100_floor/innerbook.html', 
    #                        username =session["username"],
    #                        img_name = page_conf[idx]['img_name'],
    #                        audio_name = page_conf[idx]['audio_name'],
    #                        question_name = page_conf[idx]['question_name'],
    #                        next_page=page_conf[idx]['next_page'],
    #                        ans_path = page_conf[idx]['ans_path'],  
    #                        keys=ans_keys_100[idx]) 



# @bp_nemo.route('/page1')
# @login_required
# def page1():
#     return render_template('nemo/page.html', 
#                            username =session["username"],
#                            img_name = page_conf_nemo[0]['img_name'],
#                            audio_name = page_conf_nemo[0]['audio_name'],
#                            question_name = page_conf_nemo[0]['question_name'],
#                            next_url=page_conf_nemo[0]['next_url'],
#                            ans_path = page_conf_nemo[0]['ans_path'],  
#                            keys=ans_keys_nemo[0])

# @bp_nemo.route('/page2')
# @login_required
# def page2():
#     return render_template('nemo/page.html', 
#                            username =session["username"],
#                            img_name = page_conf_nemo[1]['img_name'],
#                            audio_name = page_conf_nemo[1]['audio_name'],
#                            question_name = page_conf_nemo[1]['question_name'],
#                            next_url=page_conf_nemo[1]['next_url'],
#                            ans_path = page_conf_nemo[1]['ans_path'],  
#                            keys=ans_keys_nemo[1])

# @bp_nemo.route('/page3')
# @login_required
# def page3():
#     return render_template('nemo/page.html', 
#                            username =session["username"],
#                            img_name = page_conf_nemo[2]['img_name'],
#                            audio_name = page_conf_nemo[2]['audio_name'],
#                            question_name = page_conf_nemo[2]['question_name'],
#                            next_url=page_conf_nemo[2]['next_url'],
#                            ans_path = page_conf_nemo[2]['ans_path'],  
#                            keys=ans_keys_nemo[2])
# @bp_nemo.route('/page4')
# @login_required
# def page4():
#     return render_template('nemo/page.html', 
#                            username =session["username"],
#                            img_name = page_conf_nemo[3]['img_name'],
#                            audio_name = page_conf_nemo[3]['audio_name'],
#                            question_name = page_conf_nemo[3]['question_name'],
#                            next_url=page_conf_nemo[3]['next_url'],
#                            ans_path = page_conf_nemo[3]['ans_path'],  
#                            keys=ans_keys_nemo[3])

# @bp_nemo.route('/page5')
# @login_required
# def page5():
#     return render_template('nemo/page.html', 
#                            username =session["username"],
#                            img_name = page_conf_nemo[4]['img_name'],
#                            audio_name = page_conf_nemo[4]['audio_name'],
#                            question_name = page_conf_nemo[4]['question_name'],
#                            next_url=page_conf_nemo[4]['next_url'],
#                            ans_path = page_conf_nemo[4]['ans_path'],  
#                            keys=ans_keys_nemo[4])

