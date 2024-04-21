from flask import Flask, render_template
# from database import connection
import pymysql
import os

db_charset = os.environ.get('DB_CHARSET')
db_host = os.environ.get('DB_HOST')
db_password = os.environ.get('DB_PASSWORD')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_db = os.environ.get('DB_db')

app = Flask(__name__)

# load data from database
def load_data_from_db():
    timeout = 10
    connection = pymysql.connect(
    charset=db_charset,
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db=db_db,
    host=db_host,
    password=db_password,
    read_timeout=timeout,
    port=int(db_port),
    user=db_user,
    write_timeout=timeout,
)
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM jobs')

        return cursor.fetchall()
    
    finally:
        connection.close()
    return []

@app.route('/')
def hello():
    JOBS = load_data_from_db()
    return render_template('index.html', jobs=JOBS)

if __name__ == '__main__':
    app.run(debug=True)