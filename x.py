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

df = pd.read_sql_query('SELECT * FROM public."BC"',con=engine)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def html_table():
    return render_template('data.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/data', methods=["GET"])
def send_data():
    json_file = df.to_json(orient='records')
    j_l = json.loads(json_file)
    return jsonify(j_l)

if __name__ == "__main__":
    app.run(debug=True)
