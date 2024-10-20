from flask import Blueprint, url_for, redirect, render_template, request
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слеша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слешем'



@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a,b):
    first = a
    second = b
    return render_template('lab2/calc.html', first = first, second = second)

@lab2.route('/lab2/calc/')
def redcalc():
    return redirect("/lab2/calc/1/1")

@lab2.route('/lab2/calc/<int:a>')
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

@lab2.route('/lab2/books')
def bookss():
    return render_template('lab2/books.html', books=books)
    
spisokyagod = [{'name': 'Арбуз', 'photo': '/static/lab2/watermelon.png', 'description':
                'Это самая крупная в мире ягодная культура. Вес отдельных плодов достигает 30 кг. Арбузы'
                'используются не только в пищу: их целебные свойства были оценены косметологами. На основе'
                'измельченных косточек делают кремы и скрабы, антицеллюлитные средства.'},
                {'name': 'Барбис', 'photo': '/static/lab2/barbaris.png', 'description': 'Брусника — низкорослый вечнозеленый кустарник'
                  'с небольшими ягодами ярко-красного цвета. Это дикая культура растет в условиях умеренного климата: в тундре и таежных лесах.'
                    'Полезными свойствами обладают все части растения: побеги, стебли, листья, ягоды. Плоды предпочитают потреблять сырыми: в '
                    'таком виде они сохраняют максимум витаминов.'},{'name': 'Голубика', 'photo': '/static/lab2/golubika.png', 'description': 'Вишня — это дерево или кустарник'
                  'с несколькими стволами (в зависимости от сорта). Ягоды вишни — овальные с косточкой внутри.'
                    'Созревание ягод происходит в период с июня по июль, но на одном дереве все ягоды созревают практически одновременно.'},{
                        'name': 'Брусника', 'photo': '/static/lab2/brusnika.png', 'description': 'Брусника — низкорослый вечнозеленый кустарник с небольшими'
                          'ягодами ярко-красного цвета. Это дикая культура растет в условиях умеренного климата: в тундре и таежных лесах. Полезными'
                            'свойствами обладают все части растения: побеги, стебли, листья, ягоды. Плоды предпочитают потреблять сырыми: в таком виде'
                              'они сохраняют максимум витаминов.'
                    },{'name': 'Клубника', 'photo': '/static/lab2/klubnika.png', 'description': 'Клубника — многолетняя травянистая культура. Оно относится к'
                        'семейству розоцветных. Ягоды на стебле появляются через 20-26 дней с начала цветения.'
                    }]

@lab2.route('/lab2/yagodi')
def yagodis():
    return render_template('lab2/yagodi.html', yagoda = spisokyagod)




@lab2.route('/lab2/example')
def example():
    student = 'Дмитрий Дмитриевич'
    numberlab = 'Лабораторная работа 2'
    numbercourse = '3'
    numbergroup = 'ФБИ-21'
    fruits = [{'name':'яблоки', 'price':100},{'name':'груши', 'price':120},{'name':'апельсины', 'price':80},
              {'name':'мандарины', 'price':95},{'name':'манго', 'price':321},]
    return render_template('lab2/example.html', name=student, lab=numberlab,  course = numbercourse, group = numbergroup, fruits=fruits)

@lab2.route('/lab2/')
def laba():
    return render_template('lab2/lab2.html')

@lab2.route('/lab2/filtres')
def filtres():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase=phrase)




flower_list=[{'name':'роза', 'price': 100},{'name':'тюльпан', 'price': 150}, {'name':'незабудка', 'price': 220},{'name':'ромашка', 'price': 50}]

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list)+1:
        return render_template('lab2/ifflower.html'), 404
    else:
        selected_flower = flower_list[flower_id-1]
        selected_flowerlol = f"Название: {selected_flower['name']}, Цена: {selected_flower['price']}"
        return render_template('lab2/ifflower2.html', selected_flowerlol = selected_flowerlol)

@lab2.route('/lab2/flowers_delete')
def flowersdelete():
    flower_list.clear()
    return  render_template('lab2/flowerdelete.html')

@lab2.route('/lab2/flowers_delete/<int:delete_flower_id>')

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


@lab2.route('/lab2/ad_flowerrr/', methods=['POST'])
def addflower():
    name = request.form['name']
    price = request.form['price']
    return redirect(f'/lab2/ad_flower/{name}/{price}')

@lab2.route('/lab2/ad_flower/<name>/<int:price>')
def addflower2(name, price):
    flower_list.lab2end({'name': name, 'price': price})
    return redirect('/lab2/flower/countandnames')

@lab2.route('/lab2/ad_flower/')
def addflowerlost():
    return render_template('lab2/addflowerlist.html'), 400

@lab2.route('/lab2/flower/countandnames')
def countflowers():
    return render_template('lab2/flowers.html', flowers=flower_list)