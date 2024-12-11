from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app
import sqlite3
import json
from os import path
import psycopg2
from psycopg2.extras import RealDictCursor
lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

films = [
    {
        'title': 'Interstellar',
        'title_ru': 'Интерстеллар',
        'year': 2014,
        'description': 'Когда засуха, пыльные бури и вымирание растений приводят человечество\
              к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь червоточину\
                  (которая предположительно соединяет области пространства-времени через большое расстояние) в путешествие, \
                    чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с подходящими для человечества условиями.'
    },
    {
        'title': 'The Shawshank Redemption',
        'title_ru': 'Побег из Шоушенка',
        'year': 1994,
        'description': 'Бухгалтер Энди Дюфрейн обвинён в убийстве собственной жены и её любовника. Оказавшись в тюрьме под названием\
              Шоушенк, он сталкивается с жестокостью и беззаконием, царящими по обе стороны решётки. Каждый, кто попадает в эти стены,\
                  становится их рабом до конца жизни. Но Энди, обладающий живым умом и доброй душой, находит подход как к заключённым, \
                    так и к охранникам, добиваясь их особого к себе расположения.'
    },
    {
        'title': 'Shutter Island',
        'title_ru': 'Остров проклятых',
        'year': 2009,
        'description': 'Два американских судебных пристава отправляются на один из островов в штате Массачусетс,\
              чтобы расследовать исчезновение пациентки клиники для умалишенных преступников. При проведении расследования\
                  им придется столкнуться с паутиной лжи, обрушившимся ураганом и смертельным бунтом обитателей клиники.'
    },
    {
        'title': 'Shrek',
        'title_ru': 'Шрэк',
        'year': 2001,
        'description': 'Жил да был в сказочном государстве большой зеленый великан по имени Шрэк.\
              Жил он в гордом одиночестве в лесу, на болоте, которое считал своим. Но однажды злобный\
                  коротышка — лорд Фаркуад, правитель волшебного королевства, безжалостно согнал на Шрэково\
                      болото всех сказочных обитателей.И беспечной жизни зеленого великана пришел конец. Но лорд\
                          Фаркуад пообещал вернуть Шрэку болото, если великан добудет ему прекрасную принцессу Фиону, \
                            которая томится в неприступной башне, охраняемой огнедышащим драконом.'
    },
    {
        'title': 'Intouchables',
        'title_ru': '1+1',
        'year': 2011,
        'description': 'Пострадав в результате несчастного случая, богатый аристократ Филипп нанимает\
              в помощники человека, который менее всего подходит для этой работы, – молодого жителя предместья\
                  Дрисса, только что освободившегося из тюрьмы. Несмотря на то, что Филипп прикован к инвалидному\
                      креслу, Дриссу удается привнести в размеренную жизнь аристократа дух приключений.'
    },

]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    path = url_for('static', filename='lab1/goblin.png')
    path_css = url_for("static", filename='lab1/lab1.css')
    if id < 0 or id > len(films)-1:
        return '''
    <!doctype html>
    <link rel="stylesheet" href="'''+path_css+'''">
    <html>
        <head>
        </head>
        <main>
            <div class="trabl">Ты походу не тута :)</div>
            <img class="image2" src="''' +path+ '''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 404
    return films[id]


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_films(id):
    path = url_for('static', filename='lab1/goblin.png')
    path_css = url_for("static", filename='lab1/lab1.css')
    if id < 0 or id > len(films)-1:
        return '''
    <!doctype html>
    <link rel="stylesheet" href="'''+path_css+'''">
    <html>
        <head>
        </head>
        <main>
            <div class="trabl">Ты походу не тута :)</div>
            <img class="image2" src="''' +path+ '''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 404
    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_films(id):
    path = url_for('static', filename='lab1/goblin.png')
    path_css = url_for("static", filename='lab1/lab1.css')
    if id < 0 or id > len(films)-1:
        return '''
    <!doctype html>
    <link rel="stylesheet" href="'''+path_css+'''">
    <html>
        <head>
        </head>
        <main>
            <div class="trabl">Ты походу не тута :)</div>
            <img class="image2" src="''' +path+ '''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 404
    film = request.get_json()
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    films[id]=film
    return films[id]


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_films():
    film = request.get_json()
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    print(f"Title: {film.get('title')}, Title RU: {film.get('title_ru')}")
    if film['title'] == '':
        film['title'] = film.get('title_ru', '')
        films.append(film)
        return len(films)-1
    films.append(film)
    return len(films)-1
