from flask import Flask, url_for, redirect, render_template, request
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)


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