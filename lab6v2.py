from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app
import sqlite3
from os import path
import psycopg2
from psycopg2.extras import RealDictCursor
lab6v2 = Blueprint('lab6v2', __name__)


def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'dima_gavrilov_knowledge_base',
            user = 'dima_gavrilov_knowledge_base',
            password = '123'
            )

        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn,cur):
    conn.commit()
    cur.close()
    conn.close()



@lab6v2.route('/lab6v2/')
def main():
    return render_template('lab6v2/lab6v2.html')


@lab6v2.route('/lab6v2/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    if data['method'] == 'info':
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM offices")
        else: 
            cur.execute(f"SELECT * FROM offices")
        offices = cur.fetchall()
        db_close(conn,cur)
        print(offices)
        return {
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        }