from flask import Blueprint, url_for, redirect, render_template, request, make_response, session
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны бать заполнены!')
    if x2 == '0':
        return render_template('lab4/div.html', error='Делить на ноль нельзя!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1/x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 0
    if x2 =='':
        x2 = 0
    x1 = int(x1)
    x2 = int(x2)
    result = x1+x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mult-form')
def mult_form():
    return render_template('lab4/mult-form.html')


@lab4.route('/lab4/mult', methods=['POST'])
def mult():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 1
    if x2 =='':
        x2 = 1
    x1 = int(x1)
    x2 = int(x2)
    result = x1*x2
    return render_template('lab4/mult.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны бать заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1-x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/degree-form')
def degree_form():
    return render_template('lab4/degree-form.html')


@lab4.route('/lab4/degree', methods=['POST'])
def degree():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1=='0' and x2 =='0':
        return render_template('lab4/degree.html', error='Нельзя что бы два значения было равно нулю')
    if x1 == '' or x2 == '':
        return render_template('lab4/degree.html', error='Оба поля должны бать заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1**x2
    return render_template('lab4/degree.html', x1=x1, x2=x2, result=result)


tree_count = 0
@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count = tree_count)
    
    operation = request.form.get('operation')
    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count += 1
    
    return redirect('/lab4/tree')

users=[
    {'login': 'alex', 'password': '123', 'sex': 'male', 'realname': 'Алекс Иванов'},
    {'login': 'bob', 'password': '555','sex': 'male', 'realname': 'Боб Тотов'},
    {'login': 'vlad', 'password': '111', 'sex': 'male', 'realname': 'Влад Мышков'},
    {'login': 'saskir', 'password': '444','sex': 'male', 'realname': 'Саскир Попов'},
]

realname1 = ''
@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            for user in users:
                if login == user['login']:
                    global realname1
                    realname1 = user['realname']
        else:
            authorized = False
            login = ''
            realname1 = ''
        return render_template('lab4/login.html', authorized=authorized, realname=realname1)
    login = request.form.get('login')
    password = request.form.get('password')

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    error = 'Неверные логин и/или пароль!'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)


@lab4.route('/lab4/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('lab4/reg.html')
    
    login = request.form.get('login')
    global users
    error = ''

    for user in users:
        if login == user['login']:
            error = 'Пользователь с таким логином уже занят!'
            break  
    
    if error:
        return render_template('lab4/reg.html', error=error)
    
    password = request.form.get('password')
    sex = request.form.get('sex')
    realname = request.form.get('realname')
    new_user = {'login': login, 'password': password, 'sex': sex, 'realname': realname}
    users.append(new_user)
    
    return render_template('lab4/reg.html', regg=realname)

@lab4.route('/lab4/list_log')
def list_log():
    if request.method == 'GET':
        if 'login' in session:
            global users
            return render_template('lab4/list_log.html', users=users)
        else:
            return redirect('/lab4/login')
        

@lab4.route('/lab4/log_delete', methods=['POST'])
def log_delete():
    global users
    users = [user for user in users if user['login'] != session['login']]
    return redirect('/lab4/logout')

@lab4.route('/lab4/log_change', methods=['GET','POST'])
def log_change():
    if request.method == 'GET':
        if 'login' in session:
            return render_template('lab4/list_log.html', change = True)
        else:
            return redirect('/lab4/login')
    password = request.form.get('password')
    realname = request.form.get('realname')
    global users
    if password != '':
        for user in users:
            if user['login'] == session['login']:
                user['password'] = password
    if realname != '':
        for user in users:
            if user['login'] == session['login']:
                user['realname'] = realname
    return redirect('/lab4/list_log')





@lab4.route('/lab4/logout', methods=['POST', 'GET'])
def logout():
    if request.method == 'GET':
        if 'login' in session:
            session.pop('login', None)
            return redirect('/lab4/login')
        else:
            return redirect('/lab4/login')
        
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/holod', methods = ['GET', 'POST'])
def holod():
    if request.method == 'GET':
        if 'temp' in session:
            temp = session['temp']
            if int(temp)<(-12):
                error = 'Не удалось установить температуру слишком низкое значение'
                return  render_template('lab4/holod.html', error = error)
            elif int(temp)>(-1):
                error = 'Не удалось установить температуру слишком высокое значение'
                return  render_template('lab4/holod.html', error = error)
            elif int(temp)>(-12) and int(temp)<(-9):
                znak = "❄️❄️❄️"
                return render_template('lab4/holod.html', temp = temp, znak = znak)
            elif int(temp)>(-8) and int(temp)<(-5):
                znak = "❄️❄️"
                return render_template('lab4/holod.html', temp = temp, znak = znak)
            else:
                znak = "❄️"
                return render_template('lab4/holod.html', temp = temp, znak = znak)
        else:
            error = 'Не задана температура!'
            return render_template('lab4/holod.html', error=error)
    
    temp = request.form.get('temp')
    session['temp'] = temp
    return redirect('/lab4/holod')



@lab4.route('/lab4/zerno', methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
            return render_template('lab4/zerno.html')
    
#######################Укзать вес и возврат к странице!!!!!!!!!!!!! попробой переменные в начале error первее
    zerno = request.form.get('zerno')
    col = request.form.get('col')
    if zerno == 'yachmen':
        zerno = 'ячмень'
        price = 12345
    elif zerno == 'oves':
        zerno = 'овес'
        price = 8522
    elif zerno == 'psheno':
        zerno = 'пшеница'
        price = 8722
    else:
        zerno = 'рожь'
        price = 14111


    if int(col) == 0:
        error = "Вес может быть строго больше 0!"
        return render_template('lab4/zerno.html', error=error)
    elif int(col) > 500:
        error = "Такого объема сейчас не в наличии"
        return render_template('lab4/zerno.html', error=error)
    elif int(col) < 50:
        price = price * int(col)
        return render_template('lab4/zerno.html', price=price, zerno=zerno, col=col)
    else:
        skidka = 'Скидка применена за большой объем'
        skidkaint = (price*int(col)*0.1)
        price = price*int(col) - skidkaint
        return render_template('lab4/zerno.html', price=price, zerno=zerno, skidka=skidka, skidkaint = skidkaint, col=col)