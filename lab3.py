from flask import Blueprint, url_for, redirect, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    name_color = request.cookies.get('color')
    return render_template('/lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def lab_cockie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=300)
    resp.set_cookie('age', '20')
    resp.set_cookie('color', 'magenta')
    return resp

@lab3.route('/lab3/delete_cookie')
def lab_delte_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('color')
    return resp

@lab3.route('/lab3/form1')
def lab_form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('/lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order1')
def lab_order1():
    return render_template('/lab3/order1.html')


price=0
@lab3.route('/lab3/pay')
def pay():
    global price
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price = price)


@lab3.route('/lab3/success')
def success():
    return render_template('/lab3/success.html', price = price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    backgroundcolor = request.args.get('backgroundcolor')
    fontsize = request.args.get('fontsize')
    if color or backgroundcolor or fontsize:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color)
        resp.set_cookie('backgroundcolor', backgroundcolor)
        if fontsize:
            resp.set_cookie('fontsize', fontsize)
        return resp
    
    color = request.cookies.get('color')
    backgroundcolor = request.cookies.get('backgroundcolor')
    fontsize = request.cookies.get('fontsize')
    resp = make_response(render_template('lab3/settings.html', color=color, backgroundcolor=backgroundcolor, fontsize=fontsize))
    return resp

@lab3.route('/lab3/ticket')
def ticket():
    return render_template('lab3/ticket.html')


@lab3.route('/lab3/pay_ticket')
def pay_ticket():
    price_ticket = 0
    yearsold = request.args.get('yearsold')
    if int(yearsold) > 18:
        price_ticket = 1000
        yearbilet = 'Взрослый'
    else:
        price_ticket = 700
        yearbilet = 'Детский'
    
    if request.args.get('polka') == 'нижняя' or request.args.get('polka') == 'нижняя боковая':
        price_ticket += 100
    
    if request.args.get('withunderwear') == 'Да':
        price_ticket += 75

    if request.args.get('withbag') == 'Да':
        price_ticket += 250
    if request.args.get('withstrahovka') == 'Да':
        price_ticket += 150
    return render_template('/lab3/ticket_pay.html',price_ticket = price_ticket, yearbilet = yearbilet )

@lab3.route('/lab3/delete_new')
def delete_new():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('fontsize')
    resp.delete_cookie('backgroundcolor')
    resp.delete_cookie('color')
    return resp

smartphones = [{'name': 'tel1', 'price': '100', 'color': 'blue', 'date': '2001'}, {'name': 'tel2', 'price': '110', 'color': 'red', 'date': '2002'},
               {'name': 'tel3', 'price': '120', 'color': 'green', 'date': '1999'},{'name': 'tel4', 'price': '130', 'color': 'white', 'date': '2005'},
               {'name': 'tel5', 'price': '140', 'color': 'yellow', 'date': '2012'},{'name': 'tel6', 'price': '150', 'color': 'purple', 'date': '2001'},
               {'name': 'tel7', 'price': '160', 'color': 'blue', 'date': '2006'},{'name': 'tel8', 'price': '40', 'color': 'green', 'date': '2011'},
               {'name': 'tel9', 'price': '60', 'color': 'blue', 'date': '2014'},{'name': 'tel10', 'price': '114', 'color': 'pink', 'date': '2022'},
               {'name': 'tel11', 'price': '220', 'color': 'blue', 'date': '2024'},{'name': 'tel12', 'price': '223', 'color': 'blue', 'date': '2022'},
               {'name': 'tel13', 'price': '100', 'color': 'blue', 'date': '2002'},{'name': 'tel14', 'price': '144', 'color': 'black', 'date': '2011'},
               {'name': 'tel15', 'price': '300', 'color': 'blue', 'date': '2024'},{'name': 'tel16', 'price': '170', 'color': 'blue', 'date': '2022'},
               {'name': 'tel17', 'price': '230', 'color': 'green', 'date': '2022'},{'name': 'tel18', 'price': '230', 'color': 'yellow', 'date': '2022'},
               {'name': 'tel19', 'price': '400', 'color': 'black', 'date': '1985'},{'name': 'tel20', 'price': '400', 'color': 'black', 'date': '2013'},]

@lab3.route('/lab3/phone')
def phone():
    return render_template('/lab3/phoones.html')


@lab3.route('/lab3/phone_pay')
def phone_price():
    newlistphones = []
    min = request.args.get('min')
    max = request.args.get('max')
    for phone in smartphones:
        if phone['price'] >= min and phone['price'] <= max:
            newlistphones.append(phone)
    return render_template('/lab3/phonesready.html', newlistphones = newlistphones, min=min, max=max)