from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app
import sqlite3
import json
from os import path
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
lab7 = Blueprint('lab7', __name__)

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



@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM films")
        films = cur.fetchall()
    else: 
        cur.execute(f"SELECT * FROM films")
        films = [dict(row) for row in cur.fetchall()]
    db_close(conn,cur)
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM films WHERE id=%s", (id, ))
        films = cur.fetchone()
    else: 
        cur.execute("SELECT * FROM films WHERE id=?", (id, ))
        films = [dict(row) for row in cur.fetchone()]
    db_close(conn,cur)
    if films is None:
        return "Фильм не найден", 404
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_films(id):
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM films WHERE id=%s", (id,))
    else: 
        cur.execute("DELETE FROM films WHERE id=?", (id,))
    db_close(conn,cur)
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_films(id):
    film = request.get_json()
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM films WHERE id=%s", (id, ))
        films = cur.fetchone()
    else: 
        cur.execute("SELECT * FROM films WHERE id=?", (id, ))
        films = [dict(row) for row in cur.fetchone()]
    db_close(conn,cur)
    if films is None:
        return "Фильм не найден", 404
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    if film['title_ru'] == '':
        return {'title_ru': 'Заполните поле'}, 400
    if film['year'] == '':
        return {'year': 'Заполните дату!'}, 400
    if len(film['description']) > 2000:
        l = len(film['description'])
        return {'description': f'Описание не должно привышать 2000 символов! Символов сейчас: {l}'}, 400
    if int(film['year']) < 1895 or int(film['year']) > datetime.now().year:
        return {'year': f'Вы вышли за пределы(1895 по {datetime.now().year})'}, 400
    if film['title'] == '':
        film['title'] = film['title_ru']
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("UPDATE films set title=%s, title_ru=%s, year=%s, description=%s WHERE id=%s", (film['title'], film['title_ru'], film['year'], film['description'], id))
    else: 
        cur.execute("UPDATE films set title=?, title_ru=?, year=?, description=? WHERE id=?", (film['title'], film['title_ru'], film['year'], film['description'], id))
    db_close(conn,cur)
    return ''


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_films():
    film = request.get_json()
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    if len(film['description']) > 2000:
        l = len(film['description'])
        return {'description': f'Описание не должно привышать 2000 символов! Символов сейчас: {l}'}, 400
    if film['title_ru'] == '':
        return {'title_ru': 'Заполните поле'}, 400
    if film['year'] == '':
        return {'year': 'Заполните дату!'}, 400
    if int(film['year']) < 1895 or int(film['year']) > datetime.now().year:
        return {'year': f'Вы вышли за пределы (1895 по {datetime.now().year})'}, 400





    if film['title'] == '':
        film['title'] = film['title_ru']
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO films (title, title_ru, year, description) VALUES (%s, %s, %s, %s)", (film['title'], film['title_ru'], film['year'], film['description']))
    else: 
        cur.execute("INSERT INTO films (title, title_ru, year, description) VALUES (?, ?, ?, ?)", (film['title'], film['title_ru'], film['year'], film['description']))
    db_close(conn,cur)
    return ""
