from sqlalchemy.sql.sqltypes import String, Unicode, ARRAY
from typing import List
import csv
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, inspect

#TODO change to postgresql to support array type 
engine = create_engine('sqlite:///coco.db', echo=True)

metadata = MetaData()

# Define the table with sqlalchemy:
que_table = Table('question', metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', Integer),
    Column('page_id', Integer),
    Column('level', Integer),
    Column('audio', String(32)),
    Column('ans_audio', String(32)),
    Column('count_max', Integer),
    Column('ans_keys', Unicode(32)),
)
metadata.create_all(engine)
insert_query = que_table.insert()

with open('question_table.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',') 
    next(csv_reader, None) #skip header
    engine.execute(
        insert_query,
        [{"book_id": row[1], "page_id": row[2], "level": row[3], 
          "audio": row[4], "ans_audio": row[5], "count_max": row[6], "ans_keys": row[7]} 
            for row in csv_reader]
    )

metadata = MetaData()
#TODO change que_answered & book_read to Array type

user_table = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(20)),
    Column('pwd', String(20)),
    Column('age', Integer),
    Column('level', Integer),
    Column('group', Integer),   
    Column('que_answered', String(32)),
    Column('book_read', String(20)),
)
metadata.create_all(engine)
insert_query = user_table.insert()

with open('user_table.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader, None) #skip header
    engine.execute(
        insert_query,
        [{"username": row[1], "pwd": row[2],
          "age": row[3], "level": row[4], "group": row[5], 
          "que_answered": row[6], "book_read": row[7]} 
            for row in csv_reader]
    )


## validate db columns

# insp = inspect(engine)
# print(insp.get_table_names())
# insp.get_columns('user')

## change table schema
# user_table.drop(engine)