from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app
import sqlite3
from os import path
lab5 = Blueprint('lab5', __name__)
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash


@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))


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


@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    conn, cur = db_connect()

    login = request.form.get('login')
    password = request.form.get('password')
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT login FROM users WHERE login = %s;", (login,))
    else: 
        cur.execute(f"SELECT login FROM users WHERE login = ?;", (login,))
    if cur.fetchone():
        db_close(conn,cur)
        return render_template('lab5/register.html',
                                error='Такой пользователь уже существует')
    password_hash = generate_password_hash(password)
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"INSERT INTO users (login, password) VALUES (%s, %s);", (login,password_hash))
    else:
        cur.execute(f"INSERT INTO users (login, password) VALUES (?, ?);", (login,password_hash))
    db_close(conn,cur)
    return render_template('lab5/success.html', login=login)


@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')


    conn, cur = db_connect()


    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM users WHERE login=%s;", (login,))
    else:
        cur.execute(f"SELECT * FROM users WHERE login=?;", (login,))
    user = cur.fetchone()

    if not user:
        db_close(conn,cur)
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')
    if not check_password_hash(user['password'], password):
        db_close(conn,cur)
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')
    
    session['login'] = login
    db_close(conn,cur)
    return render_template('lab5/succes_login.html', login=login)


@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    if request.method == 'GET':
        return render_template('lab5/create_article.html')
    

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_favorite = request.form.get('is_favorite')
    is_public = request.form.get('is_public')


    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login,))
    login_id = cur.fetchone()["id"]
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"INSERT INTO articles(user_id, title, article_text, is_favorite, is_public) VALUES (%s, %s, %s, %s, %s);", (login_id, title, article_text, is_favorite, is_public))
    else:
        cur.execute(f"INSERT INTO articles(login_id, title, article_text) VALUES (?, ?, ?, ?, ?);", (login_id, title, article_text, is_favorite, is_public))
    db_close(conn, cur)
    return redirect('/lab5')


@lab5.route('/lab5/list')
def list():
    if 'login' in session:
        login = session['login']
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT id FROM users WHERE login=%s;", (login,))
        else:
            cur.execute(f"SELECT id FROM users WHERE login=?;", (login,))
        login_id = cur.fetchone()['id']
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM articles WHERE user_id=%s;", (login_id,))
        else:
            cur.execute(f"SELECT * FROM articles WHERE login_id=?;", (login_id,))
        articles = cur.fetchall()

        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM articles")
        else:
            cur.execute(f"SELECT * FROM articles")
            
        articles2 = cur.fetchall()
        db_close(conn, cur)
        return render_template('lab5/list.html', articles=articles, login=login, articles2 = articles2)
    

    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM articles")
    else:
        cur.execute(f"SELECT * FROM articles")
    articles2 = cur.fetchall()
    db_close(conn, cur)
    return render_template('lab5/list.html', articles2=articles2)


@lab5.route('/lab5/logout')
def logout2():
    session.pop('login', None)
    return redirect('/lab5/')



@lab5.route('/lab5/redact', methods=['GET', 'POST'])
def redact():
    if request.method == 'GET':
        return redirect('/lab5/')
    
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    article_title = request.form.get('article_title')
    article_text = request.form.get('article_text')
    article_id = request.form.get('article_id')
    is_favorite = request.form.get('is_favorite')
    is_public = request.form.get('is_public')
    return render_template('lab5/redact.html', article_text=article_text, article_title=article_title, article_id=article_id, is_favorite=is_favorite, is_public=is_public)


@lab5.route('/lab5/redact2', methods=['post'])
def redact2():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    article_title = request.form.get('article_title')
    article_text = request.form.get('article_text')
    article_id = request.form.get('article_id')
    is_favorite = request.form.get('is_favorite')
    is_public = request.form.get('is_public')
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT id FROM users WHERE login=%s;", (login,))
    else:
        cur.execute(f"SELECT id FROM users WHERE login=?;", (login,))


    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("UPDATE articles SET title=%s, article_text=%s, is_favorite=%s, is_public=%s WHERE id=%s;", (article_title, article_text, is_favorite, is_public, article_id))
    else:
        cur.execute("UPDATE articles SET title=?, article_text=?, is_favorite=?, is_public=? WHERE id=?;", (article_title, article_text, is_favorite, is_public, article_id))
    
    db_close(conn, cur)

    return redirect('/lab5/list')


@lab5.route('/lab5/delete', methods=['post'])
def delete_action():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    conn, cur = db_connect()
    article_id = request.form.get('article_id')
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM articles WHERE id=%s;", (article_id,))
    else:
        cur.execute("DELETE FROM articles WHERE id=?;", (article_id,))

    db_close(conn, cur)

    return redirect('/lab5/list')



@lab5.route('/lab5/all_login')
def all_login():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users")
    else:
        cur.execute("SELECT login FROM users")

    
    logins = cur.fetchall()

    db_close(conn, cur)

    return render_template('lab5/logins.html', logins = logins)