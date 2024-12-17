from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app, jsonify
import sqlite3
import json
from os import path
from db import db
from db.models import users, articles
from datetime import datetime
import psycopg2
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from psycopg2.extras import RealDictCursor
lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def main_l8():
    if current_user.is_authenticated:
        return render_template('/lab8/lab8.html',login={current_user.login})
    else:
        return render_template('/lab8/lab8.html')


@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')

    login_form = request.form.get('login')
    password_form = request.form.get('password')

    login_exists = users.query.filter_by(login=login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')

    password_hash = generate_password_hash(password_form)
    new_user = users(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    user = users.query.filter_by(login=login_form).first()
    login_user(user, remember=False)
    return redirect('/lab8')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    user = users.query.filter_by(login=login_form).first()

    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember=False)
            return redirect('/lab8')
    return render_template('/lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')


@lab8.route('/lab8/articles')
def articles_list():
    if current_user.is_authenticated:
        articles_list_1 = articles.query.filter_by(user_id=current_user.id).all()
        articles_list_2 = articles.query.filter_by (is_public = True).all()
        return render_template('/lab8/articles.html', articles = articles_list_1, login = current_user.login, articles2 = articles_list_2)
    else:
        articles_list_2 = articles.query.filter_by(is_public = True).all()
        return render_template('/lab8/articles.html', articles2 = articles_list_2)


@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create2():
    if request.method == 'GET':
        return render_template('/lab8/create.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_favorite = request.form.get('is_favorite') == 'on'
    is_public = request.form.get('is_public') == 'on'

    new_article = articles(
        user_id=current_user.id,
        title=title,
        article_text=article_text,
        is_public=is_public,
        is_favorite=is_favorite
    )
    db.session.add(new_article)
    db.session.commit()
    return redirect('/lab8/articles')


@lab8.route('/lab8/redact', methods=['POST'])
def redact_1():
    article_title = request.form.get('article_title')
    article_text = request.form.get('article_text')
    article_id = request.form.get('article_id')
    is_favorite = request.form.get('is_favorite')
    is_public = request.form.get('is_public')
    return render_template('lab8/redact.html', article_text=article_text, article_title=article_title, article_id=article_id, is_favorite=is_favorite, is_public=is_public)


@lab8.route('/lab8/redact2', methods=['POST'])
def redact_2():
    article_title = request.form.get('article_title')
    article_text = request.form.get('article_text')
    article_id = request.form.get('article_id')
    is_favorite = request.form.get('is_favorite') == 'on' 
    is_public = request.form.get('is_public') == 'on' 

    article = articles.query.get_or_404(article_id)

    article.title = article_title
    article.article_text = article_text
    article.is_public = is_public
    article.is_favorite = is_favorite
    db.session.commit()

    return redirect('/lab8/articles')



@lab8.route('/lab8/delete', methods=['post'])
def delete_act():
    article_id = request.form.get('article_id')
    article = articles.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    return redirect ('/lab8/articles')

@lab8.route('/lab8/search/me', methods=['POST'])
def search_me():
    search = request.form.get('search')
    if current_user.is_authenticated:
        articles_list_1 = articles.query.filter(articles.user_id==current_user.id, articles.title.ilike(f"%{search}%")).all()
        articles_list_2 = articles.query.filter(articles.title.ilike(f"%{search}%"), articles.is_public == True)
        if articles_list_1 or articles_list_2:
            return render_template('/lab8/articles.html', articles = articles_list_1, login = current_user.login, articles2 = articles_list_2, search=search)
        else:
            return render_template('/lab8/articles.html', error='По вашему запросу ничего не найдено')
    else:
        articles_list_2 = articles.query.filter(articles.title.ilike(f"%{search}%"), articles.is_public == True)
        if articles_list_2:
            return render_template('/lab8/articles.html', articles2 = articles_list_2, search=search)
        else:
            return render_template('/lab8/articles.html', error='По вашему запросу ничего не найдено')