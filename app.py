from flask import Flask, url_for, redirect
app = Flask(__name__)
@app.route("/lab1/web")
def start():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/author">author</a>
                    </body>
                        </html>""", 200 , {'X-Server': 'sample', 'Content-Type': 'text/plain; charset=utf-8'}
@app.route("/lab1/author")
def author():
    name = "Гаврилов Дмитрий Дмитриевич"
    group = "ФБИ-21"
    faculty = "ФБ"
    
    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """<p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
            </html>"""
@app.route("/lab1/oak")
def oak():
    path = url_for("static", filename="oak.jpg")
    path_css = url_for("static", filename='lab1.css')
    return'''
<!doctype html>
<link rel="stylesheet" href="'''+path_css+'''">
<html>
    <body>
        <h1>Дуб</h1>
        <img class='image' src="''' +path+ '''">
    </body>
</html>
'''
count = 0
@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return'''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <a href="/lab1/counternull">Обнуление счетчика</a>
    </body>
</html>
'''
@app.route('/lab1/counternull')
def counternull():
    global count
    count = 0
    return'''
<!doctype html>
<html>
    <body>
        Страница было очищена
        <a href="/lab1/counter">Обратно на страницу</a>
    </body>
</html>
'''



@app.route('/lab1/info')
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return'''
    <!doctype html>
    <html>
        <body>
            <h1>Создано успешно</h1>
            <div><i>что-то создано...</i></div>
        </body>
    </html>
    ''',201
@app.errorhandler(404)
def not_found(err):
    path = url_for('static', filename='goblin.png')
    path_css = url_for("static", filename='lab1.css')
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
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
        <head>
            <h1>НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных</h1>
        </head>
        <main>
            <ol>
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2">Вторая лабораторная</a></li>
                <li><a href="/lab3">Третья лабораторная</a></li>
                <li><a href="/lab4">Четвертая лабораторная</a></li>
                <li><a href="/lab5">Пятая лабораторная</a></li>
                <li><a href="/lab6">Шестая лабораторная</a></li>
            </ol>
        </main>
        <footer>
            <div>Гаврилов Дмитрий Дмитриевич, ФБИ-21, 3 курс, 2024</div>
        </footer>
    </html>
    '''
@app.route("/lab1")
def lab1():
    return'''
        <!doctype html>
        <title>Лабораторная работа 1</title>
        <html>
            <head>
                <h1>НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных</h1>
            </head>
            <main>
                <div>
                    Flask — фреймворк для создания веб-приложений на языке
                    программирования Python, использующий набор инструментов
                    Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                    называемых микрофреймворков — минималистичных каркасов
                    веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
                </div>
                <h2>Списки роутов</h2>
                <ol>
                    <li>
                       <a href="/lab1/web">WEB</a> 
                    </li>
                    <li>
                        <a href="/lab1/author">Автор</a>
                    </li>
                        
                    <li>
                        <a href="/lab1/oak">Дуб</a>
                    </li>
                    <li>
                        <a href="/lab1/counter">Счетчик</a>
                    </li>
                    <li>
                        <a href="/lab1/counternull">Сброс счетчика</a>
                    </li>
                    <li>
                        <a href="/lab1/created">Что то создано</a>
                    </li>
                    <li>
                        <a href="/lab1/info">Перенаправление</a>
                    </li>
                    <li>
                        <a href="/index">Список</a>
                    </li>
                    <li>
                        <a href="/lab1/zagolovki">Заголовки</a>
                    </li>
                    <li>
                        <a href="/400">Ошибка 400</a>
                    </li>
                    <li>
                        <a href="/401">Ошибка 401</a>
                    </li>
                    <li>
                        <a href="/402">Ошибка 402</a>
                    </li>
                    <li>
                        <a href="/403">Ошибка 403</a>
                    </li>
                    <li>
                        <a href="/405">Ошибка 405</a>
                    </li>
                    <li>
                        <a href="/418">Ошибка 418</a>
                    </li>
                    <li>
                        <a href="/error_500">Ошибка 500</a>
                    </li>
                </ol>
                <a href="/">Все лабы</a>
            </main>
            <footer>
                <div>Гаврилов Дмитрий Дмитриевич, ФБИ-21, 3 курс, 2024</div>
            </footer>
        </html>
        '''
@app.route("/400")
def l400():
    return "Допущена синтаксическая ошибка", 400

@app.route("/401")
def l401():
    return "Требуется аутентификация", 401

@app.route("/402")
def l402():
    return "Требуется оплата", 402

@app.route("/403")
def l403():
    return "Нету полномочий", 403

@app.route("/405")
def l405():
    return "Недопустимый метод", 405

@app.route("/418")
def l418():
    return "Я чайник", 418

@app.route("/error_500")
def error_go():
    res = 1/0
    return res

@app.errorhandler(500)
def error_500(err):
    return "Внутренняя ошибка сервера", 500

@app.route("/lab1/zagolovki")
def lab11():
    path = url_for("static", filename='rubick.jpg')
    path_css = url_for("static", filename='lab1_rubick.css')
    return'''
        <!doctype html>
        <title>Лабораторная работа 1</title>
        <html>
            <head>
                <h1>НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных</h1>
            </head>
            <main>
                <p>
                    История создания самой известной и оригинальной игрушки-головоломки
                    начинается с марта 1970 года. Американский изобретатель Ларри Николс
                    изобрел головоломку в виде кубика 2х2х2 с подвижными, поворачивающимися частями,
                    и сразу же запатентовал свое изобретение.
                </p>
                <p>
                    Классический кубик Рубика состоит из граней 3х3, каждая окрашена в один из 6 цветов.
                    Игрушка выполнена из пластика, подходит для игр детям от 6-ти лет. Каждый маленький куб вращается вокруг 3
                    внутренних осей. Каждая грань состоит из 9 квадратиков, всего их 54.
                </p>
                <p>
                    Сегодня без труда можно найти специальные алгоритмы, на YouTube-каналах множество видео-уроков,
                    просмотрев которые, вы сможете без труда собрать кубик Рубика, постоянно совершенствуя свое мастерство,
                    увеличивая скорость сборки. Классическая развивающая игрушка поможет занять руки и голову не только ребенка, но и родителей.
                </p>
                <a href="/">Все лабы</a>
                <img class="rubick_image" src="'''+path+'''">
            </main>
            <footer>
                <div>Гаврилов Дмитрий Дмитриевич, ФБИ-21, 3 курс, 2024</div>
            </footer>
        </html>
        ''',200, {'Content-language': 'ru', 'From': 'bilobilo :))))', 'Allow':'GET'}