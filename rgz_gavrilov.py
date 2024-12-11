from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app, jsonify
import sqlite3
import json
from os import path
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
rgz_gavrilov = Blueprint('rgz_gavrilov', __name__)

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



@rgz_gavrilov.route('/rgz/')
def main():
    return render_template('rgz_gavrilov/rgz_gavrilov.html')


@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/', methods=['GET'])
def get_films():
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM recipes")
        recipes = cur.fetchall()
    else: 
        cur.execute(f"SELECT * FROM recipes")
        recipes = [dict(row) for row in cur.fetchall()]
    db_close(conn,cur)
    return recipes

