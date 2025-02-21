import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='db'
    )
    cursor = conn.cursor()
    cursor.execute('select * from students')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=results)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000, debug=True)