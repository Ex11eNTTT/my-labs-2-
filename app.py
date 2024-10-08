from flask import Flask, url_for, redirect, render_template, request
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
    authorcss = url_for("static", filename='author.css')
    oak = url_for("static", filename='Oak-Tree-PNG.png')
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
    countercss = url_for("static", filename="counter.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
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
@app.route('/lab1/counternull')
def counternull():
    countercss = url_for("static", filename="counter.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
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



@app.route('/lab1/info')
def info():
    return redirect("/lab1/author")


create = 0
@app.route("/lab1/created")
def created():
    countercss = url_for("static", filename="counter.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
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
@app.route("/lab1/delete")
def deleted():
    countercss = url_for("static", filename="counter.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
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
    
@app.route("/lab1/resurce")
def resurce():
    countercss = url_for("static", filename="counter.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
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
    indexcss = url_for('static', filename="indexcss.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
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
                </ol>
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
            <div class="fotterr">Гаврилов Дмитрий Дмитриевич, ФБИ-21, 3 курс, 2024</div>
        </footer>
    </html>
    '''


@app.route("/lab1")
def lab1():
    labb1css = url_for("static", filename="labb1.css")
    oak = url_for("static", filename="Oak-Tree-PNG.png")
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
@app.route("/400")
def l400():
    countercss = url_for("static", filename="lab1_rubick.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+countercss+'''">
        <head>
        </head>
        <main>
            <div class="error">
                Допущена синтаксическая ошибка
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
        </footer>
    </html>
    ''' , 400

@app.route("/401")
def l401():
    countercss = url_for("static", filename="lab1_rubick.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+countercss+'''">
        <head>
        </head>
        <main>
            <div class="error">
                Требуется аутентификация
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
        </footer>
    </html>
    ''' , 401

@app.route("/402")
def l402():
    countercss = url_for("static", filename="lab1_rubick.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+countercss+'''">
        <head>
        </head>
        <main>
            <div class="error">
                Требуется оплата
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 402

@app.route("/403")
def l403():
    countercss = url_for("static", filename="lab1_rubick.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+countercss+'''">
        <head>
        </head>
        <main>
            <div class="error">
                Нету полномочий
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 403

@app.route("/405")
def l405():
    countercss = url_for("static", filename="lab1_rubick.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+countercss+'''">
        <head>
        </head>
        <main>
            <div class="error">
                Недопустимый метод
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 405

@app.route("/418")
def l418():
    countercss = url_for("static", filename="lab1_rubick.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+countercss+'''">
        <head>
        </head>
        <main>
            <div class="error">
                Я чайник
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 418

@app.route("/error_500")
def error_go():
    res = 1/0
    return res

@app.errorhandler(500)
def error_500(err):
    countercss = url_for("static", filename="lab1_rubick.css")
    oak = url_for("static", filename='Oak-Tree-PNG.png')
    return'''
    <!doctype html>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <html>
    <link rel="stylesheet" href="'''+countercss+'''">
        <head>
        </head>
        <main>
            <div class="error">
                Внутренняя ошибка сервера
            </div>
            <img class="oak" src="'''+oak+'''">
        </main>
        <footer>
        </footer>
    </html>
    ''', 500

@app.route("/lab1/zagolovki")
def lab11():
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




# Лабораторная работа 2
@app.route('/lab2/a')
def a():
    return 'без слеша'

@app.route('/lab2/a/')
def a2():
    return 'со слешем'



@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a,b):
    first = a
    second = b
    return render_template('calc.html', first = first, second = second)

@app.route('/lab2/calc/')
def redcalc():
    return redirect("/lab2/calc/1/1")

@app.route('/lab2/calc/<int:a>')
def redcalccc(a):
    return redirect(f"/lab2/calc/{a}/1")

books = [{'name': 'Девушка во льду', 'author': 'Роберт Брындза', 'genre': 'Детектив', 'countlist': 200},
         {'name': 'Лунный камень', 'author': 'Уилки Коллинз', 'genre': 'Детектив', 'countlist': 144},
         {'name': 'Ребекка', 'author': 'Дафна Дюморье', 'genre': 'Детектив', 'countlist': 60},
         {'name': 'Талантливый мистер Рипли', 'author': 'Патриция Хайсмит', 'genre': 'Детектив', 'countlist': 300},
         {'name': 'Властелин Колец', 'author': 'Джон Рональд Руэл Толкин', 'genre': 'Фентези', 'countlist': 500},
         {'name': 'Геральт', 'author': 'Анджей Сапковский', 'genre': 'Фентези', 'countlist': 250},
         {'name': 'Колдовской мир', 'author': 'Андрэ Нортон', 'genre': 'Фентези', 'countlist': 200},
         {'name': 'Конан', 'author': 'Роберт Ирвин', 'genre': 'Фентези', 'countlist': 210},
         {'name': 'Тёмный эльф', 'author': 'Роберт Энтони', 'genre': 'Фентези', 'countlist': 230},
         {'name': 'Сага о копье', 'author': 'Маргарет Уэйс, Трейси Хикмен', 'genre': 'Фентези', 'countlist': 200}]

@app.route('/lab2/books')
def bookss():
    return render_template('books.html', books=books)
    
spisokyagod = [{'name': 'Арбуз', 'photo': '/static/watermelon.png', 'description':
                'Это самая крупная в мире ягодная культура. Вес отдельных плодов достигает 30 кг. Арбузы'
                'используются не только в пищу: их целебные свойства были оценены косметологами. На основе'
                'измельченных косточек делают кремы и скрабы, антицеллюлитные средства.'},
                {'name': 'Барбис', 'photo': '/static/barbaris.png', 'description': 'Брусника — низкорослый вечнозеленый кустарник'
                  'с небольшими ягодами ярко-красного цвета. Это дикая культура растет в условиях умеренного климата: в тундре и таежных лесах.'
                    'Полезными свойствами обладают все части растения: побеги, стебли, листья, ягоды. Плоды предпочитают потреблять сырыми: в '
                    'таком виде они сохраняют максимум витаминов.'},{'name': 'Голубика', 'photo': '/static/golubika.png', 'description': 'Вишня — это дерево или кустарник'
                  'с несколькими стволами (в зависимости от сорта). Ягоды вишни — овальные с косточкой внутри.'
                    'Созревание ягод происходит в период с июня по июль, но на одном дереве все ягоды созревают практически одновременно.'},{
                        'name': 'Брусника', 'photo': '/static/brusnika.png', 'description': 'Брусника — низкорослый вечнозеленый кустарник с небольшими'
                          'ягодами ярко-красного цвета. Это дикая культура растет в условиях умеренного климата: в тундре и таежных лесах. Полезными'
                            'свойствами обладают все части растения: побеги, стебли, листья, ягоды. Плоды предпочитают потреблять сырыми: в таком виде'
                              'они сохраняют максимум витаминов.'
                    },{'name': 'Клубника', 'photo': '/static/klubnika.png', 'description': 'Клубника — многолетняя травянистая культура. Оно относится к'
                        'семейству розоцветных. Ягоды на стебле появляются через 20-26 дней с начала цветения.'
                    }]

@app.route('/lab2/yagodi')
def yagodis():
    return render_template('yagodi.html', yagoda = spisokyagod)




@app.route('/lab2/example')
def example():
    student = 'Дмитрий Дмитриевич'
    numberlab = 'Лабораторная работа 2'
    numbercourse = '3'
    numbergroup = 'ФБИ-21'
    fruits = [{'name':'яблоки', 'price':100},{'name':'груши', 'price':120},{'name':'апельсины', 'price':80},
              {'name':'мандарины', 'price':95},{'name':'манго', 'price':321},]
    return render_template('example.html', name=student, lab=numberlab,  course = numbercourse, group = numbergroup, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filtres')
def filtres():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)




flower_list=[{'name':'роза', 'price': 100},{'name':'тюльпан', 'price': 150}, {'name':'незабудка', 'price': 220},{'name':'ромашка', 'price': 50}]

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list)+1:
        return render_template('ifflower.html'), 404
    else:
        selected_flower = flower_list[flower_id-1]
        selected_flowerlol = f"Название: {selected_flower['name']}, Цена: {selected_flower['price']}"
        return render_template('ifflower2.html', selected_flowerlol = selected_flowerlol)

@app.route('/lab2/flowers_delete')
def flowersdelete():
    flower_list.clear()
    return  render_template('flowerdelete.html')

@app.route('/lab2/flowers_delete/<int:delete_flower_id>')

def flowerdelete(delete_flower_id):
    if delete_flower_id <= len(flower_list):
        del flower_list[delete_flower_id-1]
        return redirect('/lab2/flower/countandnames')
    else:
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


@app.route('/lab2/ad_flowerrr/', methods=['POST'])
def addflower():
    name = request.form['name']
    price = request.form['price']
    return redirect(f'/lab2/ad_flower/{name}/{price}')

@app.route('/lab2/ad_flower/<name>/<int:price>')
def addflower2(name, price):
    flower_list.append({'name': name, 'price': price})
    return redirect('/lab2/flower/countandnames')

@app.route('/lab2/ad_flower/')
def addflowerlost():
    return render_template('addflowerlist.html'), 400

@app.route('/lab2/flower/countandnames')
def countflowers():
    return render_template('flowers.html', flowers=flower_list)