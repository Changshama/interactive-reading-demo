from flask import Flask, flash, Blueprint, url_for, redirect, session, render_template

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



bp_r = Blueprint('resources', __name__, static_folder='static',
               template_folder='templates')

bp_ic = Blueprint('ic', __name__, static_folder='static',
               template_folder='templates')

bp_pipi = Blueprint('pipi', __name__, static_folder='static',
               template_folder='templates')


@bp_ic.route('/button')
def button():
  return render_template('ic/button.html')
  
@bp_ic.route('/dragon')
def dragon():
  return render_template('ic/dragon.html')

@bp_ic.route('/danny')
def danny():
  return render_template('ic/danny.html')

@bp_ic.route('/pigeon')
def pigeon():
  return render_template('ic/pigeon.html')

@bp_ic.route('/level')
def level():
  return render_template('ic/level.html')

@bp_ic.route('/book')
def book():
  return render_template('ic/book.html')

@bp_pipi.route('/part1')
def part1():
  return render_template('pipi/part1.html')

@bp_pipi.route('/part2')
def part2():
  return render_template('pipi/part2.html')

@bp_r.route('/awards')
def awards():
  return render_template('resources/awards.html')
@bp_r.route('/guide')
def guidance():
  return render_template('resources/guide.html')
@bp_r.route('/authors')
def authors():
  return render_template('resources/authors.html')
@bp_r.route('/illustrators')
def illustrators():
  return render_template('resources/illustrators.html')
