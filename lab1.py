from flask import Blueprint, url_for, redirect
lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1/web")
def start():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/author">author</a>
                    </body>
                        </html>""", 200 , {'X-Server': 'sample', 'Content-Type': 'text/plain; charset=utf-8'}


@lab1.route("/lab1/author")
def author():
    authorcss = url_for("static", filename='lab1/author.css')
    oak = url_for("static", filename='lab1/Oak-Tree-PNG.png')
    name = "Гаврилов Дмитрий Дмитриевич"
    group = "ФБИ-21"
    faculty = "ФБ"
    return '''
        <!doctype html>
        <link rel="stylesheet" href="'''+ authorcss +'''">
        <html>
            <body>
                <div class="authordiv">
                    <p>Студент: "''' + name + ''' "<p>
                    <p>Группа: "''' + group + '''"</p>
                    <p>Факультет: "''' + faculty + '''"</p>
                    <a href="/lab1/web">web</a>
                </div>
                <img class="oaktree" src="'''+oak+'''">
            </body>
            </html>'''


@lab1.route("/lab1/oak")
def oak():
    path = url_for("static", filename="lab1/oak.jpg")
    path_css = url_for("static", filename='lab1/lab1.css')
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
@lab1.route('/lab1/counter')
def counter():
    countercss = url_for("static", filename="lab1/counter.css")
    oak = url_for("static", filename='lab1/Oak-Tree-PNG.png')
    global count
    count += 1
    return'''
<!doctype html>
<link rel="stylesheet" href="'''+ countercss +'''">
<html>
    <body>
        <div class="firstcounter">
            Сколько раз вы сюда заходили: ''' + str(count) + '''
            <a href="/lab1/counternull">Обнуление счетчика</a>
        </div>
        <img class="oaktree" src="'''+oak+'''">
    </body>
</html>
'''


@lab1.route('/lab1/counternull')
def counternull():
    countercss = url_for("static", filename="lab1/counter.css")
    oak = url_for("static", filename='lab1/Oak-Tree-PNG.png')
    global count
    count = 0
    return'''
<!doctype html>
<link rel="stylesheet" href="'''+ countercss +'''">
<html>
    <body>
        <div class="secondcounter">
            Страница было очищена
            <a href="/lab1/counter">Обратно на страницу</a>
        </div>
        <img class="oaktree" src="'''+oak+'''">
    </body>
</html>
'''


@lab1.route('/lab1/info')
def info():
    return redirect("/lab1/author")


create = 0
@lab1.route("/lab1/created")
def created():
    countercss = url_for("static", filename="lab1/counter.css")
    oak = url_for("static", filename='lab1/Oak-Tree-PNG.png')
    global create
    if create == 0:
        create = 1
        return'''
        <!doctype html>
        <link rel="stylesheet" href="'''+ countercss +'''">
        <html>
            <body>
                <div class="resurscreate">
                    <h1>Ресурс успешно создан!</h1>
                </div>
                <img class="treere"src="'''+oak+'''">
            </body>
        </html>
        ''',201
    else:
        return'''
        <!doctype html>
        <link rel="stylesheet" href="'''+ countercss +'''">
        <html>
            <body>
                <div class="resurscreate">
                    <h1>Отказано! Ресурс уже есть</h1>
                </div>
                <img class="treere"src="'''+oak+'''">
            </body>
        </html>
        ''',400
    

@lab1.route("/lab1/delete")
def deleted():
    countercss = url_for("static", filename="lab1/counter.css")
    oak = url_for("static", filename='lab1/Oak-Tree-PNG.png')
    global create
    if create == 1:
        create = 0
        return'''
        <!doctype html>
        <link rel="stylesheet" href="'''+ countercss +'''">
        <html>
            <body>
                <div class="resurscreate">
                    <h1>Ресурс удален!</h1>
                </div>
                <img class="treere"src="'''+oak+'''">
            </body>
        </html>
        ''',200
    else:
        return'''
        <!doctype html>
        <link rel="stylesheet" href="'''+ countercss +'''">
        <html>
            <body>
                <div class="resurscreate">
                    <h1>Ресурс отсутсвует!</h1>
                </div>
                <img class="treere"src="'''+oak+'''">
            </body>
        </html>
        ''',400
    

@lab1.route("/lab1/resurce")
def resurce():
    countercss = url_for("static", filename="lab1/counter.css")
    oak = url_for("static", filename='lab1/Oak-Tree-PNG.png')
    global create
    return'''
    <!doctype html>
    <link rel="stylesheet" href="'''+ countercss +'''">
    <html>
        <body>
            <div class="resurcemain">
                <div>Статус ресурса: '''+str(create)+'''</div>
                <p><a href="/lab1/created">Создать ресурс!</a></p>
                <p><a href="/lab1/delete">Удалить ресурс!</a></p>
            </div>
            <img class="oaktree2" src="'''+oak+'''">
        </body>
    </html>
    ''',200


@lab1.route("/lab1")
def lab():
    labb1css = url_for("static", filename="lab1/labb1.css")
    oak = url_for("static", filename="lab1/Oak-Tree-PNG.png")
    return'''
        <!doctype html>
        <title>Лабораторная работа 1</title>
        <link rel="stylesheet" href="'''+labb1css+'''">
        <html>
            <head>
                <h1>НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных</h1>
            </head>
            <main>
                <div class="flask">
                    Flask — фреймворк для создания веб-приложений на языке
                    программирования Python, использующий набор инструментов
                    Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                    называемых микрофреймворков — минималистичных каркасов
                    веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
                </div>
                <h2>Списки роутов</h2>
                <div class="list">
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
                            <a href="/lab1/resurce">Ресурс (доп задание)</a>
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
                </div>
                <a class="alllab" href="/">Все лабораторные работы</a>
                <img class="oak" src="'''+oak+'''">
            </main>
            <footer>
                <div class="fotterr">Гаврилов Дмитрий Дмитриевич, ФБИ-21, 3 курс, 2024</div>
            </footer>
        </html>
        '''


@lab1.route("/lab1/zagolovki")
def lab11():
    path = url_for("static", filename='lab1/rubick.png')
    path_css = url_for("static", filename='lab1/lab1_rubick.css')
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
