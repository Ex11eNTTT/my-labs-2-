from flask import Flask, url_for, session
import os
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Никому не говори пжпж')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)

@app.errorhandler(404)
def not_found(err):
    path = url_for('static', filename='lab1/goblin.png')
    path_css = url_for("static", filename='lab1/lab1.css')
    return'''
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

@app.route("/")
@app.route("/index")
def index():
    indexcss = url_for('static', filename="lab1/indexcss.css")
    oak = url_for("static", filename='lab1/Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+indexcss+'''">
        <head>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </head>
        <main>
            <div class="spisok">
                <ol>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                    <li><a href="/lab2">Вторая лабораторная</a></li>
                    <li><a href="/lab3">Третья лабораторная</a></li>
                    <li><a href="/lab4">Четвертая лабораторная</a></li>
                    <li><a href="/lab5">Пятая лабораторная</a></li>
                    <li><a href="/lab6">Шестая лабораторная</a></li>
                    <li><a href="/lab7">Седьмая лабораторная</a></li>
                </ol>
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
            <div class="fotterr">Гаврилов Дмитрий Дмитриевич, ФБИ-21, 3 курс, 2024</div>
        </footer>
    </html>
    '''

    path = url_for("static", filename='rubick.png')
    path_css = url_for("static", filename='lab1_rubick.css')
    return'''
        <!doctype html>
        <link rel="stylesheet" href="'''+path_css+'''">
        <title>Лабораторная работа 1</title>
        <html>
            <head>
                <h1>НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных</h1>
            </head>
            <main>
                <p class="firsttext">
                    История создания самой известной и оригинальной игрушки-головоломки
                    начинается с марта 1970 года. Американский изобретатель Ларри Николс
                    изобрел головоломку в виде кубика 2х2х2 с подвижными, поворачивающимися частями,
                    и сразу же запатентовал свое изобретение.
                </p>
                <p class="secondtext">
                    Классический кубик Рубика состоит из граней 3х3, каждая окрашена в один из 6 цветов.
                    Игрушка выполнена из пластика, подходит для игр детям от 6-ти лет. Каждый маленький куб вращается вокруг 3
                    внутренних осей. Каждая грань состоит из 9 квадратиков, всего их 54.
                </p>
                <p class="thirsttext">
                    Сегодня без труда можно найти специальные алгоритмы, на YouTube-каналах множество видео-уроков,
                    просмотрев которые, вы сможете без труда собрать кубик Рубика, постоянно совершенствуя свое мастерство,
                    увеличивая скорость сборки. Классическая развивающая игрушка поможет занять руки и голову не только ребенка, но и родителей.
                </p>
                <a href="/">Все лабораторные</a>
                <img class="rubick_image" src="'''+path+'''">
                <img class="rubick_image2" src="'''+path+'''">
                <img class="rubick_image3" src="'''+path+'''">
            </main>
            <footer>
                <div class="fotterr">Гаврилов Дмитрий Дмитриевич, ФБИ-21, 3 курс, 2024</div>
            </footer>
        </html>
        ''',200, {'Content-language': 'ru', 'From': 'bilobilo :))))', 'Allow':'GET'}