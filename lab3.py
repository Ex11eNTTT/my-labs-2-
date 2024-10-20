from flask import Blueprint, url_for, redirect, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('color')
    return render_template('/lab3/lab3.html', name=name, name_color=name_color)


@lab3.route('/lab3/cookie')
def lab_cockie():
    resp = make_response('Установки куки!', 200)
    resp.set_cookie('name', 'Alex', max_age=5)
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