from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app, jsonify
import sqlite3
import json
from os import path
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
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
    login = session.get('login')
    if login:
        return render_template('rgz_gavrilov/rgz_gavrilov.html', login=login)
    else:
        return render_template('rgz_gavrilov/rgz_gavrilov.html')


@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/', methods=['GET'])
def get_recipes():
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM recipes")
        recipes = cur.fetchall()
    else: 
        cur.execute(f"SELECT * FROM recipes")
        recipes = [dict(row) for row in cur.fetchall()]
    db_close(conn,cur)
    return recipes

@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/<int:id>', methods=['GET'])
def get_recipe(id):
    login = session.get('login')
    if login:
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM recipes WHERE id={id}")
            recipes = cur.fetchone()
        else: 
            cur.execute(f"SELECT * FROM recipes WHERE id={id}")
            recipes = [dict(row) for row in cur.fetchone()]
        db_close(conn,cur)
        return recipes
    else:
        return {'recipes': 123}, 401
    


@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/not/<int:id>', methods=['GET'])
def get_recipe_not(id):
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM recipes WHERE id={id}")
        recipes = cur.fetchone()
    else: 
        cur.execute(f"SELECT * FROM recipes WHERE id={id}")
        recipes = [dict(row) for row in cur.fetchone()]
    db_close(conn,cur)
    return recipes








@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/', methods=['PUT'])
def put_recipe():
    recipe = request.get_json()
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("UPDATE recipes set name=%s, ingredients=%s, steps=%s, photo=%s WHERE id=%s", (recipe['name'], recipe['ingredients'], recipe['steps'], recipe['photo'], recipe['id']))
    else: 
        cur.execute("UPDATE recipes set name=?, ingredients=?, steps=?, photo=? WHERE id=?", (recipe['name'], recipe['ingredients'], recipe['steps'], recipe['photo'], recipe['id']))
    db_close(conn,cur)
    return ""

@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM recipes WHERE id=%s", (id,))
    else: 
        cur.execute("DELETE FROM recipes WHERE id=?", (id,))
    db_close(conn,cur)
    return ""

@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/search/', methods=['GET'])
def get_recipe_search_name2():
    return {'result': 0}, 400



@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/search/<name>', methods=['GET'])
def get_recipe_search_name(name):
    if name == '':
        return {'result': 0}, 400
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM recipes WHERE name ILIKE %s", ('%' + name + '%',))
    else: 
        cur.execute("SELECT * FROM recipes WHERE name LIKE ?", ('%' + name + '%',))
    
    recipes = cur.fetchall() 
    db_close(conn, cur)
    if recipes:
        return recipes
    else:
        return {'result': 0}, 400
    


@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/search/or', methods=['POST'])
def search_or():
    data = request.get_json()
    result = []
    conn, cur = db_connect()
    for i in (data['ingredients']):
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT * FROM recipes WHERE ingredients ILIKE %s", ('%' + i + '%',))
            recipes = cur.fetchall()
            result.extend(recipes)  
        else: 
            cur.execute("SELECT * FROM recipes WHERE ingredients LIKE ?", ('%' + i + '%',))
            recipes = cur.fetchall()
            result.extend(recipes)  
    db_close(conn, cur)
    if result:
        return jsonify(result), 200
    else:
        return {'result': 0}, 400


@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/search/and', methods=['POST'])
def search_and():
    data = request.get_json()
    result = []
    conn, cur = db_connect()
    # Начнем с базового запроса
    query = "SELECT * FROM recipes WHERE"
    conditions = []
    params = []

    # Создаем кортеж из списка ингредиентов
    ingredients_list = data['ingredients']
    for i in ingredients_list:
        conditions.append("ingredients ILIKE %s")
        params.append('%' + i + '%')

    # Объединяем условия с оператором AND
    query += ' ' + ' AND '.join(conditions)

    # Выполняем запрос с параметрами
    cur.execute(query, params)

    recipes = cur.fetchall()
    result.extend(recipes)

    db_close(conn, cur)

    if result:
        return jsonify(result), 200
    else:
        return {'result': 0}, 400
    


@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/login', methods=['GET','POST'])
def login_main():
    if request.method == 'GET':
        return redirect('/rgz/')
    
    login = request.form.get('login')
    password = request.form.get('password')
    conn, cur = db_connect()


    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM admin WHERE login=%s;", (login,))
    else:
        cur.execute(f"SELECT * FROM admin WHERE login=?;", (login,))
    admin = cur.fetchone()

    if not admin:
        db_close(conn,cur)
        return render_template('rgz_gavrilov/rgz_gavrilov.html', error_login='Логин и/или пароль неверны')
    if not check_password_hash(admin['password'], password):
        db_close(conn,cur)
        return render_template('rgz_gavrilov/rgz_gavrilov.html', error_login='Логин и/или пароль неверны')
    session['login'] = login
    db_close(conn,cur)
    return redirect('/rgz/')


@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/logout', methods=['POST'])
def logout_main():
    session.pop('login', None)
    return redirect('/rgz/')



@rgz_gavrilov.route('/rgz/rest-api/rgz_gavrilov/add', methods=['POST'])
def addd():
    data = request.get_json()
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"INSERT INTO recipes (name, ingredients, steps, photo) VALUES (%s, %s, %s, %s);", (data['name'],data['ingredients'], data['steps'], data['photo']))
    else:
        cur.execute(f"INSERT INTO recipes (name, ingredients, steps, photo) VALUES (?, ?, ?, ?);", (data['name'],data['ingredients'], data['steps'], data['photo']))
    db_close(conn,cur)
    return {}, 200