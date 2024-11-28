from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app
import sqlite3
import json
from os import path
import psycopg2
from psycopg2.extras import RealDictCursor
lab6 = Blueprint('lab6', __name__)
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



@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    if data['method'] == 'info':
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM offices")
            offices = cur.fetchall()
        else: 
            cur.execute(f"SELECT * FROM offices")
            def clean_value(value):
                return value if value is not None else ''
            rows = cur.fetchall()
            offices = [{key: clean_value(value) for key, value in zip(cur.description, row)} for row in rows]
            offices = json.dumps(offices)
        db_close(conn,cur)
        return {
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        }
    
    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0',
            'error':{
                'code': 1,
                'message': 'Unauthorized'
            }
        }
    
    if data['method'] == 'price':
        if not login:
            return{
                'jsonrpc': '2.0',
                'error':{
                'code': 1,
                'message': 'Unauthorized'
            },
                'id': id
            }
        endprice = 0
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM offices")
        else: 
            cur.execute(f"SELECT * FROM offices")
        offices = cur.fetchall()
        for office in offices:
            if office['tenant'] == login:
                endprice = endprice+office['price']
        db_close(conn,cur)
        
        return{
            'jsonrpc': '2.0',
            'endprice': endprice,
            'id': id
        }
        
    



    if data['method'] == 'booking':
        office_number = data['params']
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM offices")
        else: 
            cur.execute(f"SELECT * FROM offices")
        offices = cur.fetchall()
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] != '':
                    return{
                        'jsonrpc': '2.0',
                        'error':{
                            'code': 2,
                            'message': 'Alredy booked'
                        },
                        'id': id
                    }
                if current_app.config['DB_TYPE'] == 'postgres':
                    cur.execute("UPDATE offices SET tenant=%s WHERE number=%s;", (login,office_number))
                else:
                    cur.execute("UPDATE offices SET tenant=? WHERE number=?;", (login,office_number))
                db_close(conn, cur)
                return {
                    'jsonrpc': '2.0',
                    'result': 'succes',
                    'id': id
                }
    if data['method'] == 'cancellation':
        office_number = data['params']
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM offices")
        else: 
            cur.execute(f"SELECT * FROM offices")
        offices = cur.fetchall()
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] == '':
                    return {
                        'jsonroc': '2.0',
                        'error':{
                            'code': 3,
                            'message': 'Not booked'
                        },
                        'id': id
                    }
                if not login:
                    return{
                        'jsonrpc': '2.0',
                        'error':{
                        'code': 1,
                        'message': 'Unauthorized'
                    }
                    }
                if office['tenant'] != login:
                    return{
                        'jsonroc': '2.0',
                        'error':{
                            'code': 4,
                            'message': 'You cannot'
                        },
                        'id': id
                    }

                if current_app.config['DB_TYPE'] == 'postgres':
                    cur.execute("UPDATE offices SET tenant=%s WHERE number=%s;", ('',office_number))
                else:
                    cur.execute("UPDATE offices SET tenant=? WHERE number=?;", ('',office_number))
                db_close(conn, cur)
                return {
                    'jsonrpc': '2.0',
                    'result': 'succes',
                    'id': id
                }
                

    return {
        'jsonrpc': '2.0',
        'error':{
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }