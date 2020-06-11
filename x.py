import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/data')
def send_data():
    con = psycopg2.connect("host='localhost' dbname='BC_database' user='postgres' password='KRISS34GUN'")  
    cur = con.cursor()
    cur.execute("""SELECT * FROM public."BC""")
    data = [col for col in cur]
    cur.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
