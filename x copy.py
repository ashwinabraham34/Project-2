import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify
import json
from flask import jsonify
import pandas as pd


from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:KRISS34GUN@localhost:5432/BC_database')
connection = engine.connect()


app = Flask(__name__)

df = pd.read_sql_query('SELECT * FROM public."BC"',con=engine)


@app.route('/', methods=("POST", "GET"))
def html_table():
    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
if __name__ == '__main__':
    app.run(host='0.0.0.0')